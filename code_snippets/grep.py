######################### USAGE ##############
# $python grep.py myfile.txt 'letspython3x'
##############################################

from sys import argv
import re

for line in open(argv[1]):
    if re.search(argv[2], line):
        print(line)
