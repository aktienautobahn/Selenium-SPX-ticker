
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os
import time
#current directory
basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

# db_path = os.path.join(basedir, 'cafes.db')

# function to take care of downloading file
# def enable_download_headless(browser,download_dir):
#     browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
#     params = {'cmd':'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
#     browser.execute("send_command", params)

# instantiate a chrome options object so you can set the size and headless preference
# some of these chrome options might be uncessary but I just used a boilerplate
# change the <path_to_download_default_directory> to whatever your default download folder is located
chrome_options = Options()
# chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--window-size=1920x1080")
# chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--verbose')
chrome_options.add_argument('"--disable-dev-shm-usage"')
chrome_options.add_experimental_option("prefs", {
        "download.default_directory": "<path_to_download_default_directory>",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing_for_trusted_sources_enabled": False,
        "safebrowsing.enabled": False
})
chrome_options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})

# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--disable-software-rasterizer')


# # chrome driver path
# time.sleep(10)
print('options determined')
# initialize driver object and change the <path_to_chrome_driver> depending on your directory where your chromedriver should be
driver = webdriver.Remote("http://localhost:4444/wd/hub", options=chrome_options)

#
print('driver initialised and connected')



# change the base to your directory where you would like to place the downloaded file
download_dir = basedir

# function to handle setting up headless download
# enable_download_headless(driver, download_dir)

time.sleep(4)
# get request to target the site selenium is active on
driver.get("https://www.sectorspdr.com/mainfund/XLC")
time.sleep(6)
# iframe = driver.find_element(By.ID, "__BVID__115")
# ActionChains(driver)\
#     .scroll_to_element(iframe)\
#     .perform()
# mouse_tracker = driver.find_element(By.ID, "__BVID__114")
# ActionChains(driver)\
#     .move_to_element_with_offset(mouse_tracker, 8, 0)\
#     .perform()
# time.sleep(1)
hoverable = driver.find_element(By.ID, "__BVID__115")
ActionChains(driver)\
    .move_to_element(hoverable)\
    .perform()
# initialize an object to the location on the html page and click on it to download
try:
    search_input = driver.find_element(By.XPATH, '//*[@id="__BVID__115"]/div/div[1]/div[2]/button[1]')
except:
    search_input = driver.find_element(By.CSS_SELECTOR, '#__BVID__115 > div > div.fds-fund-topper > div:nth-child(2) > button:nth-child(2)')
print(search_input)
search_input.click()
time.sleep(3)
driver.close()