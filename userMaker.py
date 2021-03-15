import random
import string
import itertools

pit = input("ka ta ch 7arf ven wan cheka ? : ")
h =int(input ("user chand pite bt ? : "))
for i in itertools.product (pit, repeat=h):
	print("".join(i))