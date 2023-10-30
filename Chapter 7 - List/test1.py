
cities = ("Chicago", "Aurora", "Joliet", "Rockford", "Naperville", "Elgin")
population = (2745, 204, 152, 150, 147, 116)
demographics = {cities[i]: population[i] for i in range(len(cities)) }

print(demographics)