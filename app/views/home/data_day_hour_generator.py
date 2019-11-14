from random import randint, random
from numpy import random as aleatorio
from math import log

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
				if i <=4 :
					promedio = 4
					#if j == 1:
					#	promedio = 4
					#else:
					#	promedio = (4 + dict_valores[i][j-1])/2
				else:
					if j <= 4:
						promedio = 4
						#promedio = (dict_valores[i-1][j] + 4)/2
					else:
						promedio = (dict_valores[i-1][j] + dict_valores[i-2][j] + 
							dict_valores[i-3][j] + dict_valores[i-4][j] + 
							dict_valores[i][j-1] + dict_valores[i-1][j-1] + 
							dict_valores[i-2][j-1] + dict_valores[i-3][j-1] + 
							dict_valores[i][j-2] + dict_valores[i-1][j-2] + 
							dict_valores[i-2][j-2] + dict_valores[i][j-3] + 
							dict_valores[i-1][j-3] + dict_valores[i][j-4])/14
				'''
				aux = 1
				while aux == 1:
					valor = lnormal(mean=promedio, sigma=5)
					if valor <= 60:
						aux = 0
					else:
						valor = 4 
						aux = 0
				'''
				print('promedio:', promedio)
				valor = lnormal(mean=promedio, sigma=1)
				print('valor:', valor)
				
				dict_valores[i][j] = valor
				text = f"{i},{j},{str(valor)[0:3]},{ran_1},{ran_2}\n"
				file.write(text)


dias = [str(i) for i in range(1, 31)]
tiempos = [str(i) for i in range(1, 101) if i % 2 == 0]

print(dias)
print(tiempos)