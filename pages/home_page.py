from selenium.webdriver.common.by import By
from utilities.base_page import BasePage
import time

class AmazonHomePage(BasePage):

    SEARCH_BOX = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON = (By.ID, "nav-search-submit-button")
    CART_COUNT = (By.ID, "nav-cart-count")
    CART_ICON = (By.ID, "nav-cart")

    def search_product(self, product_name):
        self.logger.info(f"Searching for: {product_name}")
        self.send_keys(self.SEARCH_BOX, product_name)
        self.click(self.SEARCH_BUTTON)
        time.sleep(4)

    def get_cart_count(self):
        try:
            count = int(self.get_text(self.CART_COUNT))
            self.logger.info(f"Cart count: {count}")
            return count
        except:
            return 0

    def click_cart(self):
        self.logger.info("Clicking cart icon")
        self.click(self.CART_ICON)