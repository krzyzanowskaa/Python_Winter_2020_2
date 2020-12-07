s1='abcdef\''
print(s1)
s2="abcdef'"
print(s2)
s3='acd\t\tdb55666d\tij\nklm\\no\płłł'
print(s3)
i = 5
#print('i'+ str(i))
print('i={0}'.format (i))
print()
a='abcdef'
pos_cd = a.index('cd')
print(pos_cd)

def index(stack,needle):
    return stack.index(needle)
print(index(a,'cd'))

