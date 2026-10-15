import numpy as np

v1 = []
v2 = []
eq = "f"

v1 += [int(input("input x for vector 1 "))]
v1 += [int(input("input y for vector 1 "))]
v1 += [int(input("input z for vector 1 "))]

v2 += [int(input("input x for vector 2 "))]
v2 += [int(input("input y for vector 2 "))]
v2 += [int(input("input z for vector 2 "))]
    
v1 = np.array(v1)
v2 = np.array(v2)

print("sum: ", v1 + v2)
print("mult: ", v1 @ v2)
print("vmult: ", np.cross(v1, v2))
cos =  (v1 @ v2)/(np.linalg.norm(v1) * np.linalg.norm(v2))
if round(cos) - 0.1 == 0.9:
    if cos == 1:
        eq = "equal directions"
    else:
        if round(cos * 10)/10 - 0.1 >= 0.9:
            eq = "almost equal"
else:
    eq = "directions aren't equal"
print("dir: ", cos, eq)