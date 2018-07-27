kwargs = {
    'username': 'test_user',
    'password': 'test_passwd',
    'host': 'test_host'
}

X_EXPECT = "My name is %(username)s and passwd is %(password)s "

print(X_EXPECT % (kwargs))
print(X_EXPECT)

ticker_list = [1.30, 2.30, 3.30, 4.30]  # these are excel columne name

getticks_listofdict = [{'T': 1.30, 'BV': 11.30}, {'T': 2.30, 'BV': 22.3}, {'T': 4.30, 'BV': 44.3},
                       {'T': 5.30, 'BV': 55.3}]

for v in getticks_listofdict:
    if v['T'] in ticker_list:
        print(v['BV'])
    else:
        print()

k = [v['BV'] if v['T'] in ticker_list else 0 for v in getticks_listofdict]
print(k)

keys = [val['T'] for val in getticks_listofdict]
for t in ticker_list:
    if t in keys:
        for v in getticks_listofdict:
            pass
    else:
        print()

ticker_list = [1.30, 2.30, 3.30, 4.30]  # these are excel columne name
getticks_listofdict = [{'T': 1.30, 'BV': 11.30}, {'T': 2.30, 'BV': 22.3}, {'T': 4.30, 'BV': 44.3},
                       {'T': 5.30, 'BV': 55.3}]


def convert_list_of_dict_to_dict(getticks_listofdict):
    temp = dict()
    for val in getticks_listofdict:
        temp[val['T']] = val['BV']
    return temp


temp_dict = convert_list_of_dict_to_dict(getticks_listofdict)
k = [temp_dict[i] if i in temp_dict.keys() else 0 for i in ticker_list]
print(k)

for i in ticker_list:
    if i in temp_dict.keys():
        print(temp_dict[i])
    else:
        print()

k = [temp_dict[i] if i in temp_dict.keys() else 0 for i in ticker_list]

print(k)


def my_data(myage):
    print("My age is %s and my name is Ana" % str(myage))
    print("My age is " + str(myage) + "and my name is Ana")


my_data(myage=21)
