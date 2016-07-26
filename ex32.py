#!/usr/bin/env python
# coding=utf-8
#for-loop(for循环)

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'qiarters']

#这第一种循环通过一个列表
for number in the_count:
    print "This is count %d" % number

#同上
for fruit in fruits:
    print "Afruit of type: %s" % fruit

#我们也可以通过混合列表太
#通知我们必须使用%r因为我们不知道它是什么
for i in change:
    print "I got %r" % i

#我们也可以建立一个列表，先从一个空的
elements = []

#然后使用范围功能做0至5项
for i in range(0, 6):
    print "Adding %d to the list." % i
    #追加是一个函数，表明白
    elements.append(i)

#现在我们可以打印出来过
for i in elements:
    print "Element wasL %d" % i

