from pages.cart_page import AmazonCartPage
from pages.home_page import AmazonHomePage
from pages.product_page import AmazonProductPage
from pages.search_results_page import AmazonSearchResultsPage
from utilities.loggers import get_logger

logger = get_logger(__name__)

class TestAmazon:

    def test_01_search_product(self, driver):
        logger.info("\n" + "="*80)
        logger.info("TEST CASE 1: Search for iPhone 14")
        logger.info("="*80)

        home_page = AmazonHomePage(driver)
        results_page = AmazonSearchResultsPage(driver)

        home_page.search_product("iphone 14")

        assert results_page.get_results_count() > 0, "No results found"
        assert results_page.has_text_in_results("iPhone"), "iPhone not in results"

        logger.info("TEST CASE 1 COMPLETED")

    def test_02_apply_filter(self, driver):
        logger.info("\n" + "="*80)
        logger.info("TEST CASE 2: Apply HP Filter")
        logger.info("="*80)

        home_page = AmazonHomePage(driver)
        results_page = AmazonSearchResultsPage(driver)

        home_page.search_product("laptop")
        results_page.apply_hp_filter()

        assert results_page.has_text_in_results("HP"), "HP not in filtered results"

        logger.info("TEST CASE 2 COMPLETED")

    def test_03_validate_product_details(self, driver):
        logger.info("\n" + "="*80)
        logger.info("TEST CASE 3: Validate Product Details")
        logger.info("="*80)

        home_page = AmazonHomePage(driver)
        results_page = AmazonSearchResultsPage(driver)
        product_page = AmazonProductPage(driver)

        home_page.search_product("headphones")
        results_page.click_first_product()
        product_page.switch_to_new_window()

        assert product_page.is_title_visible(), "Title not visible"
        assert product_page.is_price_visible(), "Price not visible"
        assert product_page.is_rating_visible(), "Rating not visible"

        logger.info("TEST CASE 3 COMPLETED")

    def test_04_add_to_cart(self, driver):
        logger.info("\n" + "="*80)
        logger.info("TEST CASE 4: Add to Cart")
        logger.info("="*80)

        home_page = AmazonHomePage(driver)
        results_page = AmazonSearchResultsPage(driver)
        product_page = AmazonProductPage(driver)

        initial_count = home_page.get_cart_count()
        logger.info(f"Initial cart count: {initial_count}")

        home_page.search_product("mouse")
        results_page.click_first_product()
        product_page.switch_to_new_window()
        product_page.add_to_cart()
        new_count = home_page.get_cart_count()
        logger.info(f"New cart count: {new_count}")

        assert new_count > initial_count, "Cart count did not increase"

        logger.info("TEST CASE 4 COMPLETED ")

    def test_05_remove_from_cart(self, driver):
        logger.info("\n" + "="*80)
        logger.info("TEST CASE 5: Remove from Cart")
        logger.info("="*80)
        home_page = AmazonHomePage(driver)
        results_page = AmazonSearchResultsPage(driver)
        product_page = AmazonProductPage(driver)
        cart_page = AmazonCartPage(driver)
        home_page.search_product("mouse")
        results_page.click_first_product()
        product_page.switch_to_new_window()
        product_page.add_to_cart()
        home_page.click_cart()
        assert cart_page.get_items_count() > 0, "Cart already empty"
        while cart_page.get_items_count() > 0:
            cart_page.remove_first_item()

        assert cart_page.is_empty(), "Cart not empty"

        logger.info("TEST CASE 5 COMPLETED")