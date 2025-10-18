import time

import pytest

from base_packages.company_data import Add_Company
from base_packages.login_admin_page import Login_Admin_Page
from base_packages.random_data_generator import RandomDataGenerator
from utilites.custom_logger import Log_Maker
from utilites.read_properties import Read_Config


class Test_04_Add_Company:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_user_name()
    password = Read_Config.get_user_password()
    logger = Log_Maker.log_gen()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_add_company(self, setup):
        """Test to add a new company"""
        self.driver = setup
        self.driver.implicitly_wait(20)
        self.driver.get(self.admin_page_url)

        # --- Generate and Save Random Data ---
        generator = RandomDataGenerator()
        data = generator.generate_company_data()
        company_name = data["company_name"]

        # --- Admin Login ---
        self.admin_login = Login_Admin_Page(self.driver)
        self.admin_login.enter_username(self.username)
        self.admin_login.enter_password(self.password)
        self.admin_login.click_login()
        self.logger.info("✅ Login Completed")

        # --- Add Company ---
        self.add_company = Add_Company(self.driver)
        self.add_company.company_module()
        self.add_company.add_company_module()

        self.add_company.text_field_company_name(company_name)
        self.add_company.text_field_email(data["email"])
        self.add_company.text_field_password(data["password"])
        self.add_company.text_field_phone(data["phone"])

        self.add_company.country_dropdown("India")
        self.add_company.state_dropdown("Karnataka")
        self.add_company.city_dropdown("Bangalore")

        self.add_company.gst_textfield(data["gst_text"])
        self.add_company.gst_number_textfield(data["gst_number"])
        self.add_company.select_service_city_dropdown("Bangalore")
        self.add_company.select_company_type("Dispatcher")

        self.add_company.company_trip_comm()
        self.add_company.trip_comm_rate(data["gst_text"])
        self.add_company.company_sub_comm()
        self.add_company.comm_per_rate(data["gst_text"])
        self.add_company.company_sub_button()

        time.sleep(10)
        self.logger.info("✅ Company Added Successfully")
