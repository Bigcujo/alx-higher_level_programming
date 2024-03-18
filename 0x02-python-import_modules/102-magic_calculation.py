"this will print the magic charater"
def magic_calculation(a, b):
    add = __import__('magic_calculation_102', globals(), locals(), ['add'], 0).__dict__['add']
    sub = __import__('magic_calculation_102', globals(), locals(), ['sub'], 0).__dict__['sub']
    
    if a < b:
        c = add(a, b)
        for x in range(4, 6):
            c = add(c, x)
        return c
    else:
        return sub(a, b)
