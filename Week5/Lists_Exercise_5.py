def add_vectors(vector1, vector2):
    vector = []
    for i in range(len(vector1)):
        vector.append(vector1[i] + vector2[i])
    return vector


print(add_vectors([1, 1], [1, 1]) == [2, 2])
print(add_vectors([1, 2], [1, 4]) == [2, 6])
print(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])


# voor i in lengte 2

# i = 0

# vector toevoegen 1 + 1 = 2
# vector wordt [2]

# i = 1
# vector toevoegen 1 + 1 = 2
# vector wordt [2, 2]
