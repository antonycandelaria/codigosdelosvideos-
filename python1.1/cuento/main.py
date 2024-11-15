import utils
#modullo para leer el csv
import read_csv
#modulo para graficar
import charts

def run():
  #selecion de los datos 
  data = read_csv.read_csv('cuento/data.csv')
  data = list(filter(lambda item : item['Continent'] == 'South America',data))
   #selecion del pais 
  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)
  '''
  country = input('Type Country => ')

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(labels, values)
  '''

if __name__ == '__main__':
  run()