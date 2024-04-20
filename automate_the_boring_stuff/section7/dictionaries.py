myCat = {'size': 'fat', 'color':'gray', 'disposition':'loud'}
myCat['size']
# 'fat'
'My cat has ' + myCat['color'] + ' fur.'
# 'My cat has gray fur.'
spam = {12345: 'Luggage combination', 42: 'The Answer'}
[1,2,3] == [3,2,1] 
# False
eggs = {'name':'Zophie', 'species': 'cat', 'age':8}
ham = {'species':'cat', 'name':'Zophie', 'age':8}
eggs == ham
# True
eggs['color']
# ERROR
'name' in eggs
# True
eggs
# {'name':'Zophie', 'species':'cat','age':8}
'name' not in eggs
# False

list(eggs.keys())
# ['name', 'species', 'age']
list(eggs.values())
# ['Zophie', 'cat', 8]
list(eggs.items())
# [('name', 'Zophie'), ('species', 'cat'), ('age', 8)]
eggs.keys()
# dict_keys(['name', 'species', 'age'])
for k in eggs.keys():
    print(k)
    # name, species, age
for v in eggs. values():
    print(v)
    # Zophie, cat, 8
for i in eggs.items():
    print(i)
    # ('name', 'Zophie'), ('species', 'cat'), ('age', 8)
eggs
# {'name': 'Zophie', 'species': 'cat', 'age': 8}
'cat' in eggs.values()
# True
eggs['color']
# ERROR
if 'color' in eggs:
    print(eggs['color'])
# 
eggs
# {'name': 'Zophie', 'species': 'cat', 'age':8}
eggs.get( 'age', 0)
# 8
eggs.get('color', '')
# ''
picnicItems = {'apples':5, 'cups':2}
print('I am bringing ' + str(picnicItems.get('napkins', 0)) + ' to the picnic.')
# I am bringin 0 to the picnic
print('I am bringin ' + str(picnicItems['napkins']) + 'to the picnic.')
# ERROR
eggs
# {'name': 'Zophie', 'species':'cat', 'age':8}
if 'color' not in eggs:
    eggs['color'] = 'black'
# 
eggs = {'name': 'Zophie', 'species':'cat', 'age':8}
eggs
# {'name':'Zophie', 'species':'cat', 'age': 8}
eggs.setdefault('color', 'black')
'black'
eggs
# {'name':'Zophie', 'color':'black', 'species':'cat', 'age':8}