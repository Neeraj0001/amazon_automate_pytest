# Amazon Automation - PyTest + Selenium

Automated testing framework for Amazon using Selenium, PyTest, and Page Object Model (POM).

## Quick Start

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run Tests
```bash
cd test_case
pytest test_search.py -v
```

## Test Cases

- test_01_search_product - Search for iPhone 17
- test_02_apply_filter - Apply HP filter on laptops
- test_03_validate_product_details - Verify product title, price, rating
- test_04_add_to_cart - Add product to cart
- test_05_remove_from_cart - Remove item from cart

## Configuration

Edit `configuration/config.ini`:

```ini
[AMAZON CONFIG]
BROWSER = chrome
HEADLESS = False
IMPLICIT_WAIT = 10
EXPLICIT_WAIT = 20
BASE_URL = https://www.amazon.in
```

## Reports and Logs

- HTML Report: reports/report.html
- Logs: logs/test_execution.log
- Screenshots: screenshots/ (captured on failure)

## Tech Stack

- Python 3.10+
- Selenium 4.15.2
- PyTest 7.4.3
- WebDriver Manager 4.0.1

## Features

- Page Object Model design pattern
- Automatic screenshot on test failure
- Detailed logging
- HTML test reports
- Configuration-driven

## Author

Neeraj