import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
import math
from random import uniform
from time import sleep

# Variabel Untuk Menyimpan banyak titik
diLingkaran = 0 # banyaknya titik didalam lingkaran
diLuar = 0 # banyaknya titik diluar lingkaran

""" Algoritma dasar """

def pi1(n):
    global diLingkaran,diLuar

    for i in range(n):
        x = uniform(0,1) # Buat Nilai random dari rentang 0 sampai 1
        y = uniform(0,1) # Buat Nilai random dari rentang 0 sampai 1

        if (x**2 + y**2)**0.5 < 1: # jika titik didalam lingkaran
            diLingkaran +=1

        else: # jika diluar lingkaran
            diLuar +=1

    print("pi = ",4*diLingkaran/(diLuar+diLingkaran))


""" Animasi """

besarTitik = 10 # mengatur besar titik
k = 0 # var untuk mengambil koordinat x dan y titik

# Set kecepatan & banyak titik
kec = 100
banyakTitik= 1000

# List Untuk Menyimpan titik
titik = []
xLingkaran = []
yLingkaran = []
xLuar = []
yLuar = []

def main():
    # Fungsi Untuk Membuat koordinat titik
    def bikinTitik(n):
        for i in range(n):
            x = uniform(0,1) # ambil sembarang bil dari rentang 0 sampai 1
            y = uniform(0,1)
            titik.append((x,y))

    bikinTitik(banyakTitik)

    # Fungsi Untuk Animasi
    def pi(i):
        global diLingkaran,diLuar,xLingkaran,xLuar,yLingkaran,yLuar,k,diPersegi

        try:

            for i in range(kec):

                x = titik[k][0]
                y = titik[k][1]

                if (x**2 + y**2)**0.5 < 1 :
                    diLingkaran += 1
                    xLingkaran.append(x)
                    yLingkaran.append(y)

                else:
                    diLuar += 1
                    xLuar.append(x)
                    yLuar.append(y)

                k += 1 # pindah ke titik selanjutnya

            diPersegi = diLuar + diLingkaran

            plt.cla() # bersihkan plot

            plt.text(0.3,1.1,"Menentukan Nilai π Dengan Fungsi Random")
            plt.scatter(xLingkaran,yLingkaran,s=besarTitik) # buat titik titik didalam lingkaran
            plt.scatter(xLuar,yLuar,s=besarTitik) # buat titik titik diluar lingkaran

            if diPersegi != 0:
                plt.text(1.1,0.5,f" Nilai PI = {round(4*diLingkaran/diPersegi,10)}")

            plt.text(1.1,0.65,f" π = {math.pi}...")
            plt.text(1.1,0.35,f" Jumlah Titik = {diPersegi}")
            plt.text(0,-.3,"Created by: M Hatta Hakim",size=8)
            plt.text(0,-.4,"follow : @labhatta",size=8,alpha=1)

            plt.xlim([0,1]) # nilai koordinat x dari 0 sampe 1
            plt.ylim([0,1])

            plt.xticks([0,0.5,1]) # membuat nilai nilai pada koordinat x
            plt.yticks([0,0.5,1])

        except Exception as e:
            None



    plt.style.use("ggplot")
    plt.xkcd()


    plt.subplots_adjust(right=0.5,bottom=0.3,top=0.75)

    ani = FuncAnimation(plt.gcf(),pi,interval=1)


    plt.show()

main()

def pi1(n):
    global diLingkaran,diLuar

    for i in range(n):
        x = uniform(0,1) # Buat Nilai random dari rentang 0 sampai 1
        y = uniform(0,1) # Buat Nilai random dari rentang 0 sampai 1

        if (x**2 + y**2)**0.5 < 1: # jika titik didalam lingkaran
            diLingkaran +=1

        else: # jika diluar lingkaran
            diLuar +=1

    print("pi = ",4*diLingkaran/(diLuar+diLingkaran))
