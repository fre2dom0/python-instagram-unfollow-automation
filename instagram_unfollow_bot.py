import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class InstagramUnfollowBot:
    def __init__(self):
        """
        Initialize the Instagram bot with credentials from environment variables
        """
        self.username = os.getenv('INSTAGRAM_USERNAME')
        self.password = os.getenv('INSTAGRAM_PASSWORD')
        self.driver = None

    def setup_driver(self):
        """
        Set up Firefox driver with appropriate options
        """
        firefox_options = Options()
        firefox_options.add_argument("--start-maximized")
        # Uncomment the line below if you want to run in headless mode
        # firefox_options.add_argument("--headless")
        
        # Set up Firefox driver
        self.driver = webdriver.Firefox(options=firefox_options)
        self.wait = WebDriverWait(self.driver, 10)

    def login(self):
        """
        Login to Instagram using credentials
        """
        try:
            self.driver.get("https://www.instagram.com")
            time.sleep(3)  # Wait for page to load

            # Find and fill username
            username_input = self.wait.until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            username_input.send_keys(self.username)

            # Find and fill password
            password_input = self.driver.find_element(By.NAME, "password")
            password_input.send_keys(self.password)
            password_input.send_keys(Keys.RETURN)

            # Wait for login to complete
            time.sleep(5)
            print("Successfully logged in to Instagram!")
            return True

        except Exception as e:
            print(f"Error during login: {str(e)}")
            return False

    def unfollow_users(self, delay=30):
        """
        Unfollow users with specified delay between actions
        
        Args:
            delay (int): Delay in seconds between unfollow actions
        """
        while True:  # Infinite loop to keep checking for new following buttons
            try:
                # Navigate to profile page
                self.driver.get(f"https://www.instagram.com/{self.username}/")
                time.sleep(5)  # Wait for page to load

                # Click on Following button to open following list
                following_link = self.wait.until(
                    EC.presence_of_element_located(
                        (By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[3]/div/a/span")
                    )
                )
                print("Opening following list")
                following_link.click()
                time.sleep(5)  # Wait for following list to load

                # Find all following buttons with specific class names
                following_buttons = self.driver.find_elements(
                    By.CSS_SELECTOR, 
                    "button._acan, button._acap, button._acat"
                )
                print("Found following buttons:", len(following_buttons))

                if len(following_buttons) == 0:
                    print("No more following buttons found. Exiting...")
                    break

                unfollowed = 0
                for button in following_buttons:
                    try:
                        # Click the Following button
                        print("Clicking to unfollow")
                        button.click()
                        time.sleep(1)

                        # Find and click the Unfollow confirmation button
                        unfollow_button = self.wait.until(
                            EC.presence_of_element_located(
                                (By.XPATH, "//button[contains(text(), 'Unfollow')]")
                            )
                        )
                        unfollow_button.click()
                        
                        print(f"Successfully unfollowed user {unfollowed + 1}")
                        unfollowed += 1
                        time.sleep(delay)  # Wait between actions

                    except Exception as e:
                        print(f"Error unfollowing user: {str(e)}")
                        continue

                print(f"Unfollowed {unfollowed} users in this batch!")

                # If we've unfollowed all buttons in this batch, refresh and continue
                if unfollowed == len(following_buttons) - 1:
                    print("All buttons in this batch unfollowed. Refreshing page...")
                    continue
                else:
                    print("Some buttons couldn't be unfollowed. Exiting...")
                    continue

            except Exception as e:
                print(f"Error in unfollow process: {str(e)}")
                break

    def close(self):
        """
        Close the browser
        """
        if self.driver:
            self.driver.quit()
            print("Browser closed successfully!")

def main():
    # Create bot instance
    bot = InstagramUnfollowBot()
    
    try:
        # Set up driver
        bot.setup_driver()
        
        # Login to Instagram
        if bot.login():
            # Unfollow 5 users with 30 seconds delay between actions
            bot.unfollow_users(delay=5)
            pass
    finally:
        # Always close the browser
        #bot.close()
        pass

if __name__ == "__main__":
    main() 