import random
import string

def crack_password(password):
    attempts = 0
    while True:
        guess =''.join(random.choices(string.ascii_letters+string.digits, k=len(password)))
        attempts +=1
        if guess == password:
            return attempts
password = input("enter the password to crack:")
print("cracking password")
attempts = crack_password(password)
print(f"the password was cracked in {attempts} attempts")
