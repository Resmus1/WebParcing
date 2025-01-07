#  https://stepik.org/lesson/1164759/step/1?unit=1177103

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

LEFT_CLICK_BUTTON = ("xpath", "//button[@id='leftClick']")
DOUBLE_CLICK_BUTTON = ("xpath", "//button[@id='doubleClick']")
RIGHT_CLICK_BUTTON = ("xpath", "//button[@id='rightClick']")
HOVER_CLICK_BUTTON = ("xpath", "//button[@id='colorChangeOnHover']")


with webdriver.Chrome(options=chrome_options) as browser:
    try:
        browser.get("https://testkru.com/Elements/Buttons")
        actions = ActionChains(browser)

        left_button = browser.find_element(*LEFT_CLICK_BUTTON)
        double_button = browser.find_element(*DOUBLE_CLICK_BUTTON)
        right_button = browser.find_element(*RIGHT_CLICK_BUTTON)
        hover_button = browser.find_element(*HOVER_CLICK_BUTTON)

        actions.click(left_button) \
            .double_click(double_button) \
            .pause(2) \
            .context_click(right_button) \
            .pause(2) \
            .move_to_element(hover_button) \
            .pause(2) \
            .perform()

    except Exception as e:
        print(f"Error: {e}")
