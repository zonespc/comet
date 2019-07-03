#!/usr/bin/env python
# coding=utf-8


def binary_search(a,k):
    if len(a) < 1:
        return -1
    low = 0
    high = len(a)-1
    middle = low + (high-low)/2
    while low <= high and a[middle] != k:
        if a[middle] < k:
            low = middle+1
        else:
            high = middle-1
        middle = low + (high - low) / 2
    if low <= high:
        return middle
    return -1


def main():
    print "binary search"
    a = [1, 2, 3, 4, 5]
    print a
    print binary_search(a, 6)


if __name__ == '__main__':
    main()