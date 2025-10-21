import random
import string
import json
import os


class RandomDataGenerator:

    def __init__(self):
        self.data_dir = os.path.join(os.getcwd(), "data")
        os.makedirs(self.data_dir, exist_ok=True)
        self.data_file = os.path.join(self.data_dir, "company_data.json")

    def generate_company_name(self, length=7):
        return ''.join(random.choices(string.ascii_letters, k=length))

    def generate_email(self):
        username = ''.join(random.choices(string.ascii_letters, k=5))
        domain = ''.join(random.choices(string.ascii_letters, k=3))
        return f"{username}@{domain}.com"

    def generate_password(self, length=8):
        if length < 8:
            length = 8

        password_chars = [
            random.choice(string.ascii_uppercase),  # Uppercase
            random.choice(string.ascii_lowercase),  # Lowercase
            random.choice(string.digits),  # Number
            random.choice("@")  # Special character
        ]

        remaining_length = length - 4
        all_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + "@"
        password_chars.extend(random.choices(all_chars, k=remaining_length))

        random.shuffle(password_chars)

        return ''.join(password_chars)

    def generate_phone(self):
        return ''.join([str(random.randint(0, 9)) for _ in range(10)])

    def generate_gst_text(self):
        return str(random.randint(18, 28))

    def generate_gst_number(self):
        digits_2 = ''.join([str(random.randint(0, 9)) for _ in range(2)])
        letters_5 = ''.join(random.choices(string.ascii_uppercase, k=5))
        digits_4 = ''.join([str(random.randint(0, 9)) for _ in range(4)])
        letter_1 = random.choice(string.ascii_uppercase)
        digit_1 = str(random.randint(0, 9))
        letter_2 = random.choice(string.ascii_uppercase)
        digit_2 = str(random.randint(0, 9))

        return f"{digits_2}{letters_5}{digits_4}{letter_1}{digit_1}{letter_2}{digit_2}"

    def generate_company_data(self):
        data = {
            "company_name": self.generate_company_name(),
            "email": self.generate_email(),
            "password": self.generate_password(),
            "phone": self.generate_phone(),
            "gst_text": self.generate_gst_text(),
            "gst_number": self.generate_gst_number()
        }

        # Save the generated data to file
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=4)

        return data

    def load_company_data(self):
        if not os.path.exists(self.data_file):
            raise FileNotFoundError(f"Company data file not found: {self.data_file}")

        with open(self.data_file, 'r') as f:
            data = json.load(f)

        return data

