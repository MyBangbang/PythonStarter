#!/usr/bin/env python
# coding=utf-8
#字符串和列表的练习

#创建装态映射到缩写
states = {
        'Oregon': 'OR',
        'Florida': 'FL',
        'California': 'CA',
        'New York': 'NY',
        'Michigan': 'MI',
        }

#创建一个基本的国家和一些城市在他们
cities = {
        'CA': 'San Francisco',
        'MI': 'Detroit',
        'FL': 'Jacksonville'
        }

#加入一些更多的城市
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#打印出一些城市
print '-' * 10
print "NY State has: ", cities['NY']
print "OR state has: ", cities['OR']

#打印一些州
print '-' * 10
print "Michigan's addreviation is: ", states['Michigan']
print "Florida's addreviation is: ", states['Florida']

#然后，利用国家城市做
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

#打印每一个状态的缩写
print '-' * 10
for state, addrev in states.items():
    print "%s is addreviated %s" % (state, addrev)

#打印每一个城市的状态
print '-' * 10
for addrev, city in cities.items():
    print "%s has the city %s" % (addrev, city)

#现在做两个在同一时间
print '-' * 10
for state, addrev in states.items():
    print "%s state is addreviated %s and has city %s" % (state, addrev, cities[addrev])

print '-' * 10
#安全地得到一个缩写的状态，可能不在那里
state = states.get('Texas', None)

if not state:
    print "Sorry, no Texas."

#获得一个默认值的城市
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city

