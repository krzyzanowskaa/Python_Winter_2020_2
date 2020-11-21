p= True
q= False

r = bool('true')
print(r)
print(type(r))

s= p and q
t= p and not q
u= p or q
v = (p or q) and p
print(v)

U= False
if u:
    print('u is true')

if s:
    print('u is true')
    print('u is stil true')
else:
    print('u is not true')
for i in range (4, 9):
    print('i=' + str(i))



