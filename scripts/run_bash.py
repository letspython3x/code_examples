import os

r = os.popen('sh test_bash.sh --username user').read()

print(r)

for i in r9:
    print i
