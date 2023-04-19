import random
import string

def generate_password(length):
    # define the possible characters that can be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # generate a random password by choosing characters randomly from the above list
    password = ''.join(random.choice(characters) for i in range(length))

    return password

# call the generate_password function with a desired length for the password
password = generate_password(12)
print(password)