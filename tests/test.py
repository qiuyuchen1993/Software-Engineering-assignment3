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
    
def test_turnon():
    a2d=[ [0]*5 for _ in range(5)]
    light=turn_on(a2d,0,0,0,0)
    res=countnumber(light)
    expected=1
    eq_(res,expected,'The turn_on is not right')

def test_turnoff():
    a2d=[ [1]*2 for _ in range(2)]
    light=turn_off(a2d,0,0,1,1)
    res=countnumber(light)
    expected=0
    eq_(res,expected,'The turn_off is not right')
    
def test_switch():
    a2d=[ [1]*2 for _ in range(2)]
    light=switch(a2d,0,0,1,1)
    res=countnumber(light)
    expected=0
    eq_(res,expected,'The switch is not right')
    
