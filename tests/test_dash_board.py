# from config.config import TestData
# from pages.LogIn_Page import LoginPage
# from tests.test_base import BaseTest
# import  pytest
#
# class Test_DshBoard(BaseTest):
#     def test_dash_board_admin_type(self):
#        self.loginPage= LoginPage(self.driver)
#        homrPage=self.loginPage.do_login(TestData.User_Name,TestData.User_Password)
#        title=homrPage.get_dashboard_title(TestData.Admin_Type)
#        assert  title==TestData.Admin_Type
    # def test_dash_board_text(self):
    #     self.loginPage = LoginPage(self.driver)
    #     homrPage = self.loginPage.do_login(TestData.User_Name, TestData.User_Password)
    #     title = homrPage.get_dashboard_title(TestData.DASH_BOARD_TEXT)
    #     assert title == TestData.DASH_BOARD_TEXT
    #
    # def test_dash_board_email_icon(self):
    #     self.loginPage = LoginPage(self.driver)
    #     homrPage = self.loginPage.do_login(TestData.User_Name, TestData.User_Password)
    #     assert homrPage.EMAIL_ICON()


import pytest
import datetime
from config.config import TestData
from logs.logs_page import Log_Maker
from pages.LogIn_Page import LoginPage
from tests.test_base import BaseTest


@pytest.mark.usefixtures("init_driver")
class Test_DashBoard(BaseTest):
    logger = Log_Maker.log_gen()

    def test_dash_board_admin_type(self):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.logger.info(f"[{timestamp}] ========== Starting test: test_dash_board_admin_type ==========")
        try:
            self.logger.info(f"[{timestamp}] Initializing Login Page")
            self.loginPage = LoginPage(self.driver)

            self.logger.info(f"[{timestamp}] Performing login with user: {TestData.User_Name}")
            homePage = self.loginPage.do_login(TestData.User_Name, TestData.User_Password)

            self.logger.info(f"[{timestamp}] Getting dashboard title")
            title = homePage.get_dashboard_title(TestData.Admin_Type)

            self.logger.info(f"[{timestamp}] Expected title: {TestData.Admin_Type}, Actual title: {title}")
            assert title == TestData.Admin_Type, f"Expected title '{TestData.Admin_Type}', got '{title}'"

            self.logger.info(f"[{timestamp}] Test PASSED: Dashboard admin type matches expected value")
        except Exception as e:
            self.logger.error(f"[{timestamp}] Test FAILED: {str(e)}")
            raise
        finally:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.logger.info(f"[{timestamp}] ========== Finished test: test_dash_board_admin_type ==========\n")
