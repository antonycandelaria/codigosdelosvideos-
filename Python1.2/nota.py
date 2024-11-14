#ley de multiplicacion
#Un loop dentro de otro loop
def f(n):
	for i in range(n): #n pasos
		for j in range(n): #n pasos
		 print(i, j)

#O(n) * O(n) = O(n * n) = O(n**2), la funcion crece en O de n**2

'''def fibonacci(n):
	if n == 0 or n == 1:
		return 1
	#Obtenemos el resultado y los vamos imprimiendo acorde se van realizando las llamadas.
	resultado = fibonacci(n - 1) + fibonacci(n - 2)
	print(resultado)
	return resultado'''