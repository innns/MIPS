# >>>>>>
# Descripttion: 
# version: 1.0
# Author: Zx
# Email: ureinsecure@outlook.com
# Date: 2020-12-31 17:14:16
# LastEditors: Zx
# LastEditTime: 2020-12-31 17:18:21
# FilePath: /MIPS/mips_invert/hex2bin.py
# <<<<<<

f = open("mips_invert/imem.txt","r+")
a = ""
try:
    while True:
        text_line = f.readline()
        if text_line:
            a += "{:032b}".format(int(text_line.replace("\n",""),16))
            a += "\n"
        else:
            break
finally:
    f.close()

f = open("mips_invert/binary.txt","w")
f.write(a)
f.close()
