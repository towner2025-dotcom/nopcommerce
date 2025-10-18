from selenium.webdriver.common.by import By
import time
import os


class Company_List_page:
    list_page_xpath = "//span[text()='View Company']"
    company_name_search_xpath = "//input[@placeholder='Company Name']"
    company_email_id_xpath = "//input[@placeholder='Email']"
    company_phone_number_xpath = "//input[@placeholder='Phone']"
    company_type_xpath = "//input[@placeholder='companyType']"
    list_row_xpath = "//tbody/tr"

    def __init__(self, driver):
        self.driver = driver

    def view_company_module(self):
        self.driver.find_element(By.XPATH, self.list_page_xpath).click()

    def get_result_table_row(self):
        return len(self.driver.find_elements(By.XPATH, self.list_row_xpath))

    def search_company(self, search_type, search_value, screenshot_dir=None):

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
            print(f"Invalid search type: {search_type}")
            return False

        try:
            # Clear and type in search field
            search_box = self.driver.find_element(By.XPATH, search_fields[search_type])
            search_box.clear()
            search_box.send_keys(search_value)
            time.sleep(2)  # wait for table to refresh

            total_rows = self.get_result_table_row()
            match_found = False

            # Iterate all rows
            for r in range(1, total_rows + 1):
                cell_xpath = f"//tbody/tr[{r}]/td[{col_index_map[search_type]}]"
                cell_text = self.driver.find_element(By.XPATH, cell_xpath).text.strip()

                if cell_text.lower() == str(search_value).lower():
                    print(f" Match found in row {r}: '{cell_text}' == '{search_value}'")
                    match_found = True
                    break
                else:
                    print(f" No match in row {r}: '{cell_text}' != '{search_value}'")

            if not match_found:
                print(f"No matching rows found for {search_type}: '{search_value}'")

                # Take screenshot on failure
                folder = screenshot_dir or os.path.join(os.getcwd(), "screenShorts")
                os.makedirs(folder, exist_ok=True)
                screenshot_path = os.path.join(folder, f"{search_type}_not_found_{int(time.time())}.png")
                self.driver.save_screenshot(screenshot_path)
                print(f"📸 Screenshot saved at: {screenshot_path}")

            return match_found

        except Exception as e:
            print(f"Error searching by {search_type}: {e}")
            # Optional: take screenshot on exception
            folder = screenshot_dir or os.path.join(os.getcwd(), "screenShorts")
            os.makedirs(folder, exist_ok=True)
            screenshot_path = os.path.join(folder, f"{search_type}_error_{int(time.time())}.png")
            self.driver.save_screenshot(screenshot_path)
            print(f"📸 Screenshot saved at: {screenshot_path} due to exception")
            return False