import string
import random
import schedule
import time

def generate_password():
    characters = string.printable.replace(' ', '').replace('\t', '').replace('\n', '').replace('\r', '')
    length = 14
    password_string = ''.join(random.choice(characters) for _ in range(length))
    return password_string

def print_password():
    generated_password = generate_password()
    print(generated_password)

# No uses paréntesis al pasar la función a do()
schedule.every(10).seconds.do(print_password)

while True:
    schedule.run_pending()
    time.sleep(1)
