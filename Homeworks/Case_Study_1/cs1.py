import string

alphabet = ' ' + string.ascii_lowercase
positions = {}
for i in range(27):
    positions[alphabet[i]] = i


message = "hi my name is caesar"
def encode(message, key):
	encoded_message = str()
	item_list = list(positions.items())
	for letter in message:
	    print(letter, positions[letter], item_list[(positions[letter]+key)%27][0],
	          item_list[(positions[letter]+key)%27][1] )
	    encoded_message+=item_list[(positions[letter]+1)%27][0]
	return encoded_message 
encoded_message = encode(message, 10)
print(encoded_message)