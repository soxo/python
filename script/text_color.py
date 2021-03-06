#!/usr/bin/python
# _*_ coding:utf-8 _*_



# Script Name   : text_color.py
# Author        : Zhang Dong  
# Last Modified :  
# Version       : 1.0 
# Last Modified :  


'''
startColor = '\033[1;31;40m'
endColor = '\033[0m'


print startColor

print '*'*30
print 'This the color test!'
print '*'*30


print endColor

'''


'''
格式：\033[显示方式;前景色;背景色m
  
   说明：
    前景色            背景色           颜色
    ---------------------------------------
    30                40              黑色
    31                41              红色
    32                42              绿色
    33                43              黃色
    34                44              蓝色
    35                45              紫红色 
    36                46              青蓝色
    37                47              白色
    显示方式           意义
    -------------------------
    0                终端默认设置
    1                高亮显示
    4                使用下划线
    5                闪烁
    7                反白显示
    8                不可见
                       
    例子：
    \033[1;31;40m    <!--1-高亮显示 31-前景色红色  40-背景色黑色-->
    \033[0m          <!--采用终端默认设置，即取消颜色设置--> 


'''

def startColor(color):
    db = {
    'black':'\033[1;30;40m',
    'red':'\033[1;31;40m',
    'green':'\033[1;32:40m',
    'yellow':'\033[1:33:40m',
    'blue':'\033[1:34:40m',
    'fuchsia':'\033[1:35:40m',
    'cyan':'\033[1:36:40m',
    'white':'\033[1:37:40m'
    }


    print db[color]



def endColor(n):

    print '\033[0m'
