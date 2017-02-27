
def getfile(url):
    import urllib.request
    if url.startswith('http'):
        req = urllib.request.urlopen(url)
        buffer=req.read().decode('utf-8')    
    else:
        print('It is an invalid url')
    
    return buffer

def LEDtester(N):
    a2d = [ [0]*N for _ in range(N)]
    return a2d
       
def LED(buffer):
    import re
    lines=buffer.splitlines()
    N=int(lines[0])
    #start with second line
    #建立led
    a2d = LEDtester(N)
    for i in range(1,len(lines)):
        numbers=[]
        value=lines[i].strip().split()
        
        if value[0]=='turn':
            command=value[0]+" "+value[1]
            for j in range(0,len(value)):
                numbers+=re.findall(r'(\w*[0-9]+)\w*',value[j])
            x1=int(numbers[0])
            y1=N-int(numbers[1])-1
            x2=int(numbers[2])
            y2=N-int(numbers[3])-1
        elif value[0]=='switch':
            command=value[0]
            for j in range(0,len(value)):
                numbers+=re.findall(r'(\w*[0-9]+)\w*',value[j])
            x1=int(numbers[0])
            y1=N-int(numbers[1])-1
            x2=int(numbers[2])
            y2=N-int(numbers[3])-1
        #print(command,x1,y1,x2,y2)
        if (x1<0):
            x1=0
        elif (x1>N-1):
            x1=N-1
        if (x2<0):
            x1=0
        elif (x2>N-1):
            x1=N-1
        if (y1<0):
            y1=0
        elif (y1>N-1):
            y1=N-1
        if (y2<0):
            y1=0
        elif (y2>N-1):
            y1=N-1
        
        if(x1<=x2 and (N-y1-1)<=(N-y2-1)):
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
    return a2d

def countnumber(a2d):
    countnumber=0
    for i in range(len(a2d)): 
        for j in range(len(a2d)):
            if a2d[i][j]==1:
                countnumber+=1
    return countnumber
    
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input',help='inout help')
args = parser.parse_args()

url=args.input 


file=getfile(url)
a2d=LED(file)
number=countnumber(a2d)
print(number)  
