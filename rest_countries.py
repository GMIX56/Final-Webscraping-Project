# Below is an api endpoint to show you all countries that speak spanish. Dive into the data and answer the following
# questions:

# 1) Display the common name, currency symbol, population and timezone of each country that is NOT landlocked and is in
# the South American continent.

# 2) using the latitude and longitude of the data from the query above, diplay the country information on a world map (using code below)


import requests
import json
import webbrowser


url = 'https://restcountries.com/v3.1/lang/spanish'

# make the call to the API
r = requests.get(url)

#create an output file so you can see the json response that was returned by the API call
file = open('api.json', 'w')
json.dump(r.json(), file, indent=3)
file.close()


print(f"status code: {r.status_code}") 


# Create a list of country names, longitudes, latitudes and population for all countries.
# NOTE: It is important to use these names for the map to work correctly.
names = []
lons = []
lats = []
population = []

# populate this list with the data from the api call using a loop and print out information
# per requirements in 1)
if r.status_code == 200:
    data = r.json()
    
    for country in data:
        if country['subregion'] == 'South America':
            if 'landlocked' in country and not country['landlocked']:
                names.append(country['name']['common'])
                lons.append(country['latlng'][1])
                lats.append(country['latlng'][0])
                population.append(country['population'])
                currency = country['currencies'][list(country['currencies'].keys())[0]].get('symbol')
                
                print(f"Country Name: {country['name']['common']}")
                print(f"Currency: {currency}")
                print(f"Population: {country['population']}")
                print(f"Timezone: {country['timezones'][0]}")
                print()
                print()

                
#Plotly World Map (NOTE: NO CODING NEEDED HERE!)

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text':names,
    'marker':{
        'size':[p/3_000_000 for p in population],
        'color':population,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Population'}
    },
}]

my_layout = Layout(title='South American Countries that are not landlocked')

fig = {'data':data, 'layout':my_layout}

offline.plot(fig,filename='south_america.html')

webbrowser.open('south_america.html')