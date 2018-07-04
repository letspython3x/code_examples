#!/bin/python
import importlib


import argparse
import sys

def main():
    sys.path.append(sys.argv[1])
    i = importlib.import_module(sys.argv[2])
    #__import__(sys.argv[1], 'Ftp')

    #print my_var
    #print_arg(my_var.Ftp)
    kwargs = {
            'protocol' : 'ftp',
            'server' : 'ftp.dlptest.com',
            'user' : 'dlpuser@dlptest.com',
            'password' : 'hZ3Xr8alJPl8TtE',
            'working_dir':'',
            }

    obj2 = i.EtlFile(**kwargs)
    obj2.get()

def print_arg(var):
    print var


if __name__=="__main__":
    main()

