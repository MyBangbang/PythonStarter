#!/usr/bin/env python
# coding=utf-8
#读取文件

from sys import argv

script, filename = argv

txt = poen(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename agaun:"
file_again = raw_input(" > ")

txt_again = open(file_again)

print txt_again.read()

