

def NOT(a,b):
    parse(a,b)
    if a != b:
        return True
    else:
        return False

def AND(a,b):
    parse(a,b)
    if a == b:
        return True
    return False

def OR(a,b):
    if a == b and b == 0:
        return False
    return True

def XOR(a,b):
    parse(a,b)
    
    if a == b and b == 0 or a == b and b == 1:
        return False
    return True

def NAND(a,b):
    if a == b and b == 1:
        return False
    return True

def NOR(a,b):
    if a == b and b == 0:
        return True
    return False

def XNOR(a,b):
    if a == b and b == 0 or a == b and b == 1:
        return True
    return False

def parse(a,b):
    if a != 0 and a != 1 or b != 0 and b != 1:
        print("ERROR: ONLY 1 AND 0 ALLOWED")
        exit(1)

    else:
        pass