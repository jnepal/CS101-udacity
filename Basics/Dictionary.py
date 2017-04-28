'''
    Dictionary is Key value pair
    It is mutable like list
    It is analogous to Hash Table
'''
elements = { 'hydrogen': 1, 'helium': 2, 'carbon': 6 }

print(elements['hydrogen'])

elements['nitrogen'] = 7

print(elements)

#Checking whether the key is present in Dictionary or not

print('boron' in elements)
print('boron' not in elements)

elementWithDetails = {}
elementWithDetails['H']  = {'name': 'Hydrogen', 'number': 1, 'weight': 1.00794}
elementWithDetails['He'] = { 'name': 'Helium', 'number': 2, 'weight': 4.002602, 'noble gas': True}

print(elementWithDetails['H'])
print(elementWithDetails['H']['name'])