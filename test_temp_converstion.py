from temp_conversion import fahr_to_kelvin

def test_working():
	assert fahr_to_kelvin(13.0) == 262.59444444444443
	
def test_negative():
	assert fahr_to_kelvin(-10.0) == 249.81666666666663
	
def test_integer():
	assert fahr_to_kelvin(13) == 262.59444444444443

def test_empty():
	assert fahr_to_kelvin()  #trying to test for empty entry but not working. 