# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait, Select
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
#
# class Add_Company:
#     # ---------------- Locators ----------------
#     COMPANY_MODULE = (By.XPATH, "//span[text()='Company']")
#     ADD_COMPANY = (By.XPATH, "//span[text()='Add Company']")
#     COMPANY_NAME = (By.NAME, "name")
#     EMAIL = (By.NAME, "email")
#     PASSWORD = (By.NAME, "pwd")
#     PHONE_NUMBER = (By.NAME, "phone")
#     GST = (By.NAME, "vat")
#     GST_NUMBER = (By.NAME, "vatNumber")
#     SERVICE_CITY = (By.NAME, "scIds")
#     COMPANY_TYPE = (By.NAME, "companyType")
#     TRIP_COMM = (By.XPATH, "(//span[contains(text(),'Flat')])[1]")
#     FLAT_RATE = (By.XPATH, "//input[@placeholder='Rate']")
#     SUB_COMM = (By.XPATH, "(//span[contains(text(),'Percentage')])[2]")
#     SUB_COMM_PER = (By.XPATH, "(//input[@name='rate1'])[1]")
#     SUBMIT = (By.XPATH, "//button[@type='submit']")
#
#     # ---------------- Constructor ----------------
#     def __init__(self, driver):
#         self.driver = driver
#
#     # ---------------- Navigation ----------------
#     def company_module(self):
#         self.driver.find_element(*self.COMPANY_MODULE).click()
#
#     def add_company_module(self):
#         self.driver.find_element(*self.ADD_COMPANY).click()
#
#     # ---------------- Text Fields ----------------
#     def text_field_company_name(self, value):
#         self.driver.find_element(*self.COMPANY_NAME).send_keys(value)
#
#     def text_field_email(self, value):
#         self.driver.find_element(*self.EMAIL).send_keys(value)
#
#     def text_field_password(self, value):
#         self.driver.find_element(*self.PASSWORD).send_keys(value)
#
#     def text_field_phone(self, value):
#         self.driver.find_element(*self.PHONE_NUMBER).send_keys(value)
#
#     def gst_textfield(self, value):
#         self.driver.find_element(*self.GST).send_keys(value)
#
#     def gst_number_textfield(self, value):
#         self.driver.find_element(*self.GST_NUMBER).send_keys(value)
#
#     # ---------------- Dropdowns ----------------
#     def select_from_list(self, dropdown_placeholder, value_to_select):
#         try:
#             dropdown = WebDriverWait(self.driver, 10).until(
#                 EC.element_to_be_clickable(
#                     (By.XPATH, f"//div[contains(@class,'placeholder') and normalize-space(text())='{dropdown_placeholder}']")
#                 )
#             )
#             dropdown.click()
#
#             list_items = WebDriverWait(self.driver, 10).until(
#                 EC.presence_of_all_elements_located((By.XPATH, "//li[contains(@class,'ng-star-inserted')]"))
#             )
#
#             for item in list_items:
#                 if item.text.strip().lower() == value_to_select.lower():
#                     ActionChains(self.driver).move_to_element(item).click().perform()
#                     return
#         except Exception as e:
#             print(f"❌ Error selecting '{value_to_select}': {e}")
#
#     def country_dropdown(self, country_name):
#         self.select_from_list("Select a Country", country_name)
#
#     def state_dropdown(self, state_name):
#         self.select_from_list("Select a State / Provinces", state_name)
#
#     def city_dropdown(self, city_name):
#         self.select_from_list("Select a City", city_name)
#
#     def select_service_city_dropdown(self, value):
#         try:
#             self.driver.find_element(*self.SERVICE_CITY).click()
#             time.sleep(0.5)
#
#             search_box = self.driver.find_element(By.XPATH, "//input[@placeholder='Search']")
#             search_box.clear()
#             search_box.send_keys(value)
#             time.sleep(1)
#
#             option_xpath = f"//li[contains(@class,'multiselect-item-checkbox') and contains(translate(.,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'{value.lower()}')]"
#             option_li = WebDriverWait(self.driver, 10).until(
#                 EC.presence_of_element_located((By.XPATH, option_xpath))
#             )
#             option_div = option_li.find_element(By.XPATH, ".//div")
#             ActionChains(self.driver).move_to_element(option_div).click().perform()
#             time.sleep(0.5)
#         except Exception as e:
#             print(f"❌ Could not select service city '{value}': {e}")
#
#     def select_company_type(self, value):
#         try:
#             select = Select(self.driver.find_element(*self.COMPANY_TYPE))
#             select.select_by_visible_text(value)
#             time.sleep(0.5)
#         except Exception as e:
#             print(f"❌ Could not select company type '{value}': {e}")
#
#     # ---------------- Commissions ----------------
#     def company_trip_comm(self):
#         self.driver.find_element(*self.TRIP_COMM).click()
#
#     def trip_comm_rate(self, value):
#         self.driver.find_element(*self.FLAT_RATE).send_keys(value)
#
#     def company_sub_comm(self):
#         self.driver.find_element(*self.SUB_COMM).click()
#
#     def comm_per_rate(self, value):
#         self.driver.find_element(*self.SUB_COMM_PER).send_keys(value)
#
#     # ---------------- Submit ----------------
#     def company_sub_button(self):
#         self.driver.find_element(*self.SUBMIT).click()


