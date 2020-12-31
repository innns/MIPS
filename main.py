# >>>>>>
# Descripttion: 大写转换成小写
# version: 1.0
# Author: Zx
# Email: ureinsecure@outlook.com
# Date: 2020-12-31 16:06:56
# LastEditors: Zx
# LastEditTime: 2020-12-31 16:39:17
# FilePath: /MIPS/main.py
# <<<<<<
f = open("mips/assemble","r+")   #设置文件对象
a = f.read().lower()
f.close() #关闭文件
# r+模式 先读后写会变为追加模式 直接写会变成覆盖模式
f = open("mips/assemble","r+")   #设置文件对象
f.write(a)
f.close() #关闭文件

