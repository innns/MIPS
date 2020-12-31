# >>>>>>
# Descripttion: 
# version: 1.0
# Author: Zx
# Email: ureinsecure@outlook.com
# Date: 2020-12-31 17:14:16
# LastEditors: Zx
# LastEditTime: 2020-12-31 17:14:16
# FilePath: /MIPS/mips_invert/hex2bin.py
# <<<<<<
# >>>>>>
# Descripttion: 
# version: 1.0
# Author: Zx
# Email: ureinsecure@outlook.com
# Date: 2020-12-31 16:50:58
# LastEditors: Zx
# LastEditTime: 2020-12-31 17:03:49
# FilePath: /MIPS/mips_invert/16to2.py
# <<<<<<
f = open("mips_invert/binary.txt","r+")
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

f = open("mips_invert/binary","w+")
f.write(a)
f.close()

