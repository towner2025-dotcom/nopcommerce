import os
import time
from selenium.webdriver.common.by import By
from base_packages.login_admin_page import Login_Admin_Page
from utilites.read_properties import Read_Config
from utilites.custom_logger import Log_Maker
from utilites import excel_utilitys
# https://admin-demo.nopcommerce.com/login?returnurl=%2Fadmin%2F

class Test_02_Admin_Login_Data_Driven:
    admin_page_url = Read_Config.get_admin_page_url()
    logger = Log_Maker.log_gen()
    path = ".//test_data//Admin Login Data.xlsx"  # ✅ Correctly declared as class variable (no self)

    def test_valid_admin_login_ddt(self, setup):
        self.logger.info("****** Test_02_Admin_Login_Data_Driven ******")
        self.logger.info("****** Running Data-Driven Test for Admin Login ******")

        driver = setup
        driver.implicitly_wait(5)
        driver.get(self.admin_page_url)
        admin_login = Login_Admin_Page(driver)

        status_list = []

        # Get total row count from Excel
        rows = excel_utilitys.get_row_count(self.path, "Sheet1")
        self.logger.info(f"Total Rows in Excel: {rows}")

        for r in range(2, rows + 1):
            username = excel_utilitys.read_data(self.path, "Sheet1", r, 1)
            password = excel_utilitys.read_data(self.path, "Sheet1", r, 2)
            exp_login = excel_utilitys.read_data(self.path, "Sheet1", r, 3)

            # ✅ Make sure exp_login is a string
            if not exp_login:
                self.logger.warning(f"Row {r}: 'exp_login' is empty. Skipping this row.")
                continue
            exp_login = str(exp_login).strip()  # Remove extra spaces

            self.logger.info(f"Testing with Username: {username} | Password: {password} | Expected: {exp_login}")

            admin_login.enter_username(username)
            admin_login.enter_password(password)
            admin_login.click_login()
            time.sleep(3)

            actual_title = driver.title
            expected_title = "Towner"

            # --- Logic for result validation ---
            if actual_title == expected_title:
                if exp_login.lower() == "yes":
                    self.logger.info("✅ Login passed (expected pass)")
                    status_list.append("Pass")

                    # Logout
                    try:
                        admin_login.logout()
                        self.logger.info("✅ Successfully logged out after valid login.")
                    except Exception as e:
                        self.logger.warning(f"⚠️ Logout failed: {e}")

                else:
                    self.logger.info("❌ Login passed (expected fail)")
                    status_list.append("Fail")
            else:
                if exp_login.lower() == "yes":
                    self.logger.info("❌ Login failed (expected pass)")
                    status_list.append("Fail")
                else:
                    self.logger.info("✅ Login failed (expected fail)")
                    status_list.append("Pass")

            # Navigate back to login page
            driver.get(self.admin_page_url)
            time.sleep(2)

        # --- Final validation ---
        self.logger.info(f"Test status list: {status_list}")
        if "Fail" in status_list:
            self.logger.error("❌ Data Driven Test FAILED.")
            self.take_screenshot(driver, "ddt_test_failed.png")
            assert False
        else:
            self.logger.info("✅ Data Driven Test PASSED.")
            assert True

    def take_screenshot(self, driver, filename):
        """Save screenshot to the screenShorts folder"""
        screenshots_folder = os.path.join(os.getcwd(), "screenShorts")
        os.makedirs(screenshots_folder, exist_ok=True)
        screenshot_path = os.path.join(screenshots_folder, filename)
        driver.save_screenshot(screenshot_path)
        self.logger.info(f"📸 Screenshot saved at: {screenshot_path}")
