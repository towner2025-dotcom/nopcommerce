# test_03_filter_company.py
import os
import pytest
import time

from data_file.randomdatagenerator import RandomDataGenerator
from logs.logs_page import Log_Maker
from pages.Create_Company_Page import Add_Company
from pages.List_Comapny_Page import CompanyListPage
from tests.test_base import BaseTest
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.mark.order(3)
@pytest.mark.usefixtures("init_driver")
class Test03FilterCompany(BaseTest):
    driver: WebDriver

    @pytest.mark.parametrize("search_type", ["name", "email", "phone"])
    @pytest.mark.regression
    def test_search_company_by_type(self, search_type):
        Log_Maker.info(f"Test 03: Searching Company by {search_type.upper()}")

        # Load previously saved company data
        generator = RandomDataGenerator()
        data_file_path = os.path.join(os.getcwd(), "data", "company_data.json")

        if not os.path.exists(data_file_path):
            Log_Maker.warning("⚠️ No company data found. Run Test_02_Create_Company first!")
            pytest.skip("Company data not available")

        data = generator.load_company_data()
        Log_Maker.info(f"✅ Company data loaded: {data}")

        # Navigate to Company List (No login - already logged in!)
        Log_Maker.info("🏢 Navigating to Company List")
        add_company_page = Add_Company(self.driver)
        add_company_page.company_module()
        time.sleep(1)

        company_list_page = CompanyListPage(self.driver)
        company_list_page.view_company_module()
        time.sleep(2)

        # Map search type to data
        search_value_map = {
            "name": data["company_name"],
            "email": data["email"],
            "phone": data["phone"]


        }
        search_value = search_value_map[search_type]

        Log_Maker.info(f"🔍 Searching company by {search_type}: {search_value}")

        # Perform search
        result = company_list_page.search_company(search_type, search_value)
        time.sleep(2)

        # Validation
        assert result, f"❌ Company not found for {search_type}: {search_value}"
        Log_Maker.info(f"✅ Company found by {search_type}: {search_value}")

        # Get result count
        count = company_list_page.get_search_result_count()
        Log_Maker.info(f"📊 Total results found: {count}")