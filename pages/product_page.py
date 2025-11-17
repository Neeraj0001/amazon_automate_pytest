from selenium.webdriver.common.by import By
from utilities.base_page import BasePage
import time

class AmazonProductPage(BasePage):

    TITLE = (By.ID, "productTitle")
    PRICE = (By.CSS_SELECTOR, "span.a-price-whole")
    RATING = (By.ID, "acrCustomerReviewText")
    ADD_TO_CART = (By.ID, "add-to-cart-button")

    def is_title_visible(self):
        return self.is_visible(self.TITLE)

    def is_price_visible(self):
        return self.is_visible(self.PRICE)

    def is_rating_visible(self):
        return self.is_visible(self.RATING)

    def add_to_cart(self):
        self.click(self.ADD_TO_CART)
        time.sleep(2)