import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.BasePage import BasePage


class Add_Company(BasePage):
    # Locators
    COMPANY_MODULE = (By.XPATH, "//span[text()='Company']")
    ADD_COMPANY = (By.XPATH, "//span[text()='Add Company']")
    COMPANY_NAME = (By.NAME, "name")
    EMAIL = (By.NAME, "email")
    PASSWORD = (By.NAME, "pwd")
    PHONE_NUMBER = (By.NAME, "phone")
    GST = (By.NAME, "vat")
    GST_NUMBER = (By.NAME, "vatNumber")
    SERVICE_CITY = (By.NAME, "scIds")
    COMPANY_TYPE = (By.NAME, "companyType")
    TRIP_COMM = (By.XPATH, "(//span[contains(text(),'Flat')])[1]")
    FLAT_RATE = (By.XPATH, "//input[@placeholder='Rate']")
    SUB_COMM = (By.XPATH, "(//span[contains(text(),'Percentage')])[2]")
    SUB_COMM_PER = (By.XPATH, "(//input[@name='rate1'])[1]")
    SUBMIT = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        super().__init__(driver)

    def company_module(self):
        self.do_click(self.COMPANY_MODULE)

    def add_company_module(self):
        self.do_click(self.ADD_COMPANY)

    def text_field_company_name(self, value):
        self.do_send_keys(self.COMPANY_NAME, value)

    def text_field_email(self, value):
        self.do_send_keys(self.EMAIL, value)

    def text_field_password(self, value):
        self.do_send_keys(self.PASSWORD, value)

    def text_field_phone(self, value):
        self.do_send_keys(self.PHONE_NUMBER, value)

    def gst_textfield(self, value):
        self.do_send_keys(self.GST, value)

    def gst_number_textfield(self, value):
        self.do_send_keys(self.GST_NUMBER, value)

    def select_from_list(self, dropdown_placeholder, value_to_select):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//div[contains(@class,'placeholder') and normalize-space(text())='{dropdown_placeholder}']")
            )
        )
        dropdown.click()

        list_items = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//li[contains(@class,'ng-star-inserted')]"))
        )

        for item in list_items:
            if item.text.strip().lower() == value_to_select.lower():
                ActionChains(self.driver).move_to_element(item).click().perform()
                return

    def country_dropdown(self, country_name):
        self.select_from_list("Select a Country", country_name)

    def state_dropdown(self, state_name):
        self.select_from_list("Select a State / Provinces", state_name)

    def city_dropdown(self, city_name):
        self.select_from_list("Select a City", city_name)

    def select_service_city_dropdown(self, value):
        self.driver.find_element(*self.SERVICE_CITY).click()
        time.sleep(0.5)

        search_box = self.driver.find_element(By.XPATH, "//input[@placeholder='Search']")
        search_box.clear()
        search_box.send_keys(value)
        time.sleep(1)

        option_xpath = f"//li[contains(@class,'multiselect-item-checkbox') and contains(translate(.,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'{value.lower()}')]"
        option_li = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, option_xpath))
        )
        option_div = option_li.find_element(By.XPATH, ".//div")
        ActionChains(self.driver).move_to_element(option_div).click().perform()
        time.sleep(0.5)

    def select_company_type(self, value):
        select = Select(self.driver.find_element(*self.COMPANY_TYPE))
        select.select_by_visible_text(value)
        time.sleep(0.5)

    def company_trip_comm(self):
        self.do_click(self.TRIP_COMM)

    def trip_comm_rate(self, value):
        self.do_send_keys(self.FLAT_RATE, value)

    def company_sub_comm(self):
        self.do_click(self.SUB_COMM)

    def comm_per_rate(self, value):
        self.do_send_keys(self.SUB_COMM_PER, value)

    def company_sub_button(self):
        self.do_click(self.SUBMIT)