n = 10
a = 0
b = 1
f = [a]
for i in range(n):
    temp = a
    a = b
    b += temp
    f.append(a)
print("Fibonachi number for {} is {}".format(n,a))

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(len(f))
plt.bar(x, height=f)

import turtle

turtle.shape("turtle")
turtle.color("green")

for _ in range(4):
    turtle.forward(100)
    turtle.left(90)

