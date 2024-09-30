#AntonyCandelaria
set_countries = {'col','mex','bol'}
#saber  cuantos elementos hay dentro de un conjunto
size = len(set_countries)
print (size)

#preguntar por un elemento en especifico
print ('col' in set_countries)
print ('pe' in set_countries)

# add permite agregar elementos al conjunto
set_countries.add('pe')
print(set_countries)

#update permite actualizar los elemetos de  un conjunto
set_countries.update({'ar','ecua','pe'})
print (set_countries)

#remove  permite elimnar un elemento a un conjunto
set_countries.remove('col')
print(set_countries)

set_countries.remove('ar')
set_countries.discard('arg')
print (set_countries)
set_countries.add('arg')
print(set_countries)
#clear limpia el conjunto
set_countries.clear()
print (set_countries)
print (len(set_countries))
