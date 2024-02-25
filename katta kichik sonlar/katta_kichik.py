def find_elder(a,b,c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    elif b > a:
        if b > c:
            return b
        else:
            return c
    elif c > a:
        if c > b:
            return c
        else:
            return b

print(find_elder(2,5,8))