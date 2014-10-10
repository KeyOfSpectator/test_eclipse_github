#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
Created on 2014年10月10日

@author: KeyOfSpectator
'''

print 'this is mod1'
print '这是中文'

import sys

def test():
    args = sys.argv
    print "args len == " ,len(args)
    if len(args)==1:
        print 'args len == 1'
    elif len(args)==2:
        print 'Hello,%s'% args[1]
    else:
        print 'too many arguments'

print __name__
if __name__ == '__main__':
    test()
    
    
    