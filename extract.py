import os
import shutil
import subprocess
import sys

try:
    shutil.rmtree("NDS_UNPACK")
except:
    pass
subprocess.run([ "dslazy.bat", "UNPACK", sys.argv[1] ])
try:
    os.remove("out_arm9.bin")
except:
    pass
subprocess.run([ "blz.exe", "-d", "NDS_UNPACK/arm9.bin", "out_arm9.bin" ])
n = open("out_arm9.bin", "rb")
r = n.read()
n.close()
for i in range(0, len(r), 8):
    if (int.from_bytes(r[i:(i + 8)], "big") == 0x4E415243FEFF0001):
        loc = i
        break
n2 = open("new.narc", "wb")
size = int.from_bytes(r[(loc + 8):(loc + 12)], "little")
n2.write(r[loc:(loc + size)])
n2.close()
subprocess.run([ "extract.cmd", "new.narc", "NDS_UNPACK/data" ])
subprocess.run([ "dslazy.bat", "PACK", "out.nds" ])
n3 = open("out.nds", "rb")
r3 = n3.read()
n3.close()
n3 = open("out.nds", "wb")
n3.close()
n3 = open("out.nds", "ab")
n3.write(r3[0:12])
if (r3[6] == 0):
    n3.write((0x594B4845).to_bytes(4, "big")) # YKHE
else:
    n3.write((0x56444545).to_bytes(4, "big")) # VDEE
n3.write(r3[16:])
n3.close()
subprocess.run([ "fftool.exe", "out.nds" ])