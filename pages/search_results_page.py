from selenium.webdriver.common.by import By
from utilities.base_page import BasePage
import time

class AmazonSearchResultsPage(BasePage):

    SEARCH_RESULTS = (By.CSS_SELECTOR, "div[data-component-type='s-search-result']")
    PRODUCT_TITLES = (By.CSS_SELECTOR, "h2 span")
    FIRST_PRODUCT = (By.XPATH, "(//*[@role='listitem']//a)[1]")
    BRAND_HP = (By.XPATH, "//a[contains(@aria-label, 'HP')]")

    def get_results_count(self):
        try:
            count = len(self.find_elements(self.SEARCH_RESULTS))
            return count
        except:
            return 0

    def has_text_in_results(self, text):
        titles = self.find_elements(self.PRODUCT_TITLES)
        for title in titles[:5]:
            if text.lower() in title.text.lower():
                return True
        return False

    def click_first_product(self):
        self.click(self.FIRST_PRODUCT)
        time.sleep(2)

    def apply_hp_filter(self):
        self.click(self.BRAND_HP)
        time.sleep(2)