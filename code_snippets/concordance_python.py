"""
It is a program that displays a concordance for a file i.e. 
it outputs the unique words and their frequencies in alphabetical order.
"""

f = "HELLO HELLO HELLO WHAT ARE YOU DOING"
myDict = {}
linenum = 0

for word in f.split():
    if not word in myDict:
        myDict[word] = []

    myDict[word].append(linenum)


print "%-15s %-15s" %("Word", "Frequency")
for key in sorted(myDict):
    print '%-15s: %-15d' % (key, len(myDict[key]))
