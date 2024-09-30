#AntonyCandelaria
countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}
#usando el metodo 
new_set = countries.union(northAm,centralAm,southAm)
print(new_set)
# usando el operador 
print (countries |northAm | centralAm |southAm)
