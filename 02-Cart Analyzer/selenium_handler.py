from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


class SeleniumHandler:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")
        
        # Connect to the existing Chrome instance
        self.driver = webdriver.Chrome(options=chrome_options)


    def open_new_tab_take_screenshots(self, url):
        # Now you can open a new tab in the existing Chrome window
        self.driver.switch_to.new_window('tab')
        self.driver.get(url)


        time.sleep(2)  # Wait for the page to load

        scroll_pause_time = 2  # seconds
        scroll_height = self.driver.execute_script("return document.body.scrollHeight")
        current_position = 0
        screenshot_count = 1

        last_position = -1  # Track the last scroll position

        while True:
            self.driver.save_screenshot(f"screenshots/screenshot_{screenshot_count}.png")
            screenshot_count += 1

            # Scroll down by window height
            self.driver.execute_script("window.scrollBy(0, window.innerHeight);")
            time.sleep(scroll_pause_time)

            # Get new scroll position
            current_position = self.driver.execute_script("return window.pageYOffset + window.innerHeight;")
            scroll_height = self.driver.execute_script("return document.body.scrollHeight")

            # Stop if we've reached the bottom or can't scroll further
            if current_position >= scroll_height or current_position == last_position:
                break

            last_position = current_position


        self.driver.quit()


# use the below command to open a google chrome extension in a debugging mode
# once you do this, you will be able to open new tabs in this instance from selenium

# /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="/tmp/chrome-debug"