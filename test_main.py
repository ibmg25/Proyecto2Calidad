import pytest
from main import *

def test_valid_number():
    num_string = "+919876543210"
    assert isnumber(num_string) == True

def test_invalid_number():
    num_string = "1234567890"
    assert isnumber(num_string) == False