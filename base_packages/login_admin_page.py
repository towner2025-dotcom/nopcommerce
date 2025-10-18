from selenium.webdriver.common.by import By

class Login_Admin_Page:
    testBox_UserName_id = "input-email"
    testBox_Password_id = "input-password"
    button_login_Xpath = "//button[normalize-space()='Log In']"
    profile_xpath="//div[@class='user-container']"
    logout_xpath = "//span[normalize-space()='Log out']"
    #  https://rahulshettyacademy.com/client/#/dashboard/dash
    #  https://demoapps.qspiders.com/ui/ecommerce?sublist=0&scenario=1

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.testBox_UserName_id).clear()
        self.driver.find_element(By.ID, self.testBox_UserName_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.testBox_Password_id).clear()
        self.driver.find_element(By.ID, self.testBox_Password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.button_login_Xpath).click()

    def logout(self):
        self.driver.find_element(By.XPATH,self.profile_xpath).click()
        self.driver.find_element(By.XPATH, self.logout_xpath).click()

