# import pytest
# import datetime
# from config.config import TestData
# from logs.logs_page import Log_Maker
# from pages.Create_Company_Page import Add_Company
# from pages.LogIn_Page import LoginPage
# from tests.test_base import BaseTest
#
#
# @pytest.mark.usefixtures("init_driver")
# class Test_Create_Company(BaseTest):
#     logger = Log_Maker.log_gen()
#
#     def test_create_company(self):
#         timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         self.logger.info(f"[{timestamp}] ========== Starting test: test_create_company ==========")
#
#         try:
#             # Login
#             self.logger.info(f"[{timestamp}] Initializing Login Page")
#             self.login_page = LoginPage(self.driver)
#
#             timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             self.logger.info(f"[{timestamp}] Performing login with user: {TestData.User_Name}")
#             self.login_page.do_login(TestData.User_Name, TestData.User_Password)
#             self.logger.info(f"[{timestamp}] Logged in to the application successfully")
#
#             # Initialize Add Company Page
#             timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             self.logger.info(f"[{timestamp}] Initializing Add Company Page")
#             self.add_Company = Add_Company(self.driver)
#
#             # Navigate to Add Company
#             timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             self.logger.info(f"[{timestamp}] Navigating to Company Module")
#             self.add_Company.company_module()
#
#             timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             self.logger.info(f"[{timestamp}] Opening Add Company form")
#             self.add_Company.add_company_module()
#
#             # Fill Company Details
#             timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             self.logger.info(f"[{timestamp}] Filling company basic information")
#             self.add_Company.text_field_company_name("Test Company Ltd")
#             self.add_Company.text_field_email("testcompany@example.com")
#             self.add_Company.text_field_password("TestPass@123")
#             self.add_Company.text_field_phone("9876543210")
#
#             # Location Details
#             timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             self.logger.info(f"[{timestamp}] Filling location details")
#             self.add_Company.country_dropdown("India")
#             self.add_Company.state_dropdown("Karnataka")
#             self.add_Company.city_dropdown("Bangalore")
#
#             # GST Details
#             timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             self.logger.info(f"[{timestamp}] Filling GST information")
#             self.add_Company.gst_textfield("18")
#             self.add_Company.gst_number_textfield("29ABCDE1234F1Z5")
#
#             # Service City and Company Type
#             timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             self.logger.info(f"[{timestamp}] Selecting service city and company type")
#             self.add_Company.select_service_city_dropdown("Bangalore")
#             self.add_Company.select_company_type("Private Limited")
#
#             # Commission Details
#             timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             self.logger.info(f"[{timestamp}] Setting commission rates")
#             self.add_Company.company_trip_comm()
#             self.add_Company.trip_comm_rate("100")
#             self.add_Company.company_sub_comm()
#             self.add_Company.comm_per_rate("10")
#
#             # Submit
#             timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             self.logger.info(f"[{timestamp}] Submitting company creation form")
#             self.add_Company.company_sub_button()
#
#             timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             self.logger.info(f"[{timestamp}] Test PASSED: Company created successfully")
#
#         except Exception as e:
#             timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             self.logger.error(f"[{timestamp}] Test FAILED: {str(e)}")
#             raise
#         finally:
#             timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             self.logger.info(f"[{timestamp}] ========== Finished test: test_create_company ==========\n")
#
#     def test_create_company_with_custom_data(self):
#         timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         self.logger.info(f"[{timestamp}] ========== Starting test: test_create_company_with_custom_data ==========")
#
#         try:
#             # Login
#             self.login_page = LoginPage(self.driver)
#             self.login_page.do_login(TestData.User_Name, TestData.User_Password)
#
#             # Initialize and navigate
#             self.add_Company = Add_Company(self.driver)
#             self.add_Company.company_module()
#             self.add_Company.add_company_module()
#
#             # Custom company data
#             timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             company_name = f"AutoTest_Company_{timestamp.replace(':', '').replace('-', '').replace(' ', '_')}"
#             self.logger.info(f"[{timestamp}] Creating company with name: {company_name}")
#
#             self.add_Company.text_field_company_name(company_name)
#             self.add_Company.text_field_email(
#                 f"auto_{timestamp.replace(':', '').replace('-', '').replace(' ', '_')}@test.com")
#             self.add_Company.text_field_password("AutoTest@123")
#             self.add_Company.text_field_phone("9999999999")
#
#             # Fill remaining fields
#             self.add_Company.country_dropdown("India")
#             self.add_Company.state_dropdown("Karnataka")
#             self.add_Company.city_dropdown("Bangalore")
#             self.add_Company.gst_textfield("18")
#             self.add_Company.gst_number_textfield("29AUTOTEST1234Z5")
#             self.add_Company.select_service_city_dropdown("Bangalore")
#             self.add_Company.select_company_type("Private Limited")
#             self.add_Company.company_trip_comm()
#             self.add_Company.trip_comm_rate("150")
#             self.add_Company.company_sub_comm()
#             self.add_Company.comm_per_rate("15")
#             self.add_Company.company_sub_button()
#
#             timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             self.logger.info(f"[{timestamp}] Test PASSED: Custom company created successfully")
#
#         except Exception as e:
#             timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             self.logger.error(f"[{timestamp}] Test FAILED: {str(e)}")
#             raise
#         finally:
#             timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             self.logger.info(
#                 f"[{timestamp}] ========== Finished test: test_create_company_with_custom_data ==========\n")


