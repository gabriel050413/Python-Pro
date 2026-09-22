import random
password = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
passnum = int(input("quantos caracteres tem sua senha"))
passaa = ""
for i in range(passnum):
    passaa += random.choice(password)
print("sua senha é", passaa)
