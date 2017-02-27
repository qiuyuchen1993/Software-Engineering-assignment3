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

def turn_on(a2d,x1,y1,x2,y2):
    for a in range(y1,y2+1):
        for b in range(x1,x2+1):
            a2d[a][b]=1
    return a2d

def turn_off(a2d,x1,y1,x2,y2):
    for a in range(y1,y2+1):
        for b in range(x1,x2+1):
            a2d[a][b]=0
    return a2d

def switch(a2d,x1,y1,x2,y2):
    for a in range(y1,y2+1):
        for b in range(x1,x2+1):
            if a2d[a][b]==1:
                a2d[a][b]=0
            else:
                a2d[a][b]=1
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
                numbers+=re.findall("[-\d]+",value[j])
            x1=int(numbers[0])
            y1=int(numbers[1])
            x2=int(numbers[2])
            y2=int(numbers[3])
        elif value[0]=='switch':
            command=value[0]
            for j in range(0,len(value)):
                numbers+=re.findall("[-\d]+",value[j])
            x1=int(numbers[0])
            y1=int(numbers[1])
            x2=int(numbers[2])
            y2=int(numbers[3])
        
        if (x1<0):
            x1=0
        elif (x1>N-1):
            x1=N-1
        if (x2<0):
            x2=0
        elif (x2>N-1):
            x2=N-1
        if (y1<0):
            y1=0
        elif (y1>N-1):
            y1=N-1
        if (y2<0):
            y2=0
        elif (y2>N-1):
            y2=N-1
        print(command,x1,y1,x2,y2)
        if(x1<=x2 and y1<=y2):
        


#打开灯
            if command=="turn on":
                turn_on(a2d,x1,y1,x2,y2)
            elif command=="turn off":
                turn_off(a2d,x1,y1,x2,y2)
            elif command=="switch":
                switch(a2d,x1,y1,x2,y2)
    return a2d

def countnumber(a2d):
    countnumber=0
    for i in range(len(a2d)): 
        for j in range(len(a2d)):
            if a2d[i][j]==1:
                countnumber+=1
    return countnumber
    
'''import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input',help='inout help')
args = parser.parse_args()

url=args.input'''
url="http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
file=getfile(url)
a2d=LED(file)
number=countnumber(a2d)
print(number)  