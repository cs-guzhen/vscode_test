#!/usr/bin/env python

import string

alphas = string.letters + '_'
nums = string.digits

print 'Welcome to the Identifier Checker v1.0'
print 'Testees must be at least 2 chars long.'
myInput = raw_input('Idendifier to test? ')

if len(myInput) > 1:
    if myInput[0] not in alphas:
        print 'Invalid: first symbol must be alphabetic'
    else:
        for otherChar in myInput[1:]:
            if otherChar not in alphas + nums:
                print 'Invalid: remaining symbols must be alphabetic'
                break
        else: #只有当for循环正常结束才运行
            print "okay as an identifier."