import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Add_Rider_Details:

    riderModule_Xpath="//span[text()='Rider']"
    addRiderModule_Xpath = "//span[text()='Add  Rider']"
    riderFName_name="fname"
    riderLName_name = "lname"
    riderEmail_name = "email"
    riderPhoneNumber_name = "phone"
    riderPassword_name = "password"
    riderGender1_Xpath = "//span[text()='Male']"
    riderGender2_Xpath = "//span[text()='Female']"
    dropDownData_Xpath="(//div[@class='below form-control'])"

    riderCountry_Xpath="ng-select[placeholder='Select a Country'] div[class='below form-control']"
    riderState_Xpath="//ng-select[@placeholder='Select a State / Provinces']//div[@class='below form-control']"
    riderCity_Xpath="//ng-select[@placeholder='Select a City']//div[@class='below form-control']"
    riderServiCecity_name="scIds"
    riderAddButton_Xpaath="//button[text()='Add']"


    def __init__(self, driver):
        self.driver = driver

    def rider_module(self):
        self.driver.find_element(By.XPATH, self.riderModule_Xpath).click()
    def add_rider_module(self):
        self.driver.find_element(By.XPATH, self.addRiderModule_Xpath).click()


    def text_field_fname(self,fname):
        self.driver.find_element(By.NAME, self.riderFName_name).send_keys(fname)
    def text_field_lname(self, lname):
        self.driver.find_element(By.NAME, self.riderLName_name).send_keys(lname)

    def text_field_email(self, email):
            self.driver.find_element(By.NAME, self.riderEmail_name).send_keys(email)

    def text_field_password(self, password):
                self.driver.find_element(By.NAME, self.riderPassword_name).send_keys(password)

    def text_field_phonenumber(self, phonenumber):
            self.driver.find_element(By.NAME, self.riderPhoneNumber_name).send_keys(phonenumber)

    def select_gender(self, gender):
        """Click the matching gender radio button."""
        gender = gender.lower()
        try:
            if gender == "male":
                element = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.riderGender1_Xpath))
                )
                element.click()
            elif gender == "female":
                element = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.riderGender2_Xpath))
                )
                element.click()
            else:
                raise ValueError(f"Invalid gender: {gender}. Use 'Male' or 'Female'.")
        except Exception as e:
            print(f"Failed to select gender '{gender}': {e}")

    def select_from_dropdown(self, index, value, placeholder_text):
        dropdown_field = self.driver.find_elements(By.XPATH, self.dropDownData_Xpath)[index]
        dropdown_field.click()
        time.sleep(1)  # slight delay for the input to appear

        # Find input field
        input_xpath = f"//input[@placeholder='{placeholder_text}']"
        search_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, input_xpath))
        )
        search_input.clear()
        search_input.send_keys(value)
        time.sleep(1)

        # Wait for the list item to appear (case-insensitive)
        option_xpath = f"//li[contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'{value.lower()}')]"
        option_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, option_xpath))
        )
        option_element.click()
        time.sleep(0.5)

        # Convenience wrappers

    def country_dropdown(self, value):
        self.select_from_dropdown(0, value, "Type to Search a Country")

    def state_dropdown(self, value):
        self.select_from_dropdown(1, value, "Type to Search a State / Provinces")

    def city_dropdown(self, value):
        self.select_from_dropdown(2, value, "Type to Search a City")
    def select_servicecity(self, value):
        # 1. Click the service city dropdown to open it
        elements = self.driver.find_elements(By.NAME, self.riderServiCecity_name)
        if len(elements) < 3:
            raise Exception("Service city dropdown not found")
        dropdown_field = elements[2]
        dropdown_field.click()
        time.sleep(1)  # allow list to render

        # 2. Find the input/filter box inside the dropdown and type the value
        filter_input = self.driver.find_element(By.XPATH, "//li[@class='filter-textbox']//input")
        filter_input.clear()
        filter_input.send_keys(value)
        time.sleep(1)  # allow filtering

        # 3. Wait for the matching list items to appear
        option_xpath = f"//ul[@class='item2']/li[contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'{value.lower()}')]"
        options = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, option_xpath))
        )

        # 4. Scroll into view and click the first matching option
        if options:
            action = ActionChains(self.driver)
            action.move_to_element(options[0]).click().perform()
        else:
            raise Exception(f"No matching service city found for '{value}'")
        time.sleep(0.5)

    def add_button(self):
        self.driver.find_element(By.ID, self.riderAddButton_Xpaath).click()






