#!/bin/python

import argparse

def main():
    parser = argparse.ArgumentParser()

    # All the arguments should be provided in the same order
    parser.add_argument("user_name", help="provide User Name")
    parser.add_argument("group_name", help="provide Group Name")
    parser.add_argument("func_name", help="provide Function Name")

    # The arguments will be stored in the args object and would be accessible like 'args.user_name'; as used below.
    args = parser.parse_args()

    print " Username: {0} \n Group Name: {1} \n Function Name: {2}".format(args.user_name,args.group_name,args.func_name)

if __name__=="__main__":
    main()

