#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
DocString 文档字符串

这个文件的功能是：

猜数字，首先生成一个数字
死循环，如果猜错就继续，如果猜对就退出
"""

magic = 22

while True:
    input = int(raw_input("please input an integer between 1-30:"))
    if input < 1 or input > 30:
        print "you must input integer between 1-30"
        continue
    if input == magic:
        print "ok, you just guess it ,exit"
        break
    else:
        print "you are wrong ,continue"
        continue