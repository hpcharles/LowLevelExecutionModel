#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import locale

theBox = dict(boxstyle="round", ec=(1., 0.5, 0.5), fc=(.5, .8, .5), )
ylabels = {" ": -1, 
           "Register":    0, "L1 Cache": 1, 
           "L2 Cache":    2, "L3 Cache": 3, 
           "Scratch Pad": 4, "DRAM"    : 5, 
#           "FLASH"      : 6, "SSD"     : 7, 
#           "Hard Drive" : 8, "Tapes": 9,
}
xlabels = {"None"  :      0, "Intrinsic" : 1,
           "C compiler":  2, "Compiler Vectorizer" : 3,
           "OpenMP"     : 4, "":5}
dataSet = [
    {"txt": "UPMEM\nDPU",      "y": "DRAM",      "x": "C compiler",  "color": "green"},
    {"txt": "CPU\nScalar|Vector","y": "Register","x": "C compiler",  "color": "green"},
    {"txt": "Michigan\nCompute Cache",  "y": "L1 Cache", "x": "None",  "color": "green"},
    {"txt": "Mutlu\nRowClone", "y": "DRAM",     "x": "None",    "color": "green"},
    {"txt": "Mutlu\nTesseract","y": "DRAM",     "x": "Intrinsic",    "color": "green"},
#    {"txt": "CEA\nC-SRAM\n                     ","y": "Scratch Pad", "x": "Intrinsic",  "color": "red"},
]
if __name__ == '__main__' :
    plt.figure (figsize=(10, 10))
    plt.xticks(list(xlabels.values()), list(xlabels.keys()))
    plt.yticks(list(ylabels.values()), list(ylabels.keys()))
    for d in dataSet:
        plt.text(xlabels[d["x"]], ylabels[d["y"]]-0.5, d["txt"], size= 20, color = d["color"], bbox= theBox)
    plt.text(xlabels["Intrinsic"], ylabels["Scratch Pad"]-1.5, "CEA\nC-SRAM", size= 50, color = "red", bbox= theBox)

    plt.draw()
#    plt.show()
    plt.savefig("OtherApproaches.png")
