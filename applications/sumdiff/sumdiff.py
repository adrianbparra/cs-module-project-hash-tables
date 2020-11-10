"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here

# calculate the total for all in a dict

calcDict = {}

for val in q:

    calcDict[val] = f(val)

# print(calcDict)

# make a dict of all values added
addDict = {}
subDict = {}
# make a dict of all values subtracted


for k,v in calcDict.items():
    for k2,v2 in calcDict.items():
        keyString = str(f'{k},{k2}')
        addDict[str(v+v2)] = str(f'{k} + {k2}')
        subDict[str(v-v2)] = str(f'{k} - {k2}')

print(addDict)
print(subDict)

for k,v in addDict.items():

    if k in subDict:
        print(v,'=', subDict[k])

