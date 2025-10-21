from config.config import TestData
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from pages.Dash_Board_Page import DashboardPage


class LoginPage(BasePage):
    # Locators
    USERNAME = (By.ID, "input-email")
    PASSWORD = (By.ID, "input-password")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Log In']")
    PROFILE_ICON = (By.XPATH, "//div[@class='user-container']")
    LOGOUT_BUTTON = (By.XPATH, "//span[normalize-space()='Log out']")
    FORGOT_LINK = (By.XPATH, "//a[normalize-space()='Forgot Password?']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.get(TestData.BASE_URL)

    def get_login_page_title(self, title):
        return self.get_title(title)

    def is_forgot_link_exist(self):
        return self.is_isvisible(self.FORGOT_LINK)

    def do_login(self, username, password):
        self.do_send_keys(self.USERNAME, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        return DashboardPage(self.driver)