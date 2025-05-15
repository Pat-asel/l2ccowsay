import sys
sys.path.insert(0, r"C:\Users\yassi\l2ccowsay\src\l2ccowsay")

from characters import OCTOPUS

def gloup(txt: str = 'gloup gloup gloup'):
    tt = f'{"="*(len(txt)+4)}\n'
    tt += f"| {txt} |\n"
    tt += f'{"="*(len(txt)+4)}'
    return tt + OCTOPUS

print(gloup())