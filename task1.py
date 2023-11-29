import collections
import re

def most_wanted_letter(s:str):
    if s == '':
        return 'String is empty'
    else:
        s = re.sub(r'[^\w\s]', '', s)
        return 'The most popular letter is ' + collections.Counter(s.lower()).most_common(1)[0][0]

print(most_wanted_letter('...............Hellllllllo............'))