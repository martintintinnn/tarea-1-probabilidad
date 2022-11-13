import random
import matplotlib.pyplot as my_plt 
import numpy as np

#Debemos graficar las frecuencias, en que la suma son desde 10, hasta 60
#Analizar el grafico obtenido segun las esperanzas de cada valor

max_range = 10000
dice_throw = 10
example_list = []
number_list = []
relative_frequency_list = []
hope_list = []
xf = 0

for i in range(0,max_range):
    summation_number = 0

    for j in range(0,dice_throw):
        my_random_number = random.randint(1,6)
        summation_number += my_random_number

    #Agregamos el numero a la lista
    number_list.append(summation_number)

for i in range(10,61):
    hope_list.append(0.002)
    example_list.append(i)
    relative_frequency_list.append(number_list.count(i)/max_range)

my_plt.bar(example_list, relative_frequency_list, color="g", label="Experimental")
my_plt.title("Summation vs Frequency")
my_plt.xlabel("Sum_of_%d_dices" % (dice_throw))
my_plt.ylabel("Frequency")


#----------        SEGUNDA PARTE      ----------------
#Para calcular la probabilidad de la sumatoria entre 10 y 60 debemos contar todos los posibles casos
summatory_list = [0] * 100
summatory_probability = [0] * 100

#Creeamos una lista que nos ayudara a ver los posibles numeros de los 10 dados
dice_list= [1] * 10
summatory = sum(dice_list)

#Doble bucle hasta que llegemos a la maxima sumatoria posible
while summatory < 60:  
    summatory = sum(dice_list)
    summatory_list[summatory] += 1
    dice_list[0] += 1

    i = 0
    while i < 9:
        if dice_list[i] >= 7:
            dice_list[i+1] += 1
            dice_list[i] = 1 
        i += 1

#Ahora que ya contamos los casos, debemos sacar las probabilidades de cada caso
example_list = [0]*100
for i in range(0,51):
    example_list[i] = i+10
    summatory_probability [i] = summatory_list[i+10]  / sum(summatory_list)


my_plt.plot(example_list, summatory_probability, color="b", label="Theoretical")
my_plt.legend()
my_plt.draw
my_plt.show()




