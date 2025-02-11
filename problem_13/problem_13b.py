import math

def find_ab(xa, ya, xb, yb, xc, yc):
    if (float(ya) * xb - yb * xa) == 0:
        return -1, -1
    a = (yc * xb - yb * xc) / (ya * xb - yb * xa)
    b = (yc - a * ya) / yb
    return a, b

ans = 0

with open("input.txt", "r") as rf:
    while line := rf.readline():
        line = line.strip()
        line2 = rf.readline().strip()
        line3 = rf.readline().strip()
        rf.readline()
        xa, ya = [float(thing.split("+")[1]) for thing in line.split(":")[1].split(", ")]
        xb, yb = [float(thing.split("+")[1]) for thing in line2.split(":")[1].split(", ")]
        xc, yc = [float(thing.split("=")[1])+10000000000000 for thing in line3.split(":")[1].split(", ")]
        
        if xa/xb == ya/yb:
            print("we found a multiple lol")
        else:
            a, b = find_ab(xa, ya, xb, yb, xc, yc)
            if a.is_integer() and b.is_integer() and a >= 0 and b >= 0:
                ans += 3*a + b

print(ans)