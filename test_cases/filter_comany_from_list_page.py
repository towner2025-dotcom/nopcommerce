from selenium.webdriver.common.by import By
from base_packages.company_data import Add_Company
from base_packages.company_list_page import Company_List_page
from base_packages.login_admin_page import Login_Admin_Page
from base_packages.random_data_generator import RandomDataGenerator
from utilites.custom_logger import Log_Maker
from utilites.read_properties import Read_Config
import pytest
import time


class Test_05_Filter_Company:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_user_name()
    password = Read_Config.get_user_password()
    logger = Log_Maker.log_gen()
    screenshot_dir = r".\\nopCommerce\\screenShorts.png"

    @pytest.mark.parametrize("search_type", ["name", "email", "phone","type"])
    @pytest.mark.regression
    def test_search_company(self, setup, search_type):
        self.logger.info("====== Test_05_Filter_Company Started ======")
        self.driver = setup
        self.driver.implicitly_wait(20)
        self.driver.get(self.admin_page_url)

        # --- Load previously generated company data ---
        generator = RandomDataGenerator()
        data = generator.load_company_data()

        # --- Admin Login ---
        self.admin_login = Login_Admin_Page(self.driver)
        self.admin_login.enter_username(self.username)
        self.admin_login.enter_password(self.password)
        self.admin_login.click_login()
        self.logger.info("Login Completed")

        # --- Navigate to Company List Page ---
        self.add_company = Add_Company(self.driver)
        self.add_company.company_module()
        company_page = Company_List_page(self.driver)
        company_page.view_company_module()
        time.sleep(2)

        # --- Determine Search Value Based on Type ---
        search_value_map = {
            # "name": data["company_name"],
            # "email": data["email"],
            # "phone": data["phone"]

            "name": "Abbas Pvt Ltd",
            "email": "dudekulaabbas174@gmail.com",
            "phone": "8919893733",
            "type": "Dispatcher"
        }
        search_value = search_value_map[search_type]

        # --- Validate Company Data ---
        self.logger.info(f"Searching company by {search_type}: {search_value}")
        result = company_page.search_company(
            search_type,
            search_value,
            screenshot_dir=self.screenshot_dir
        )
        time.sleep(2)

        if result:
            self.logger.info(f"Company found by {search_type}: {search_value}")
            print(f"Company found by {search_type}: {search_value}")
        else:
            self.logger.warning(f"Company NOT found by {search_type}: {search_value}")
            print(f"Company NOT found by {search_type}: {search_value}")

        assert result, f"Company not found for {search_type}: {search_value}"
        self.logger.info("====== Test_05_Filter_Company Completed ======")
