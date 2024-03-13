import random 
from werkzeug.security import generate_password_hash

    
def generatePass():
    
    #SAMPLE 
    """
    minus = "abcdefghijklmnopqrstuvwyxz"
    long =  12
    muestra = random.sample(minus, long)
    print(muestra) """


    minus = "abcdefghijklmnopqrstuvwyxz"
    mayus = minus.upper()
    num = "1234567890"
    long =  12
    Simbol = "`+ç´,.^*Ç;:_!·$%&/"

    base = minus + mayus + num + Simbol

    for i in range (5):

        muestra = random.sample(base, long)
        password = "".join(muestra)             
        password_encriptado = generate_password_hash(password)

        print("{} => {}".format(password, password_encriptado))

generatePass()


# BUT...... The Random Module in Python: Is It Secure Enough?

"""
    Random Module => pseudorandom. Never use in Security.
    The term pseudorandom means that although the sequence may appear random, it is actually deterministic.

import random           --Choose between 3 options:

papers = ['A','B','C']

for i in range (10):
    q_list=random.choice(papers)
    print (q_list, end='')

For statistical simulations, you can use the random module; for sensitive applications, use the secrets module.

"""


import secrets
import string

def GeneratePass2():

    letters = string.ascii_letters    #minus and mayus (the variables from before)
    digits = string.digits             #num
    special_chars = string.punctuation    #Simbol

    base2 = letters + digits + special_chars
    long2 = 15
    passw = ""

    for i in range(long2):
        passw += ''.join(secrets.choice(base2))

    print(passw)

GeneratePass2()
