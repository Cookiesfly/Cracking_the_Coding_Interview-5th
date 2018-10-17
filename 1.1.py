#实现一个算法，确定一个字符串的所有字符是否全都不同。假使不允许使用额外的数据结构，又该如何处理？
#Implement an algorithm to determine if a string has all unique characters. What if you can not use additional data structures?

# -*- coding:utf-8 -*-
class Different:
    def checkDifferent1(self, iniString):
        return len(set(iniString)) == len(iniString)


    def checkDifferent2(self, iniString):
        for i in iniString:
            if (iniString.count(i)>1):
                return False
        return True