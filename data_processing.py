import csv, os
import copy

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

countries = []
with open(os.path.join(__location__, 'Countries.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        countries.append(dict(r))

class TableDB:
    def __init__(self):
        self.database = []

    def insert(self, table):
        self.database.append(table)

    def search(self, table_name):
        for table in self.database:
            if table.table_name == table_name:
                return table
        return None
    
class Table:
    def __init__(self, table_name, table):
        self.table_name = table_name
        self.table = table
    
    def join(self, other_table, common_key):
        joined_table = Table(self.table_name + '_joins_' + other_table.table_name, [])
        for item1 in self.table:
            for item2 in other_table.table:
                if item1[common_key] == item2[common_key]:
                    dict1 = copy.deepcopy(item1)
                    dict2 = copy.deepcopy(item2)
                    dict1.update(dict2)
                    joined_table.table.append(dict1)
        return joined_table
    
    def filter(self, condition):
        filtered_table = Table(self.table_name + '_filtered', [])
        for item1 in self.table:
            if condition(item1):
                filtered_table.table.append(item1)
        return filtered_table
    
    def aggregate(self, function, aggregation_key):
        temps = []
        for item1 in self.table:
            temps.append(float(item1[aggregation_key]))
        return function(temps)
    
    def select(self, attributes_list):
        temps = []
        for item1 in self.table:
            dict_temp = {}
            for key in item1:
                if key in attributes_list:
                    dict_temp[key] = item1[key]
            temps.append(dict_temp)
        return temps

    def __str__(self):
        return self.table_name + ':' + str(self.table)

db = TableDB()

cities_table = Table('Cities', cities)
countries_table = Table('Countries', countries)

db.insert(cities_table)
db.insert(countries_table)

joined_table = cities_table.join(countries_table, 'country')
eu_no_coastline_cities = joined_table.filter(lambda x: x['EU'] == 'yes' and x['coastline'] == 'no')
min_temp = eu_no_coastline_cities.aggregate(min, 'temperature')
max_temp = eu_no_coastline_cities.aggregate(max, 'temperature')

print(f"Min temperature for cities in the EU without coastlines: {min_temp}")
print(f"Max temperature for cities in the EU without coastlines: {max_temp}")

countries_with_cities = cities_table.select(['country', 'latitude'])

country_latitudes = {}

for item in countries_with_cities:
    country = item['country']
    latitude = float(item['latitude'])
    if country not in country_latitudes:
        country_latitudes[country] = []
    country_latitudes[country].append(latitude)

for country, latitudes in country_latitudes.items():
    min_lat = min(latitudes)
    max_lat = max(latitudes)
    print(f"{country}: Min latitude = {min_lat}, Max latitude = {max_lat}")