# Instagram Unfollow Automation Bot

This Python script automates the process of unfollowing users on Instagram using Selenium and Firefox. It opens a real browser window and performs actions like a human user.

## Features

- Uses Selenium with Firefox for browser automation
- Handles Instagram's following list
- Automatic page refresh when all visible users are unfollowed
- Configurable delay between actions
- Error handling and logging

## Requirements

- Python 3.x
- Firefox browser
- GeckoDriver (Firefox WebDriver)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/instagram-unfollow-automation.git
cd instagram-unfollow-automation
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Install Firefox and GeckoDriver:
- Download and install [Firefox](https://www.mozilla.org/firefox/new/)
- Download [GeckoDriver](https://github.com/mozilla/geckodriver/releases) for your system
- Add GeckoDriver to your system PATH

4. Create a `.env` file in the project root:
```
INSTAGRAM_USERNAME=your_username
INSTAGRAM_PASSWORD=your_password
```

## Usage

Run the script:
```bash
python instagram_unfollow_bot.py
```

The bot will:
1. Open Firefox browser
2. Log in to Instagram
3. Navigate to your profile
4. Open following list
5. Start unfollowing users
6. Refresh the page when all visible users are unfollowed
7. Continue until no more users are found

## Customization

You can modify the following parameters in the code:
- `delay`: Time to wait between unfollow actions (in seconds)

## Important Notes

- Instagram has rate limits, so be careful with the delay between actions
- Using automation tools might violate Instagram's terms of service
- Use this script responsibly and at your own risk
- The script uses a real browser window, so you can see what's happening

## License

This project is licensed under the MIT License - see the LICENSE file for details. 