'''
    The Name says it all. It generates bad hash
    Doesnot distribute evenly
'''
def badHashString(keyword,size):
    return ord(keyword[0]) % size

print(badHashString('Sabin', 3))
print(ord('s'))


'''
    Test Written to check whether the Algorithm
    used to generate the Hash Table is Evenly
    distributed or Not
'''
def testHashFunction(func, keys, size):
    results = [0] * size
    keysUsed = []
    for w in keys:
        if(w not in keysUsed ):
            hv = func(w, size)
            results[hv] +=1
            keysUsed.append(w)
    return results

print(testHashFunction(badHashString, 'I am Learning Python. Currently undertaking the Udacity CS101 Intro in Computer Science Course', 5))


def hashString(string, bucketSize):
    totalASCIIvalue = 0
    for char in string:
        totalASCIIvalue += ord(char)
    return totalASCIIvalue % bucketSize

print(hashString('udacity', 12))
'''

    can also be done as this

     def hashTable(size):
        table = [[]]*size
        return table
'''
#Creates Empty hash Table(^alternate method)
def makeHashTable(size):
    table = []

    for i in range(0,size):
        table.append([])

    return table

# print(makeHashTable(10))
'''
    Get the position of bucket in which
    the string is stored
'''
def hashTableGetBucket(hashtable, keyword):
    return hashString(keyword, len(hashtable))


def hashTableAdd(hashtable, keyword, url):
    position = hashTableGetBucket(hashtable, keyword)
    for entry in hashtable[position]:
        if(entry[0] == keyword):
            entry[1].append(url)
            return hashtable
    hashtable[position].append([keyword, [url]])
    return hashtable

table = makeHashTable(3)
hashTableAdd(table, 'udacity', 'http://udacity.com')
hashTableAdd(table, 'udacity', 'http://ncm.com')
hashTableAdd(table, 'coursera', 'http://coursera.com')
hashTableAdd(table, 'eudonix', 'http://eduonix.com')
print(table)
# print(hashTableGetBucket(table, 'udacity'))

def hashTableLookup(hashtable, keyword):
    position = hashTableGetBucket(hashtable, keyword)
    for entry in hashtable[position]:
        if entry[0] == keyword:
            return entry[1]
    return []

# print(hashTableLookup(table, 'udacity'))

def hashTableUpdate(hashtable, keyword, value):
    position = hashTableGetBucket(hashtable, keyword)
    for entry in hashtable[position]:
        if(entry[0] == keyword):
            entry[1] = value
            return hashtable
    return 'No match for the Keyword found'

# print(hashTableUpdate(table, 'udacity', 'http://udacity.org'))