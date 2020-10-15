def letter_count(s):
    s = s.lower()
    dic = {}
    for letter in s:
        if letter in dic:
            dic[letter] += 1
        else:
            dic[letter] = 1
    return dic


print(letter_count("ThiS is String with Upper and lower case Letters"))