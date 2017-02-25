#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Samren'
import xlrd,os
"""
open_workbool() 查看文件中的sheets
通过索引（heets_by_index）和sheet名称（sheets_by_name），定位工作表
获取行数和列数，及整行和整列
遍历sheet
获取具体的单元格
问题：31行 row_values(0)、col_values(0)括号中的零？
"""
def read_Excel():
    data = xlrd.open_workbook('user_Data.xlsx')
    #查看文件中所有的sheet名称
    print data.sheets()[0]

    #得到一个工作表，或者通过索引顺序 或sheets表名称
    table1= data.sheets()[0]
    #table1 = data.sheets_by_index(0) #索引
    #table1 = data.sheets_by_name('account') #sheets名称
    print table1

    #获取行数和列数
    nrows = table1.nrows
    ncols = table1.ncols
    print nrows , ncols

    #获取整行和整列的值（数组）
    print table1.row_values(0)
    print table1.col_values(0)

    #遍历sheet
    for i  in range(nrows):
        print "row %s: %s" % (i, table1.row_values(i))

    #获取单元格
    cell_A2 = table1.cell(1,0).value
    cell_B1 = table1.cell(0,1).value
    cell_A1 = table1.cell(0,0).value
    cell_C3 = table1.cell(1,1).value
    print cell_A2,cell_B1,cell_A1,cell_C3

    #分别使用行、列索引
    cell_B4 = table1.row(3)[1].value
    cell_C2 = table1.col(2)[1].value
    print cell_B4,cell_C2

if __name__ == '__main__':
    read_Excel()