#Write your code below this line 👇
import math


def prime_checker(number):
    count = 0
    mid = math.ceil(number / 2)
    for i in range(2, mid):
        if number % i == 0:
            count += 1
    if count >= 1:
        print(f"{number} is not prime!")
    else:
        print(f"{number} is prime!")


#Write your code above this line 👆

#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
