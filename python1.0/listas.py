tu_du =["dirigirnso al hotel","quiero ir a almorzar",
       "visitar un museo","volver al hotel"]
print(tu_du)
numbers = [1,2,3,4,"cinco"]
print(type(numbers))
mix = ["uno",1,2,3.14,True,[1,2,3]]
print(mix)
print(len(mix))
print("primer elemento",mix[0])
print("segundo elemento",mix[2])
print(" elemento",mix[-1])
string = "hola munedo"
print("primer elemento",string[0])
print("segundo elemento",string[1])
print("tercer elemento",string[-1])
print(mix[0:2])
print(mix)
mix.append(False)
print(mix)
mix.append(["a","b"])
print(mix)
mix.insert(1,["a","b"])
print(mix)
print(mix.index(["a","b"]))
numbers = [1,2,100,90,45,3,4,5]
print(numbers)
print("mayor",max(numbers))
print("menor",min(numbers))
del numbers[-1]
print(numbers)
del numbers[:2]
print(numbers)

