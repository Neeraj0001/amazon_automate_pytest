from selenium.webdriver.common.by import By
from utilities.base_page import BasePage
import time

class AmazonCartPage(BasePage):

    CART_ITEMS = (By.CSS_SELECTOR, "div.sc-list-item-content")
    DELETE_BUTTON = (By.CSS_SELECTOR, "input[value='Delete']")
    CART_COUNT = (By.ID, "nav-cart-count")

    def get_items_count(self):
        try:
            count = len(self.find_elements(self.CART_ITEMS))
            self.logger.info(f"Cart has {count} items")
            return count
        except:
            self.logger.info("Cart is empty")
            return 0

    def remove_first_item(self):
        buttons = self.find_elements(self.DELETE_BUTTON)
        if buttons:
            buttons[0].click()
            time.sleep(2)

    def is_empty(self):
        return self.get_text(self.CART_COUNT)=='0'