import random


# work with this variable
n = int(input())
text = "Voldemort"
random.seed(n)
print(random.choice(text))
