from tests.login.pages.login import LoginPage
from selenium import webdriver
import pytest


@pytest.fixture(scope="session")
def driver(login=False):
    driver = webdriver.Chrome()
    driver.fullscreen_window()
    if login:
        driver = LoginPage(driver).login()
    return driver


@pytest.fixture(scope="session")
def tear(dri):
    dri.close()
    dri.quit()
