# from pages.BasePage import BasePage
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class DashboardPage(BasePage):
#
#     # Locators
#     ADMIN_TYPE = (By.XPATH, "//span[normalize-space()='superadmin']")
#     DASHBOARD_TEXT = (By.XPATH, "//span[normalize-space()='Dashboard']")
#     EMAIL_ICON = (By.XPATH, "//i[@class='control-icon nb-email']")
#
#     def __init__(self, driver):
#         super().__init__(driver)
#
#     def get_dashboard_title(self, title):
#         WebDriverWait(self.driver, 10).until(EC.title_is(title))
#         return self.driver.title
#
#     def get_admin_type_text(self):
#         if self.is_isvisible(self.ADMIN_TYPE):
#             return  self.get_element_text(self.ADMIN_TYPE)
#
#     def is_email_icon_visible(self):
#         return self.is_isvisible(self.EMAIL_ICON)
#


from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage(BasePage):

    # Locators
    ADMIN_TYPE = (By.XPATH, "//span[normalize-space()='superadmin']")
    DASHBOARD_TEXT = (By.XPATH, "//span[normalize-space()='Dashboard']")
    EMAIL_ICON = (By.XPATH, "//i[@class='control-icon nb-email']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_dashboard_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def get_admin_type_text(self):
        if self.is_visible(self.ADMIN_TYPE):
            return self.get_element_text(self.ADMIN_TYPE)

    def is_email_icon_visible(self):
        return self.is_visible(self.EMAIL_ICON)