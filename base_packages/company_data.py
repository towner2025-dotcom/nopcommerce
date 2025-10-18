import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Add_Company:
    # XPaths and names
    company_module_xpath = "//span[text()='Company']"
    add_company_Xpath = "//span[text()='Add Company']"
    company_name_name = "name"
    email_name = "email"
    password_name = "pwd"
    phone_number_name = "phone"
    gst_name = "vat"
    gst_number_name = "vatNumber"
    service_city_name = "scIds"
    company_type_name = "companyType"
    trip_comm_xpath = "(//span[contains(text(),'Flat')])[1]"
    flat_rate_xpath="//input[@placeholder='Rate']"
    sub_comm_xpath = "(//span[contains(text(),'Percentage')])[2]"
    sub_cumm_per_xpath="(//input[@name='rate1'])[1]"
    submit_xpath = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    # ---------- Basic Inputs ----------
    def company_module(self):
        self.driver.find_element(By.XPATH, self.company_module_xpath).click()

    def add_company_module(self):
        self.driver.find_element(By.XPATH, self.add_company_Xpath).click()

    def text_field_company_name(self, fname):
        self.driver.find_element(By.NAME, self.company_name_name).send_keys(fname)

    def text_field_email(self, email):
        self.driver.find_element(By.NAME, self.email_name).send_keys(email)

    def text_field_password(self, password):
        self.driver.find_element(By.NAME, self.password_name).send_keys(password)

    def text_field_phone(self, phone):
        self.driver.find_element(By.NAME, self.phone_number_name).send_keys(phone)

    def gst_textfield(self, value):
        self.driver.find_element(By.NAME, self.gst_name).send_keys(value)

    def gst_number_textfield(self, value):
        self.driver.find_element(By.NAME, self.gst_number_name).send_keys(value)

    def select_from_list(self, dropdown_placeholder, value_to_select):
        """
        Clicks a dropdown, grabs all list items, and clicks the matching value.
        Works for Angular/ng-select dropdowns.
        """
        try:
            # 1. Click the dropdown placeholder to open the list
            dropdown = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH,
                     f"//div[contains(@class,'placeholder') and normalize-space(text())='{dropdown_placeholder}']")
                )
            )
            dropdown.click()

            # 2. Wait for the list items to appear
            list_items = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, "//li[contains(@class,'ng-star-inserted')]")
                )
            )

            # 3. Loop through list items and click the matching one
            for item in list_items:
                text = item.text.strip()
                if value_to_select.lower() == text.lower():
                    # Move to the element and click
                    ActionChains(self.driver).move_to_element(item).click().perform()
                    print(f"Selected: {text}")
                    return

            print(f"No matching item found for '{value_to_select}'")

        except Exception as e:
            print(f"Error selecting '{value_to_select}': {e}")

    # Specific dropdown methods
    def country_dropdown(self, country_name):
        self.select_from_list("Select a Country", country_name)

    def state_dropdown(self, state_name):
        self.select_from_list("Select a State / Provinces", state_name)

    def city_dropdown(self, city_name):
        self.select_from_list("Select a City", city_name)

    def select_service_city_dropdown(self, value):
        try:
            # 1. Open the multiselect dropdown
            self.driver.find_element(By.NAME, self.service_city_name).click()
            time.sleep(0.5)

            # 2. Type into the search box
            search_box = self.driver.find_element(By.XPATH, "//input[@placeholder='Search']")
            search_box.clear()
            search_box.send_keys(value)
            time.sleep(1)

            # 3. Wait for the matching <li> to appear
            option_xpath = f"//li[contains(@class,'multiselect-item-checkbox') and contains(translate(.,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'{value.lower()}')]"
            option_li = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, option_xpath))
            )

            # 4. Click the inner <div> inside <li> (Angular requires it)
            option_div = option_li.find_element(By.XPATH, ".//div")
            ActionChains(self.driver).move_to_element(option_div).click().perform()

            print(f"✅ Selected service city: {value}")
            time.sleep(0.5)

        except Exception as e:
            print(f"❌ Could not select service city '{value}': {e}")

    # ---------- Company Type Dropdown ----------
    def select_company_type(self, value):
        try:
            dropdown = self.driver.find_element(By.NAME, self.company_type_name)
            select = Select(dropdown)
            select.select_by_visible_text(value)
            print(f"✅ Selected company type: {value}")
            time.sleep(0.5)
        except Exception as e:
            print(f"❌ Could not select company type '{value}': {e}")

    # ---------- Commissions ----------
    def company_trip_comm(self):
        self.driver.find_element(By.XPATH, self.trip_comm_xpath).click()
    def trip_comm_rate(self, value):
        self.driver.find_element(By.XPATH, self.flat_rate_xpath).send_keys(value)

    def company_sub_comm(self):
        self.driver.find_element(By.XPATH, self.sub_comm_xpath).click()

    def comm_per_rate(self, value):
        self.driver.find_element(By.XPATH, self.sub_cumm_per_xpath).send_keys(value)

    # ---------- Submit ----------
    def company_sub_button(self):
        self.driver.find_element(By.XPATH, self.submit_xpath).click()
