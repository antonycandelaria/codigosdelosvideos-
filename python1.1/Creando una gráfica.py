import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):
  #recibimos los elementos y usamos el  metodo 
  fig, ax = plt.subplots()
  #elementos
  ax.bar(labels, values)
  #renderisar
  plt.show()

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.show()

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [10, 40, 800]
  #generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)
