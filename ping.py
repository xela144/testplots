#!/usr/bin/python

import sys, re
import numpy as np
import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt


def main():
    if sys.stdin.isatty():
        print ("Please use a pipe as stdin\nExample: ping stackoverflow.com | python script.py")
        return 0
    regex = re.compile('time=(\d+.\d+)')

    data = [0]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    #l1, = ax.plot(data)
    fig.show()

    while True:
        #get ping, if no string: stream has ended
        line = sys.stdin.readline()
        if line == '':
            break
        #conversion: 64 bytes from 127.0.0.1: icmp_seq=0 ttl=45 time=100.873 ms --> 100.873
        match = regex.findall(line)
        number = 0.

        if len(match) > 1:
            raise ValueError()
        if len(match) == 1:
            try:
                number = float(match[0])
            except ValueError as e:
                print (e)
        #add number to array, plot the data
        data.append(number)
        l1, = ax.plot(data, 'r')
        plt.draw()
    return 0

if __name__ == '__main__':
        sys.exit(main())
