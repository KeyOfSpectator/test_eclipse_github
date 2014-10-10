#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
Created on 2014��10��10��

@author: KeyOfSpectator
'''
def _private_1(name):
    return 'hello private1, %s'% name

def _private_2(name):
    return 'hello private2, %s'% name

def greeting(name):
    if len(name)>3:
        return _private_1(name)
    else:
        return _private_2(name)

print 'blablabal'