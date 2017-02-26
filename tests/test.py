from nose.tools import *
from NAME.functions import *

def test_LEDtester():
    expected=10
    res=len(LEDtester(10))
    eq_(res,expected,'The size does not match')
    
    