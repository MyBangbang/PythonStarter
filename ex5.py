#!/usr/bin/env python
# coding=utf-8
#更多的变量和打印

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that' s not too heavy."
print "He's got %s eyes and %s deoending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d , %d, and %d I get %d." %(my_age, my_height, my_weigth, my_age + my_height + my_weight)
