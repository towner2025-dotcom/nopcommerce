# from base_packages.login_admin_page import Login_Admin_Page
# from utilites.custom_logger import Log_Maker
# from utilites.read_properties import Read_Config
# from base_packages.add_rider import Add_Rider_Details
# # import os
# # import json
# # import random
# # import string
# # import secrets
# # import datetime
# # import uuid
#
#
# class Test_03_Add_Rider:
#     admin_page_url = Read_Config.get_admin_page_url()
#     username = Read_Config.get_user_name()
#     password12 = Read_Config.get_user_password()
#     logger=Log_Maker.log_gen()
#
#     def test_add_rider(self,setup):
#         # name, email, phone, password = self.generate_random_user()
#         self.driver=setup
#         self.driver.implicitly_wait(20)
#         self.driver.get(self.admin_page_url)
#         self.admin_login = Login_Admin_Page(self.driver)
#         self.admin_login.enter_username(self.username)
#         self.admin_login.enter_password(self.password12)
#         self.admin_login.click_login()
#
#         self.logger.info(">>>>>Login Completed<<<<<")
#
#         self.logger.info(">>>>>Start Adding the Rider<<<<<")
#         self.add_rider=Add_Rider_Details(self.driver)
#         self.add_rider.rider_module()
#         self.add_rider.add_rider_module()
#         self.add_rider.text_field_fname("sdhfdfs")
#         self.add_rider.text_field_lname("fuidg")
#         self.add_rider.text_field_email("uisdfnuisd@sdhfn.ujsdhf")
#         self.add_rider.text_field_phonenumber(1234567765)
#         self.add_rider.text_field_password("Abbas@123")
#         self.add_rider.select_gender("Male")
#         # self.add_rider.country_dropdown("India")
#         # self.add_rider.state_dropdown("Karnataka")
#         # self.add_rider.city_dropdown("Bangalore")
#         self.add_rider.select_servicecity("Bangalore")
#         self.add_rider.add_button()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#     #
#     #
#     # def generate_random_user(self):
#     #     if os.path.exists("user_data.txt"):
#     #         with open("user_data.txt", "r") as f:
#     #             data = f.read().strip().split(",")
#     #             name, email, phone, password = data
#     #             return name, email, phone, password
#     #
#     #     # Generate random name
#     #     letters = "abcdefghijklmnopqrstuvwxyz"
#     #     name = "".join(random.choice(letters) for _ in range(random.randint(5, 8))).capitalize()
#     #
#     #     # Generate email
#     #     domains = ["gmail.com", "yahoo.com", "outlook.com", "example.com"]
#     #     email = name.lower() + str(random.randint(10, 99)) + "@" + random.choice(domains)
#     #
#     #     # Generate phone number
#     #     phone = str(random.randint(6000000000, 9999999999))
#     #
#     #     # Generate valid password
#     #     uppercase = random.choice(string.ascii_uppercase)
#     #     lowercase = random.choice(string.ascii_lowercase)
#     #     digit = random.choice(string.digits)
#     #     special = random.choice("!@#$%^&*()_+-=[]{}|;:,.<>?")
#     #     remaining = "".join(
#     #         random.choice(string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?") for _ in range(4))
#     #     password_list = list(uppercase + lowercase + digit + special + remaining)
#     #     random.shuffle(password_list)
#     #     password = "".join(password_list)
#     #
#     #     # Save all data for reuse
#     #     with open("user_data.txt", "w") as f:
#     #         f.write(f"{name},{email},{phone},{password}")
#     #
#     #     return name, email, phone, password
#     # # Example usage
#     # name, email, phone = generate_random_user()
#     # print("Name :", name)
#     # print("Email:", email)
#     # print("Phone:", phone)
#
#
#
#
#
#
#
#
#
