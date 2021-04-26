from geopy.distance import geodesic
import cities

def get_distances():
    Cities = cities.get_cities()
    distances = {}

    city_id = 0

    for city in Cities:
        city_name = city['name']
        distances[city_name] = []
        city2_id = 0

        for city2 in Cities:

            coords_1 = (city['lat'], city['lng'])
            coords_2 = (city2['lat'], city2['lng'])

            # print( city['name'], ' < - > ', city2['name'], end = ' Distance = ' )
            distance = geodesic(coords_1, coords_2).km

            if( distance == 0 ):
                city2_id += 1
                continue

            distances[city_name].append(
                {
                    'start_id': city_id,
                    'end_id': city2_id,
                    'end_name' : city2['name'],
                    'distance' : distance
                }
            )
            city2_id += 1

        city_id += 1
    return distances

# print(get_distances()['Almaty'][0:4])