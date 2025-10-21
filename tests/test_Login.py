import pytest
from config.config import TestData
from logs.logs_page import Log_Maker
from pages.LogIn_Page import LoginPage
from tests.test_base import BaseTest


@pytest.mark.usefixtures("init_driver")
class Test_Login(BaseTest):

    def test_forgot_password_link_visible(self):
        Log_Maker.info("Starting test: test_forgot_password_link_visible")
        self.login_page = LoginPage(self.driver)
        flag = self.login_page.is_forgot_link_exist()
        assert flag, "Forgot Password link is not visible"
        Log_Maker.info("Test PASSED: Forgot Password link is visible")

    def test_title(self):
        Log_Maker.info("Starting test: test_title")
        self.login_page = LoginPage(self.driver)
        title = self.login_page.get_title(TestData.Login_page_Title)
        assert title == TestData.Login_page_Title, f"Expected title '{TestData.Login_page_Title}', got '{title}'"
        Log_Maker.info(f"Test PASSED: Title matches - {title}")

    def test_login(self):
        Log_Maker.info("Starting test: test_login")
        self.login_page = LoginPage(self.driver)
        Log_Maker.info(f"Logging in with username: {TestData.User_Name}")
        self.login_page.do_login(TestData.User_Name, TestData.User_Password)
        Log_Maker.info("Test PASSED: Logged in successfully")