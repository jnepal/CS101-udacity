name = 'Dave'

print(name[1])
print(name[-1])  #counts from backward

print('Hello ' + name + '!' * 3)

word = 'assume'

print(word[1:5])  #print()s all the letters from including that of position 1 to position 5(not included)
print(word[1:])
print(word[:5])
print(word[:])

#Find Method String

pythagoras = 'There is geometry in the humming of the strings, there is Music in the spacing of the spheres'
print(pythagoras.find('string'))  #Case Sensitive, Returns the position of first occurence of string 'string'
print(pythagoras[40:])
print(pythagoras.find('is', 6)) #Case Sensitive, Returns the position of first occurence of string 'is' after the position 6


print('pythagoras'.find('p'))#Case Sensitive, Returns the position of first occurence of letter 'p' in string 'pythagoras'