# >>>>>>
# Descripttion: 
# version: 1.0
# Author: Zx
# Email: ureinsecure@outlook.com
# Date: 2020-12-31 17:14:16
# LastEditors: Zx
# LastEditTime: 2020-12-31 20:10:05
# FilePath: /MIPS/mips/bin2hex.py
# <<<<<<

f = open("mips/binary","r+")
a = ""
try:
    while True:
        text_line = f.readline()
        if text_line:
            a += "{:08x}".format(int(text_line.replace("\n",""),2))
            a += "\n"
        else:
            break
finally:
    f.close()

f = open("mips/hexbin","w+")
f.write(a)
f.close()
