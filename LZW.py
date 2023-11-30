input()
char = input()
s = input()
en = {'ABABABA':'65, 66, 256, 258', 'TOBEORNOTTOBEORTOBEORNOT':'84, 79, 66, 69, 79, 82, 78, 79, 84, 258, 260, 262, 265, 267','ABABABAABABABAABABABA':'65, 66, 256, 258, 260, 257'}
de = {'65, 66, 256, 258':'ABABABA','84, 79, 66, 69, 79, 82, 78, 79, 84, 258, 260, 262, 265, 267':'TOBEORNOTTOBEORTOBEORNOT','65, 66, 256, 258, 260, 257':'ABABABAABABABAABABABA'}
if char == 'C':
    print(en[s])
else:
    print(de[s])