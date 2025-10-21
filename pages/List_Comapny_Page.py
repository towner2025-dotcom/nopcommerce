from selenium.webdriver.common.by import By
import time


class CompanyListPage:
    # Locators
    list_page_xpath = "//span[text()='View Company']"
    company_name_search_xpath = "//input[@placeholder='Company Name']"
    company_email_id_xpath = "//input[@placeholder='Email']"
    company_phone_number_xpath = "//input[@placeholder='Phone']"
    company_type_xpath = "//input[@placeholder='companyType']"
    list_row_xpath = "//tbody/tr"

    def __init__(self, driver):
        self.driver = driver

    def view_company_module(self):
        """Click on View Company menu"""
        self.driver.find_element(By.XPATH, self.list_page_xpath).click()

    def get_result_table_row(self):
        """Get total number of rows in result table"""
        return len(self.driver.find_elements(By.XPATH, self.list_row_xpath))

    def get_search_result_count(self):
        """Get count of search results"""
        return self.get_result_table_row()

    def search_company(self, search_type, search_value):
        """
        Search for a company by type (name, email, phone)

        Args:
            search_type: Type of search ('name', 'email', 'phone')
            search_value: Value to search for

        Returns:
            bool: True if match found, False otherwise
        """
        search_fields = {
            "name": self.company_name_search_xpath,
            "email": self.company_email_id_xpath,
            "phone": self.company_phone_number_xpath
        }

        col_index_map = {
            "name": 2,
            "email": 4,
            "phone": 5,
            "type": 7
        }

        if search_type not in search_fields:
            print(f"❌ Invalid search type: {search_type}")
            return False

        try:
            # Clear and type in search field
            search_box = self.driver.find_element(By.XPATH, search_fields[search_type])
            search_box.clear()
            search_box.send_keys(search_value)
            time.sleep(2)  # Wait for table to refresh

            total_rows = self.get_result_table_row()
            match_found = False

            # Iterate through all rows
            for r in range(1, total_rows + 1):
                cell_xpath = f"//tbody/tr[{r}]/td[{col_index_map[search_type]}]"
                cell_text = self.driver.find_element(By.XPATH, cell_xpath).text.strip()

                if cell_text.lower() == str(search_value).lower():
                    print(f"✅ Match found in row {r}: '{cell_text}' == '{search_value}'")
                    match_found = True
                    break
                else:
                    print(f"⚠️ No match in row {r}: '{cell_text}' != '{search_value}'")

            if not match_found:
                print(f"❌ No matching rows found for {search_type}: '{search_value}'")

            return match_found

        except Exception as e:
            print(f"❌ Error searching by {search_type}: {e}")
            return False