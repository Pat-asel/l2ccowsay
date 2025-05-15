# -*- coding: utf-8 -*-
"""
Created on Thu May 15 15:13:55 2025

@author: Modoukpè
"""

import sys
sys.path.insert(0,r'C:\Users\Modoukpè\l2ccowsay\\')
from characters import KITTY

def meowing(txt: str = 'S2QT coding club is great'):
    tt = f'{"="*(len(txt)+4)}\n'
    tt += f"| {txt} |\n"
    tt += f'{"="*(len(txt)+4)}'
    return tt + KITTY
print(meowing())