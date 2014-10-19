#!/usr/bin/python
from optparse import OptionParser


def read_flags():
    '''reads flags from command line'''
    usage = """usage: %prog [options] args"""
    parser = OptionParser(usage)
    parser.add_option("-c", "--count", dest="count", type='int',default=5,help='Optional. Default: 5.')
    options, args = parser.parse_args()
    return options



def hello_world(count=5):
    for i in xrange(0,count):
        print 'hello world'

if __name__ == '__main__':
    options = read_flags()
    hello_world(options.count)
