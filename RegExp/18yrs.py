import re
from datetime import datetime, timedelta


def validate_birthday(birthday):
    # Regular expression pattern to match the birthday format "dd.mm.yyyy"
    pattern = "^\d{2}\.\d{2}\.\d{4}$"

    # Check if the input birthday matches the pattern
    if re.match(pattern, birthday):
        # Try to parse the input birthday as a datetime object
        try:
            birthday_date = datetime.strptime(birthday, "%d.%m.%Y")
            # Check if the input birthday is 18 years or older
            if birthday_date <= (datetime.now() - timedelta(days=365.25 * 18)):
                # Return True if the input birthday represents someone who is 18 years old or older
                return True
            else:
                # Return False if the input birthday represents someone who is under 18 years old
                return False
        except ValueError:
            # Return False if the input birthday is not a valid date
            return False
    # Return False if the input birthday does not match the pattern
    return False


# Take birthday as input from the user
birthday = input("Enter your birthday in the format 'dd.mm.yyyy': ")

# Check if the input birthday is valid
if validate_birthday(birthday):
    # Display message if the input birthday is valid
    print("You are 18 years old or older.")
else:
    # Display message if the input birthday is not valid
    print("You are under 18 years old.")
