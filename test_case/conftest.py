import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from configurations.config import Config
from utilities.loggers import get_logger
import os
import stat

logger = get_logger(__name__)

@pytest.fixture
def driver():
    logger.info("="*80)
    logger.info("STARTING BROWSER SESSION")
    logger.info("="*80)

    chrome_options = Options()

    if Config.HEADLESS:
        chrome_options.add_argument('--headless')
        logger.info("Running in HEADLESS mode")

    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver_path = ChromeDriverManager().install()

    if 'THIRD_PARTY_NOTICES' in driver_path:
        driver_dir = os.path.dirname(driver_path)
        driver_path = os.path.join(driver_dir, 'chromedriver')

    os.chmod(driver_path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IROTH | stat.S_IXOTH)

    driver = webdriver.Chrome(
        service=Service(driver_path),
        options=chrome_options
    )

    driver.maximize_window()
    driver.implicitly_wait(Config.IMPLICIT_WAIT)
    driver.get(Config.BASE_URL)
    logger.info(f"Navigated to: {Config.BASE_URL}")

    yield driver

    logger.info("CLOSING BROWSER SESSION")
    driver.quit()
    logger.info("="*80)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call':
        if report.failed:
            logger.error(f"TEST FAILED: {item.name}")
            driver = item.funcargs.get('driver')
            if driver:
                from utilities.base_page import BasePage
                BasePage(driver).take_screenshot(f"FAILED_{item.name}")
        elif report.passed:
            logger.info(f"TEST PASSED: {item.name}")