import random

passlen = int(input("enter the length of password: "))
s = "qwertyuiopasdfghjklzxcvbnm0123456789QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()?"
p = "".join(random.sample(s, passlen))
print(p)
