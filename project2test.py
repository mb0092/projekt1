## str1 = '| {name} | {surname} | {age} |'.format('name'= 'John', 'surname' = 'Smith', 'age' = 89)
str2 = '| {name} | {surname} | {age} |'.format(name= 'John', surname = 'Smith', age = 89)
## str3 = '| {name} | {surname} | {age} |'.format({name: 'John', surname : 'Smith', age : 89})
str4 = '| {name} | {surname} | {age} |'.format(**{'name': 'John', 'surname' : 'Smith', 'age' : 89})
print(str2)
print(str4)