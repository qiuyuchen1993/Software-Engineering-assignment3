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
    lines=buffer.splitlines()
    N=int(lines[0])
    #start with second line
    #建立led
    a2d = LEDtester(N)
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
args = parser.paese_args()

filename=args.input  '''  
url="http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
file=getfile(url)
a2d=LED(file)
number=countnumber(a2d)
print(number)  
