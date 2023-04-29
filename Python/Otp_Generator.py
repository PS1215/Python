import random
digits = "0123456789"
OTP = ""
for i in range(6):
    OTP += random.choice(digits)
print("Your OTP is:", OTP)
