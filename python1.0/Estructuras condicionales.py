x = 5
if x > 5:
  print("X es mayor que 5 ")
  #print("adentro del if")
elif x == 5:
  print("x es igual que 5")
else:
  print("X es menor que 5 ")
print("afuera")

z = 15
y = 20

if z>10 and y>25:
    print("z es mayor que 10 y Y es mayor que 15")

if z>10 or y>25:
    print("z es mayor que 10 O Y es Mayor que 25")

if not z>10:
    print("z no es mayor que 10")

is_member = True
age = 11

if is_member:
    if age>=15:
        print("Tienes acceso ya que eres miembro y mayor o igual a 15 aÃ±os")
    else:
        print("No tienes acceso ya que eres miembro pero menor a 15 aÃ±os")
else:
    print("No eres miembro y NO TIENES ACCESO")