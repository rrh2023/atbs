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