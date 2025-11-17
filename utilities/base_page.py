from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configurations.config import Config
from utilities.loggers import get_logger
from datetime import datetime

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)
        self.logger = get_logger(self.__class__.__name__)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find_element(locator).text

    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def switch_to_new_window(self):
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[-1])

    def close_and_switch_back(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def take_screenshot(self, name):
        timestamp = datetime.now().strftime("%Y-%m-%d::%H:%M:%S")
        path = Config.SCREENSHOTS_DIR / f"{name}_{timestamp}.png"
        self.driver.save_screenshot(str(path))
        return str(path)