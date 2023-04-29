import random
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!@#$%^&*'
digits = '0123456789'
password = random.choice(alphabet) + random.choice(punctuation) + random.choice(digits)
for i in range(7):
    password += random.choice(alphabet + punctuation + digits)
print("Your secure password is:", password)

