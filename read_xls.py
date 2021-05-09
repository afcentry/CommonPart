# _*_ coding:utf-8 _*_
"""
----------------------------------
filename:  read_xls
author:    afcentry
date:      2021/4/15
description:
----------------------------------
"""
# -*- coding: utf-8 -*-
import xlrd


def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook(r'ljq.xls')
    # 获取所有sheet
    print(workbook.sheet_names())  # [u'sheet1', u'sheet2']
    # 获取sheet2
    # sheet2= workbook.sheet_names()[1]
    # print(sheet2_name)
    # 根据sheet索引或者名称获取sheet内容
    sheet2 = workbook.sheet_by_name('表单')
    # sheet的名称，行数，列数
    print(sheet2.name, sheet2.nrows, sheet2.ncols)
    for row_index in range(1, 8000):
        row = sheet2.row_values(row_index)
        print(row)
        title = row[1]
        itemid = str(row[2]).split("=")[1] if row[2] else ""
        price = float(row[5])
        special_content = str(row[8])
        break
    # rows = sheet2.row_values(3) # 获取第四行内容
    # cols = sheet2.col_values(2) # 获取第三列内容
    # print(rows)
    # print(cols)
    # #获取单元格内容的三种方法
    # print(sheet2.cell(1,0).value.encode('utf-8'))
    # print(sheet2.cell_value(1,0).encode('utf-8'))
    # print(sheet2.row(1)[0].value.encode('utf-8'))
    # # 获取单元格内容的数据类型
    # print(sheet2.cell(1,3).ctype)


if __name__ == '__main__':
    read_excel()
