
r,t = map(int,input().split())
w = []
d = 0
l = 0
h = 0
m = [0]*100
for i in range(r):
    s = input()
    c = 0
    f = 0 
    for j in range(len(s)):
        w.insert(j,s[j])
        if(w[j] == '.' and f!=1 ):
            c = c+1
        elif w[j] == 'S':
            c = 0
            f = 1
            if m[j]!= -1:
                d = d+1
                m[j] = -1
    
    l = l+c
    if(c!=0):
        h = h+1

print(l+(t-d)*(r-h))


        

        
