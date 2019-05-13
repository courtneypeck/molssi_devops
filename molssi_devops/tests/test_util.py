"""
Unit test for util module
"""

#Import packages
import molssi_devops as md
import pytest 
import sys

def test_title_case():
	"""Test title case function"""
	test_string = "ThIS is A StrIng"
	expected = "This Is A String "
	calculated = md.title_case(test_string)
	assert calculated == expected

def test_type_error():
	test_case = ['this', 'is', 'not', 'a', 'string']
	
	with pytest.raises(TypeError):
		md.title_case(test_case)
