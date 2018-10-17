#用C或C++实现void reverse(char* str)函数，即反转一个null结尾的字符串
#Write code to reverse a C-Style String. (C-String means that “abcd” is represented as five characters, including the null character.)

# -*- coding:utf-8 -*-
class Reverse:
    def reverseString(self, iniString):
        return iniString[::-1]


# C++
# class Reverse1 {
# public:
#     void swap(char &a, char &b)
#     {
#         char temp = a;
#         a = b;
#         b = temp;
#     }
    
#     string reverseString(string iniString) {
#         if(iniString.empty())
#             return iniString;
#         int len = iniString.size();
#         for(int i = 0, j = len-1; i < j; i++, j--)
#         {
#             swap(iniString[i], iniString[j]);
#         }
#         return iniString;
#     }
# };