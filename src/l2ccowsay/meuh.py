from .characters import COW

def mooing(txt: str = 'S2QT coding club is great'):
    tt = f'{"="*(len(txt)+4)}\n'
    tt += f"| {txt} |\n"
    tt += f'{"="*(len(txt)+4)}'
    return tt + COW