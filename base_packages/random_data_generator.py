import random
import string
import json

class RandomDataGenerator:
    def __init__(self):
        self.data_store = {}

    def random_string(self, length=6):
        return ''.join(random.choices(string.ascii_letters, k=length))

    def random_email(self):
        return f"{self.random_string(5)}@{self.random_string(3)}.com"

    def random_phone(self):
        return ''.join(random.choices(string.digits, k=10))

    def random_password(self):
        # Example: 1 uppercase, 1 lowercase, 1 digit, 1 special char
        letters = string.ascii_letters
        digits = string.digits
        special = "@#$%&!"
        password = (
            random.choice(string.ascii_uppercase) +
            random.choice(string.ascii_lowercase) +
            random.choice(digits) +
            random.choice(special) +
            ''.join(random.choices(letters + digits, k=4))
        )
        return password

    def random_gst_number(self):
        # GSTIN format: 15 characters
        # 1-2: State code (01-37)
        state_code = str(random.randint(1, 37)).zfill(2)

        # 3-12: PAN format: 5 letters + 4 digits + 1 letter
        pan = ''.join(random.choices(string.ascii_uppercase, k=5)) + \
              ''.join(random.choices(string.digits, k=4)) + \
              random.choice(string.ascii_uppercase)

        # 13th: Entity code (alphanumeric)
        entity = random.choice(string.ascii_uppercase + string.digits)

        # 14th: Default Z
        default_z = 'Z'

        # 15th: Checksum (alphanumeric)
        checksum = random.choice(string.ascii_uppercase + string.digits)

        return f"{state_code}{pan}{entity}{default_z}{checksum}"

    def generate_company_data(self):
        self.data_store = {
            "company_name": self.random_string(7),
            "email": self.random_email(),
            "password": self.random_password(),
            "phone": self.random_phone(),
            "gst_text": str(random.randint(10, 99)),
            "gst_number": self.random_gst_number()
        }
        # Optional: save to a file for later reuse
        with open("company_data.json", "w") as f:
            json.dump(self.data_store, f, indent=4)
        return self.data_store

    def load_company_data(self):
        # Load previously stored data
        with open("company_data.json", "r") as f:
            self.data_store = json.load(f)
        return self.data_store
