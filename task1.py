def most_wanted_letter(s:str):
    s =  s.lower().translate(str.maketrans('', '', '.;:!?-–+=()[]{}«"/\|1234567890+-*÷=><%^#№@$&~`'))
    if s == '':
        return 'There are no letters in the string.'
    else:
        letters = [x for x in s if x.isalpha()]
        max_count = 0
        for letter in set(letters):
            count = letters.count(letter)
            if count > max_count:
                max_count = count
                result = (letter, max_count)

        return 'The most popular letter is ' + result[0]

print(most_wanted_letter("......HeLlo......"))
print(most_wanted_letter("String ssss ttAAds TTTTTTT"))
print(most_wanted_letter("!@#$%^&*(*&^%$#@@#$%^&*DFGBQQQQQQQQqqqrrrrrrrr"))
print(most_wanted_letter("!@#$%^&*543234%^&*%$#@345677^%$#@#$%^&"))
print(most_wanted_letter("....пррррривет..."))
print(most_wanted_letter("....Tschüüüüüüüss!..."))