from geopy.distance import geodesic
import cities

def get_distances():
    Cities = cities.get_cities()
    distances = {}

    for city in Cities:
        city_name = city['name']
        distances[city_name] = []
        for city2 in Cities:

            coords_1 = (city['lat'], city['lng'])
            coords_2 = (city2['lat'], city2['lng'])

            # print( city['name'], ' < - > ', city2['name'], end = ' Distance = ' )
            distance = geodesic(coords_1, coords_2).km

            if( distance == 0 ):
                continue

            distances[city_name].append(
                {
                    city2['name'] : distance
                }
            )
            
    return distances

# print(get_distances()['Almaty'][0: 2])