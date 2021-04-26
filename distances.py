from geopy.distance import geodesic

coords_1 = (43.2500, 76.9000)
coords_2 = (51.1333, 71.4333)

print (geodesic(coords_1, coords_2).km)