import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
import math
from random import uniform
from time import sleep

"""VERSI CONSOLE"""

def pi(n):
    x = 0

    for i in range(1,n):
        x += 1/(i**2)

    return (6*x)**0.5

# print("nilai pi: ",pi(100000000))
# print("π = ",math.pi)

"""ANIMASI"""

kec = 10000 #Iterasi/frame 
iterasi = 100000

plt.style.use("ggplot")
plt.xkcd()


x = []
y = []

fig, (ax1,ax2) = plt.subplots(nrows=2)
ax2.remove()



k = 0

def gen():
    global k
    i=0
    while k<= iterasi:
        i += 1
        yield i

def animate(i):
    global k


    x.append(k)
    y.append(pi(k))



    ax1.cla()

    ax1.set_title("Pendekatan π dengan Deret Euler")
    ax1.text(0.2*k,-3,f"Nilai pi = {pi(k)}")
    ax1.text(0.2*k,-2,f"π = {math.pi} ")
    ax1.text(0.2*k,-4,f"Iterasi = {k} ")
    ax1.text(0,-6,"Created by: M Hatta Hakim",size=8)
    ax1.text(0,-6.5,"follow : @labhatta",size=8)

    plt.xlim([0,k])
    plt.ylim([0,5])

    ax1.plot(x,y)

    k += kec

ani = FuncAnimation(fig,animate,frames=gen,repeat=False,interval=10)

plt.show()