# test_02_create_company.py
import pytest

from data_file.randomdatagenerator import RandomDataGenerator
from logs.logs_page import Log_Maker
from pages.Create_Company_Page import Add_Company
from tests.test_base import BaseTest
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.mark.order(2)
@pytest.mark.usefixtures("init_driver")
class Test02CreateCompany(BaseTest):
    """Test class for creating companies - No login needed"""
    driver: WebDriver

    @pytest.mark.regression
    def test_create_company(self):
        """Test creating a new company with random data"""
        Log_Maker.info("Test 02: Creating New Company")

        # Generate random company data
        data_generator = RandomDataGenerator()
        data = data_generator.generate_company_data()
        Log_Maker.info(f"📝 Generated company data: {data}")

        # Navigate to Add Company (No login - already logged in!)
        Log_Maker.info("🏢 Navigating to Company Module")
        self.add_Company = Add_Company(self.driver)
        self.add_Company.company_module()
        self.add_Company.add_company_module()

        # Fill Company Details with random data
        Log_Maker.info("✍️ Filling company details")
        self.add_Company.text_field_company_name(data["company_name"])
        self.add_Company.text_field_email(data["email"])
        self.add_Company.text_field_password(data["password"])
        self.add_Company.text_field_phone(data["phone"])

        # Location Details
        Log_Maker.info("📍 Selecting location")
        self.add_Company.country_dropdown("India")
        self.add_Company.state_dropdown("Karnataka")
        self.add_Company.city_dropdown("Bangalore")

        # GST Details
        Log_Maker.info("📄 Entering GST information")
        self.add_Company.gst_textfield(data["gst_text"])
        # self.add_Company.gst_number_textfield(data["gst_number"])

        # Service City and Company Type
        Log_Maker.info("🏙️ Selecting service city and company type")
        self.add_Company.select_service_city_dropdown("Bangalore")
        self.add_Company.select_company_type("Dispatcher")

        # Commission Details
        Log_Maker.info("💰 Setting commission rates")
        self.add_Company.company_trip_comm()
        self.add_Company.trip_comm_rate(data["gst_text"])
        self.add_Company.company_sub_comm()
        self.add_Company.comm_per_rate(data["gst_text"])

        # Submit
        Log_Maker.info("✅ Submitting company creation form")
        self.add_Company.company_sub_button()
        Log_Maker.info(f"✅ Test PASSED: Company '{data['company_name']}' created successfully")

    # def test_create_company_with_existing_data(self):
    #     """Test creating a company using previously generated data"""
    #     Log_Maker.info("Starting test: test_create_company_with_existing_data")
    #
    #     # Load existing company data
    #     data_generator = RandomDataGenerator()
    #     data = data_generator.load_company_data()
    #     Log_Maker.info(f"Loaded company data: {data}")
    #
    #     # Login
    #     self.login_page = LoginPage(self.driver)
    #     self.login_page.do_login(TestData.User_Name, TestData.User_Password)
    #
    #     # Navigate and fill form
    #     self.add_Company = Add_Company(self.driver)
    #     self.add_Company.company_module()
    #     self.add_Company.add_company_module()
    #
    #     # Fill form with loaded data
    #     Log_Maker.info("Filling company details with existing data")
    #     self.add_Company.text_field_company_name(data["company_name"])
    #     self.add_Company.text_field_email(data["email"])
    #     self.add_Company.text_field_password(data["password"])
    #     self.add_Company.text_field_phone(data["phone"])
    #     self.add_Company.country_dropdown("India")
    #     self.add_Company.state_dropdown("Karnataka")
    #     self.add_Company.city_dropdown("Bangalore")
    #     self.add_Company.gst_textfield(data["gst_text"])
    #     self.add_Company.gst_number_textfield(data["gst_number"])
    #     self.add_Company.select_service_city_dropdown("Bangalore")
    #     self.add_Company.select_company_type("Dispatcher")
    #     self.add_Company.company_trip_comm()
    #     self.add_Company.trip_comm_rate(data["gst_text"])
    #     self.add_Company.company_sub_comm()
    #     self.add_Company.comm_per_rate(data["gst_text"])
    #     self.add_Company.company_sub_button()
    #
    #     Log_Maker.info("Test PASSED: Company created with existing data")

    # def test_create_multiple_companies(self):
    #     """Test creating multiple companies with different random data"""
    #     Log_Maker.info("Starting test: test_create_multiple_companies")
    #
    #     # Login once
    #     self.login_page = LoginPage(self.driver)
    #     self.login_page.do_login(TestData.User_Name, TestData.User_Password)
    #
    #     # Create 3 companies with different data
    #     for i in range(1, 4):
    #         Log_Maker.info(f"Creating company #{i}")
    #
    #         # Generate new random data for each company
    #         data_generator = RandomDataGenerator()
    #         data = data_generator.generate_company_data()
    #         Log_Maker.info(f"Company #{i} data: {data}")
    #
    #         # Navigate to Add Company
    #         self.add_Company = Add_Company(self.driver)
    #         self.add_Company.company_module()
    #         self.add_Company.add_company_module()
    #
    #         # Fill company details
    #         self.add_Company.text_field_company_name(data["company_name"])
    #         self.add_Company.text_field_email(data["email"])
    #         self.add_Company.text_field_password(data["password"])
    #         self.add_Company.text_field_phone(data["phone"])
    #         self.add_Company.country_dropdown("India")
    #         self.add_Company.state_dropdown("Karnataka")
    #         self.add_Company.city_dropdown("Bangalore")
    #         self.add_Company.gst_textfield(data["gst_text"])
    #         self.add_Company.gst_number_textfield(data["gst_number"])
    #         self.add_Company.select_service_city_dropdown("Bangalore")
    #         self.add_Company.select_company_type("Dispatcher")
    #         self.add_Company.company_trip_comm()
    #         self.add_Company.trip_comm_rate(data["gst_text"])
    #         self.add_Company.company_sub_comm()
    #         self.add_Company.comm_per_rate(data["gst_text"])
    #         self.add_Company.company_sub_button()
    #
    #         Log_Maker.info(f"Company #{i} '{data['company_name']}' created successfully")
    #
    #     Log_Maker.info("Test PASSED: All 3 companies created successfully")