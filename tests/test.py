from nose.tools import *
from NAME.functions import *

def test_LEDtester():
    expected=10
    res=len(LEDtester(10))
    eq_(res,expected,'The size does not match')
    
def test_LEDtester1():
    expected=1000
    res=len(LEDtester(1000))
    eq_(res,expected,'The size does not match')
    
    
def test_countnumber():
    a2d = [ [1]*10 for _ in range(10)]
    expected=100
    res=countnumber(a2d)
    eq_(res,expected,'The countnumber function is not right')

def test_all():
    expected=400410
    file=getfile("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt")
    a2d=LED(file)
    res=countnumber(a2d)
    eq_(res,expected,'The countnumber does not match')
    

    