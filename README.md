# About
Inspects your Instagram follows and followers to expose who isn't following you back and who you're not following back.
The application prompts you to log in and complete 2FA (if applicable) before gathering all your following and followers. Fetching this data may take a while if you have lots of followers, or follow lots of people. After completion, you will be asked what you'd like to view. The application will also generate 2 files, `non-followers.txt` and `not-following.txt` containing the same details.

## Requirements
- [Python 3.8](https://www.python.org/downloads/) - *may work on other versions*
- BeautifulSoup4 `pip install beautifulsoup4`
- Selenium `pip install selenium`
- [Google Chrome](https://www.google.com/intl/en_uk/chrome/) - *required for ChromeDriver to work*
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) - *install version corresponding to your Chrome version*

## Usage
1. [Download this GitHub repo](https://github.com/AaronVickers/Instagram-Inspector/archive/main.zip) and extract it
2. Put your `chromedriver.exe` in the extracted folder
3. Open terminal and change directory to extracted folder
4. Run `py .`