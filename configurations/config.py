import configparser
from pathlib import Path

class Config:
    BASE_DIR = Path(__file__).resolve().parent.parent
    CONFIG_FILE = BASE_DIR / "configurations" / "config.ini"

    config = configparser.RawConfigParser()
    config.read(CONFIG_FILE)

    SCREENSHOTS_DIR = BASE_DIR / "screenshots"
    LOGS_DIR = BASE_DIR / "logs"
    REPORTS_DIR = BASE_DIR / "reports"

    SCREENSHOTS_DIR.mkdir(exist_ok=True)
    LOGS_DIR.mkdir(exist_ok=True)
    REPORTS_DIR.mkdir(exist_ok=True)

    BROWSER = config.get('AMAZON CONFIG', 'BROWSER')
    HEADLESS = config.getboolean('AMAZON CONFIG', 'HEADLESS')

    IMPLICIT_WAIT = config.getint('AMAZON CONFIG', 'IMPLICIT_WAIT')
    EXPLICIT_WAIT = config.getint('AMAZON CONFIG', 'EXPLICIT_WAIT')

    BASE_URL = config.get('AMAZON CONFIG', 'BASE_URL')