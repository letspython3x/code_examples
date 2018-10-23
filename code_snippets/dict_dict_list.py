from collections import defaultdict

d = defaultdict(lambda: defaultdict(list))

for i in ['a','b','c']:
    for j in ['c','d','c','e','e','f']:
        for k in range(5):
            d[i][j].append(k)

for i in d.keys():
    print i
    print d[i]


print d
