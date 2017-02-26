from nose.tools import *
from NAME.functions import *

def test_LEDtester():
    expected=10
    res=len(LEDtester(10))
    eq_(res,expected,'The size does not match')
    
def test_countnumber():
    a2d = [ [1]*10 for _ in range(10)]
    expected=100
    res=countnumber(a2d)
    eq_(res,expected,'The countnumber does not match')
    
    
    