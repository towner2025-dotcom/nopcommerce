import os

import pytest
from selenium.webdriver.common.by import By
from base_packages.login_admin_page import Login_Admin_Page
from utilites.read_properties import Read_Config
from utilites.custom_logger import Log_Maker

class Test_01_Admin_Login:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_user_name()
    password12 = Read_Config.get_user_password()
    invalid_username = Read_Config.get_invalid_username()
    logger=Log_Maker.log_gen()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_valid_admin_login(self, setup):
        self.logger.info("******Test_01****** >>>>>test_valid_admin_login<<<<<")
        self.logger.info("******Test_01****** >>>>>With Valued Data<<<<<")
        driver = setup
        driver.get(self.admin_page_url)
        admin_login = Login_Admin_Page(driver)
        admin_login.enter_username(self.username)
        admin_login.enter_password(self.password12)
        admin_login.click_login()
        # Optionally, add assertion:
        # assert driver.find_element(By.XPATH, "//span[normalize-space()='superadmin']").text.upper() == "SUPERADMIN"
    # C:\Users\hp\PycharmProjects\nopCommerce
    @pytest.mark.regression
    def test_invalid_admin_login(self, setup, request):
        self.logger.info("******Test_02****** >>>>>test_valid_admin_login<<<<<")
        self.logger.info("******Test_02****** >>>>>With inValued Data<<<<<")
        driver = setup
        driver.get(self.admin_page_url)
        admin_login = Login_Admin_Page(driver)
        admin_login.enter_username(self.invalid_username)
        admin_login.enter_password(self.password12)
        admin_login.click_login()

        try:
            # Example check for invalid login alert
            act_text = driver.find_element(By.CSS_SELECTOR, "p.alert-title b").text
            assert act_text == "Oh snap!"
            self.logger.info("******Test_02****** >>>>>Data Matching<<<<<")
        except Exception as e:
            self.logger.info("******Test_02****** >>>>>MisMatch<<<<<")
            # Take screenshot on failure
            screenshots_folder = os.path.join(os.getcwd(), "screenShorts")
            os.makedirs(screenshots_folder, exist_ok=True)
            screenshot_path = os.path.join(screenshots_folder, "invalid_login_fail.png")
            driver.save_screenshot(screenshot_path)

            # Log where screenshot is saved
            print(f"❌ Test failed — Screenshot saved at: {screenshot_path}")
            raise e