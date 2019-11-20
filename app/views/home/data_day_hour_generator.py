from random import randint, random
from numpy import random as aleatorio
from math import log
from math import e as euler
print(euler)

lnormal = aleatorio.lognormal


for k in range(1, 11):
	with open(f"data{k}.csv", "w", encoding="utf-8") as file:
		file.write("coord_x,coord_y,value,water_saturation,confidence\n")
		dict_valores = {}
		for i in range(1, 31):
			dict_valores[i] = {}
			for j in range(1, 101):
				ran_1 = str(random())[0:3]
				ran_2 = str(random())[0:3]
				if i <=2 :
					promedio = log(4)
					#if j == 1:
					#	promedio = euler^4
					#else:
					#	promedio = (4 + log(dict_valores[i][j-1])/2
				else:
					if j <= 2:
						promedio = log(4)
						#promedio = (log(dict_valores[i-1][j] + 4)/2
					else:
						promedio = (log(dict_valores[i-1][j]) + log(dict_valores[i-2][j]) 
							 + log(dict_valores[i][j-1]) + log(dict_valores[i-1][j-1]) 
							 + log(dict_valores[i-2][j-1]) + log(dict_valores[i][j-2]) 
							 + log(dict_valores[i-1][j-2]) + log(dict_valores[i-2][j-2])
							)/8


				
				valor = lnormal(mean=(promedio), sigma=1)
				
				dict_valores[i][j] = valor
				j_ = j-(i-1)
				if j_ < 1:
					j_ += 100
				delta = + (j_/20)
				print(delta)
				text = f"{i},{j_},{str((valor +1) * delta)},{ran_1},{ran_2}\n"
				file.write(text)


dias = [str(i) for i in range(1, 31)]
tiempos = [str(i) for i in range(1, 101) if i % 2 == 0]

print(dias)
print(tiempos)