"""
Input
d = {
     Topic 1: [ (val_a, val_b) , (val_a, val_b), (val_a, val_b) ]
     Topic 2: [ (val_a, val_b) , (val_a, val_b), (val_a, val_b) ]
  Topic 3: [ (val_a, val_b) , (val_a, val_b), (val_a, val_b) ]
}
"""
"""
output

Column 1, Column 2,Column 3,Column 4,Column 5,Column 6
Topic 1,Topic 1, Topic 2, Topic 2, Topic 3, Topic 3
val a, val b, val a, val b, val a, val b
"""

d=dict()
header = "Column 1, Column 2,Column 3,Column 4,Column 5,Column 6"
with open('myfile.csv', 'w') as fin:
    topics = ''
    for key in d.keys():
        topics += "%s,%s" % key
    values = ''
    for val in d.values():
        values += "{0},{1}".format(*val)

    fin.write(header)
    fin.write(topics)
    fin.write(values)

