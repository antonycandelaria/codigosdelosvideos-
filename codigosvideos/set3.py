#AntonyCandelaria
set_a = {'col','mex','bol'}
set_b = {'peru','bol'}
#union permite unir dos conjuntos diferentes (metodo)
set_c = set_a.union(set_b)
print(set_c)
# lo mismo solo usando un operador
print (set_a | set_b)

#intercercion permtie ves la intercecion de los dos conjuntos
set_c = set_a.intersection(set_b)
print(set_c)
#intercecion con operador
print(set_a & set_b)
#difference  permite saber la diferencia de los conjutos
set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b)#con operador

#symmetric_difference permite ver la diferenciasimetrica
set_c = set_a.symmetric_difference(set_b)
print(set_c)
print (set_a ^ set_b)