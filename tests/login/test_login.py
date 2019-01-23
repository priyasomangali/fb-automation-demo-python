from tests.common.global_fixtures import driver, tear
from tests.login.pages.login import LoginPage
from tests.config.settings import *
from tests.login.fixtures.login_fixture import *
from tests.login.locators.login_locators import *


class TestLogin:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = driver()
        cls.invalid_login_data = invalid_login_data()
        cls.login_page = LoginPage(cls.driver)

    def assertions(self, error_loc):
        if self.login_page.is_displayed(error_loc):
            assert True

    def test_valid_login(self):
        self.login_page.login(username, password)
        if self.login_page.is_displayed(fb_post_txt_loc, 'id'):
            assert True
            self.login_page.click(navigation_icon_loc, 'id')
            self.login_page.click(logout_loc)

    def test_invalid_email(self):
        self.login_page.login(self.invalid_login_data['username'], password)
        self.assertions(login_email_error_popover_loc)

    def test_invalid_password(self):
        self.login_page.login(username, self.invalid_login_data['password'])
        self.assertions(login_password_error_popover_loc)

    def test_login_with_empty_creds(self):
        self.login_page.login('', '')
        self.assertions(login_email_error_popover_loc)

    def test_login_with_only_email(self):
        self.login_page.login(username, '')
        self.assertions(login_password_error_popover_loc)

    def test_login_with_only_password(self):
        self.login_page.login('', password)
        self.assertions(login_email_error_popover_loc)

    def test_login_with_invalid_creds(self):
        self.login_page.login(self.invalid_login_data['username'], self.invalid_login_data['password'])
        self.assertions(login_email_error_popover_loc)
