import pandas

def get_cities():

    # df = pandas.read_csv('kz.csv')
    df = pandas.read_csv('main_cities.csv')

    columns = [
        'city',
        'lat',
        'lng'
    ]

    city_id = 0
    cities = []

    while True:
        city = {
            'name': '',
            'lat': None,
            'lng': None,
        }
        city['name'] = df[columns[0]][city_id]
        city['lat'] = df[columns[1]][city_id]
        city['lng'] = df[columns[2]][city_id]

        city_id += 1
        if( city_id >= len (df[columns[0]] ) ):
            break

        cities.append(city)

    return cities

# print(get_cities())