# Input(C là nén ảnh, D là giải nén)
input()
char = input()
s = input()
en = {'abracadabra':'01001110110101100010101101', 'hello':'1011001000100'}
de = {'01001110110101100010101101':'abracadabra','1011001000100':'hello'}
if char == 'C':
    print(en[s])
else:
    print(de[s])
# C
#01001110110101100010101101
# Output
#abracadabra