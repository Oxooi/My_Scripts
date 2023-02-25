#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fizz():

    # make loop for 1 to 100
    for i in range(1, 101):
        if(i % 5 == 0 ):
            print('Fizz')
        elif(i % 3 == 0 ):
            print('Buzz')
        elif(i % 15 == 0):
            print('FizzBuzz')
        else :
            print(i)


if __name__ == '__main__':
   fizz()