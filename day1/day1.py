#!/usr/bin/env python

def main():
    with open('input.txt') as input:
        data = input.readline()
        floor = data.count('(') - data.count(')')
        print(floor)

if __name__ == "__main__":
    main()
