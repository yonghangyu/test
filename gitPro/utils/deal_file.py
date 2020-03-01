import os


def prinff():
    code_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(code_path)
    namelist = os.listdir(code_path)
    print(namelist)

def sum(a, b):
    return  a + b

def max(a, b):
    if a > b:
        return a
    else:
        return b
