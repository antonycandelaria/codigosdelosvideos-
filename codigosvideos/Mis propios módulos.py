"""
def get_population():
  keys = ['col', 'bol']
  values = [300, 400]
  return keys, values

def population_by_country(data, country):
  result = list(filter(lambda item: item['Country'] == country, data))
  return result
"""
import utils

keys, values = utils.get_population()
print(keys, values)

data = [
  {
    'Country': 'Colombia',
    'Population': 500
  },
  {
    'Country': 'Bolivia',
    'Population': 300
  }
]

country = input('Type Country => ')

result = utils.population_by_country(data, country)
print(result)