import random
import string

def generate_password(length):

    # create the character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # combine all sets
    all_character = lower + upper + digits + symbols

    # tack one character from each set
    password = [
        random.choice(lower),    
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    # choice randomly character form all_character
    password += random.choices(all_character, k=length-4)

    # change the randomly location of all characters
    random.shuffle(password)
    str="".join(password)

    return str


if __name__=="__main__":
    length = int(input("Enter the desired length of the password: "))
    password = generate_password(length) # Call password generater function
    print("Generated password: ",password)

    
    # permistion save password or not
    save=input("do you save this passowrd on password.txt y/n: ")
    save = save.lower()
    if save=="y" :
        App_name=input("Enter the application name: ")
        user_name=input("Enter the user name: ")
        with open("password.txt","a") as file:
            text=f"""
Application name    : {App_name}
user_name           : {user_name}
password            : {password}
"""

            file.write(text)