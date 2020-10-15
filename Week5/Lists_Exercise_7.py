def dot_product(vec1, vec2):
    product = 0
    for i in range(len(vec1)):
        product += vec1[i] * vec2[i]
    return product


print(dot_product([1, 1], [1, 1]) == 2)
print(dot_product([1, 2], [1, 4]) == 9)
print(dot_product([1, 2, 1], [1, 4, 3]) == 12)
