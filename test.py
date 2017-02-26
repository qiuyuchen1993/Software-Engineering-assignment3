import urllib.request
#request
url="http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"

if url.startswith('http'):
    req = urllib.request.urlopen(url)
    buffer=req.read().decode('utf-8')
    lines=buffer.splitlines()
    print(lines)
    print(len(lines))
    N=int(lines[0])
    print('N',N)
    #start with second line
    #建立led
    a2d = [ [0]*N for _ in range(N)]
    for i in range(1,len(lines)):
        value=lines[i].strip().split()
        if value[0]=='turn':
            command=value[0]+" "+value[1]
            position1=value[2].split(',')
            position2=value[4].split(',')
            x1=int(position1[0])
            y1=N-int(position1[1])-1
            x2=int(position2[0])
            y2=N-int(position2[1])-1
        elif value[0]=='switch':
            command=value[0]
            position1=value[1].split(',')
            position2=value[3].split(',')
            x1=int(position1[0])
            y1=N-int(position1[1])-1
            x2=int(position2[0])
            y2=N-int(position2[1])-1
        if(x1>x2):
            x1,x2=x2,x1
        if(y1>y2):
            y1,y2=y2,y1


#打开灯
        if command=="turn on":
            for a in range(y1,y2+1):
                for b in range(x1,x2+1):
                    a2d[a][b]=1
        elif command=="turn off":
            for a in range(y1,y2+1):
                for b in range(x1,x2+1):
                    a2d[a][b]=0
        elif command=="switch":
            for a in range(y1,y2+1):
                for b in range(x1,x2+1):
                    if a2d[a][b]==1:
                        a2d[a][b]=0
                    else:
                        a2d[a][b]=1
    
else:
    print('It is an invalid url')
    
#算灯亮数量
countnumber=0
for i in range(N): 
    for j in range(N):
        if a2d[i][j]==1:
            countnumber+=1
print (countnumber)
z=len(a2d)
print(z)
    


'''
#建立led
from pprint import pprint
a2d = [ [0]*N for _ in range(N)]

#把x，y分配给相应的值
while(x1>=0 and y1>=0 and x2>=0 and y2>=0 and x1<=N-1 and x2<=N-1 and y1<=N-1 and y2<=N-1): 
    if(x1>x2):
        x1,x2=x2,x1
    if(y1>y2):
        y1,y2=y2,y1


#打开灯
    if command=="turn on":
        for a in range(y1,y2+1):
            for b in range(x1,x2+1):
                a2d[a][b]=1
    elif command=="turn off":
        for a in range(y1,y2+1):
            for b in range(x1,x2+1):
                a2d[a][b]=0
    elif command=="switch":
        for a in range(y1,y2+1):
            for b in range(x1,x2+1):
                if a2d[a][b]==1:
                    a2d[a][b]=0
                else:
                    a2d[a][b]=1
    
    pprint(a2d)
    command=input('please enter the command')
    x1=int(input('please enter the x of beginneing plot'))
    y1=int(input('please enter the y of beginneing plot'))
    x2=int(input('please enter the x of endding plot'))
    y2=int(input('please enter the y of endding plot'))
    y1=N-y1-1
    y2=N-y2-1
    
print("Inputs are invalid")


#算灯亮数量
countnumber=0
for i in range(N): 
    for j in range(N):
        if a2d[i][j]==1:
            countnumber+=1
print (countnumber)
'''