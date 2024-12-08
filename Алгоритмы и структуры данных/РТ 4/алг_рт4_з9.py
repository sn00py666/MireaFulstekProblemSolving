def dict_letters(string):
    itog = dict()
    for i in string:
        if itog.get(i) is None:
            itog[i] = 1
        else: itog[i] += 1
    return itog

print(dict_letters("aaabbv"))