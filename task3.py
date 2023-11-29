n = int(input('Write number of students: '))
journal = {}

for i in range(n):
    name = input(f'Name of student #{i+1}: ')
    subjects = input(f'Subjects of student #{i+1}: ')
    subjects = subjects.split(sep=' ')

    journal.update({name:subjects})

def show_all():
    new_journal = {k: v for k, v in sorted(journal.items(), key=lambda item: item[0], reverse=True)}
    for key in new_journal.keys():
        print(key + str(new_journal[key]))

    return

def student_for_sub(name):
    if name not in journal.keys():
        print('Name not found')
    else:
        return journal[name]

def sub_for_students(sub):
    names = []
    for key in journal.keys():
        if sub in journal[key]:
            names.append(key)

    if len(names) == 0:
        print('Nothing found')
    else:
        return names

show_all()
print(student_for_sub('John'))
print(sub_for_students('math'))