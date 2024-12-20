# Fossil-Fighters-Demo-Extractor

This tool extracts the files out of the FF1 and FFC Download Station demos (the tiny ~2MB ones; the bigger ones already have normal files).
It then runs them through fftool, so you get the PNGs and decompressed files. You should also be able to run the resulting out.nds through
Carbonizer (https://github.com/simonomi/carbonizer/releases) to get the text, events, etc. Finally, it has been confirmed
to work on both the American and Japanese demos.

You download this by pressing the green "Code" button and choosing "Download ZIP", and you run it by dragging and dropping an
FF1/FFC demo ROM onto demoExtract.exe. Note that you MUST put the ROM in the same folder as the exe, or it won't work.

NOTE: The output from fftool will be in the folder YKHE (for FF1) or VDEE (for FFC). Both the American and Japanese demos of a game will
use the same folder, so make sure to rename it if you would like to have both around.

# Source Codes
- Narchive: https://github.com/nickworonekin/narchive (note that I have modified extract.cmd)
- FFTool: https://github.com/jianmingyong/Fossil-Fighters-Tool
- NDSTool: https://github.com/devkitPro/ndstool (this is a later version; the one used here came without a license as part of DSLazy)
- CUE Decompressors (blz.exe): https://www.romhacking.net/utilities/826/
