def filter_by_length(words):
   # Escribe tu solución 👇
   return list(filter(lambda numLetters: len(numLetters) >= 4, words))

words = ['carro', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)