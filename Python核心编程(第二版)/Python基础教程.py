#coding:utf8
'''
kevin = ['Gu Kevin',18]
simth = ['Will Simth',20]
database = [kevin,simth]
print database

#索引
greeting = 'Hello'
print greeting[0]
print greeting[-1]
print "Hello"[1]
'''
#代码清单2-1 索引示例
#根据给定的年月日以数字形式打印日期
months = ['January','February','March','April','May','June','July','August','September','October','November','December']
#以1-31的数字作为结尾的列表
endings = ['st', 'nd', 'rd']+17*['th']+['st', 'nd', 'rd']+7*['th']+['st']
year = '2018' #raw_input('Year: ')
month = '10'  #raw_input('Month(1-12): ')
day = '31'    #raw_input('Day(1-31): ')
month_number = int(month)
day_number = int(day)
#记得要将月份和天数-1，以获得正确的索引
month_name = months[month_number-1]
ordinal = day+endings[day_number-1]
print month_name+' '+ordinal+', '+year

#代码清单2-2 分片示例
#对http://www.python.org形式的URL进行分割
url = 'http://www.python.org'
domain = url[11:-4]
print "Domain name: "+domain

#代码清单2-3 序列（字符串）乘法示例
#以正确的宽度在居中的盒子内打印一个句子
#注意，整数除法运算符（//）只能用在Python2.2及以后版本，在之前的版本中，只使用普通除法（/）
sentence = 'He is a very naughty boy!'
screen_width = 80
text_width = len(sentence)
box_width = text_width+6
left_margin = (screen_width-box_width)/2

print
print ' '*left_margin+'+'  +'-'*(box_width-2)+  '+'
print ' '*left_margin+'|  '+' '*text_width   +'  |'
print ' '*left_margin+'|  '+  sentence       +'  |'
print ' '*left_margin+'|  '+' '*text_width   +'  |'
print ' '*left_margin+'+'  +'-'*(box_width-2)+  '+'
print

#代码清单2-4 序列成员资格示例
#检查用户名和PIN码
database = [
['albert', '1234'],
['dilbert', '4242'],
['smith', '7542'],
['jones', '9843']
]
username = 'jones'
pin = '9843'
if [username, pin] in database: print 'Access granted'

#列表赋值
#指向同一列表
x = [2, 1, 6, 4]
y = x
y.sort()
print x

x = [2, 1, 6, 4]
y = x[:]
y.sort()
print x

###########################################
'''
from string import Template
s = Template('$x, glorious $x!')
s.substitute(x = 'slurm')
s = Template("It's ${x}tastic!")
s.substitute(x = 'slurm')
s = Template('A $thing must never $action.')
d = {}
d['thing'] = 'gentlemen'
d['action'] = 'show his sock'
s.substitute(d)


print ('%5d' %10)+'\n'+('%5d' %-10)
print ('%+5d' %10)+'\n'+('%+5d' %-10)
'''
###########################################

#代码清单3-1 字符串格式化示例
#使用给定的宽度打印格式化后的价格表
width = 35
price_width = 10
item_width = width - price_width
header_format = '%-*s%*s'
format = '%-*s%*.2f'
print '=' * width
print header_format %(item_width, 'Item', price_width, 'Price')
print '-' * width
print format %(item_width, 'Apples', price_width, 0.4)
print format %(item_width, 'Pears', price_width, 0.5)
print format %(item_width, 'Cantaloupes', price_width, 1.92)
print format %(item_width, 'Dried Apricots(16 oz.)', price_width, 8)
print format %(item_width, 'Prunes(4 lbs.)', price_width, 12)
print '=' * width








