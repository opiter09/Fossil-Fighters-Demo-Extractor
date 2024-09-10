# Fossil-Fighters-Demo-Extractor
You MUST put the ROM in the same folder as the exe, or it won't work.

This tool extracts the files out of the FF1 and FFC Kiosk demos (the tiny ~2MB ones; the bigger ones already have normal files). It then runs them through fftool, so you get PNGs and whatnot. You should also be
able to run the resulting out.nds through Carbonizer to get the text. It should work on both the American and Japanese demos, though I have only tested it on the former.

Also, you download this by pressing the green "Code" button and choosing "Download ZIP," and
you run it by dragging and dropping an FF1/FFC demo ROM onto demoExtract.exe.

# Source Codes
- Narchive: https://github.com/nickworonekin/narchive (note that I have modified exract.cmd)
- FFTool: https://github.com/jianmingyong/Fossil-Fighters-Tool
- NDSTool: https://github.com/devkitPro/ndstool (this is a later version; the one used here came without a license as part of DSLazy)
- CUE Decompressors (Blz.exe): https://www.romhacking.net/utilities/826/
