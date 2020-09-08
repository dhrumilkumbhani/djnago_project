# ABHI= "abhishek"
# ROHAN ="rohan"
# # print("helolo wosxfhsdbf fge")
# print(f"{ABHI} and is a good nosyhrf fhue iur8 ewrfy7et rf{ROHAN}")


# ABHI= "abhishek"
# ROHAN ="rohan"
# print('{:3} is a good boy {:-2}'.format(ABHI,ROHAN))

# abhi = 12 *3 
# roahn =1346 % 3


# print('name      ' + repr(abhi) + 'good       ' + repr(roahn) + 'a')

# abhi="hello world\n \t"
# c=str(abhi)
# # print(c)
# lst = [1,2,3,4,5]
# abhi = repr((12.3,5,('fdfhdufdeh','sfnuh',lst)))
# # repr((x, y, ('spam', 'eggs')))
# print(abhi)
# import random
# print(f"DFHDIHF DFHIU DNG DIDN {random.randint(1,10)}")
# table = {'Sjoerd': 8474867487568478567, 'Jack': 4098, 'Dcab': 7678}
# for name, phone in table.items():
#     print(f'{name[2:4]} ==> {phone:2d}')

# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
# print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
#       'Dcab: {0[Dcab]:d}'.format(table))

# for x in range(1, 11):
#     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))



# def f1(self, x, y):
#     return min(x, x+y)

# class C:
#     f = f1
#     def g(self):
#         return 'hello world'

#     h = g


# abhi = C()
# a=abhi.f(57846847,467846798467)
# print(a)
# b=abhi.h()
# print(b)


# class Bag:
#     def __init__(self):
#         self.data = []

#     def add(self, x):
#         self.data.append(x)

#     def addtwice(self, x):
#         self.add(x)
#         self.add(x)


# abhi = Bag()
# abhi.add(120)   
# abhi.add(45)
# abhi.add(78677)  
# abhi.addtwice(23)   
# # print(abhi.data)
# import os
# print(os.getcwd())

# str1="tea for abhi"
# str2=str1.replace('tea','cbghxchdx')
# print(str2)

# 'abhi is a good'.replace('abhi','khatam')

# import smtplib
# server = smtplib.SMTP('localhost')
# server.sendmail('abhidhameliya94271@gmail.com', 'abhidhameliya111@gmail.com')
# server.quit()

# from urllib.request import urlopen
# with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
#     for line in response:
#         line = line.decode('utf-8')  # Decoding the binary data to text.
#         if 'EST' in line or 'EDT' in line:  # look for Eastern Time
#             print(line)
# from datetime  import date
# bid=date(1999,12,18)
# now = date.today()
# age = now - bid
# print(age)

# import reprlib
# print(reprlib.repr(set('abcshdfhiughruihgr')))
# import pprint
# t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
# print(t)
# # pprint.pprint(t)
# import textwrap
# doc = """The wrap() method is just like fill() except that it returns
#  a list of strings instead of one big string with newlines to separate
#  	the wrapped lines."""
# print(doc)
# print(textwrap.fill(doc, width=12))
# locale setting nahi thtu
# from string import Template
# t = Template('${village}folk send $$10 to ${cause}.')
# print(t.substitute(village='Nottingham', cause='the ditch fund'))

# 11.2 11.3 SKIPPPED

# import logging
# logging.debug('Debugging information')
# logging.info('Informational message')
# logging.warning('Warning:config file %s not found', 'server.conf')
# logging.error('Error occurred')
# logging.critical('Critical error -- shutting down')

# from array import array
# a = array('H',[4000, 10, 700, 22222,136])
# print(sum(a))
# print(a[1:4])
# list1= [23,5,7,89,90,12]
# print(sum(list1))

# from collections import deque
# d = deque(["task1", "task2", "task3"])
# d.append("main")
# d.appendleft("iop")
# print(d)
# d.popleft()
# abh= ["scfd","vcv"]
# d.extendleft(abh)
# print(d)


# import bisect
# scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
# bisect.insort(scores, (50, 'ruby'))
# print(scores)



# from heapq import heapify, heappop, heappush
# data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
# heapify(data)
# heappush(data,90)
# [heappop(data) for i in range(3)]
# print(data)


from decimal import *
n=Decimal(12.5665) * Decimal(2.5)
print(n)