from pprint import pprint
a = [1,2,3,4,5,6,7,8,9,10]
a2d = [a,a,a,a]
pprint(a2d)

b = [0]*10
pprint(b)

N = 6
c2d = [ [0]*N for _ in range(N)]
pprint(c2d)

M = 6
e2d = [list(range(i*M,i*M+M)) for i in range(M)]
pprint(e2d)
pprint(e2d[2][1])

O=10
f=list(range(O))
pprint(f)
pprint(f[2:])
pprint(f[2:5])
f.reverse()
pprint(f)

