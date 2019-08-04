result = {'a': 0, 'b': 0,'c': 0,'d': 0,'e': 0,'f': 0,'g': 0,'h': 0,'i': 0,'j': 0,'k': 0,'l': 0,'m': 0,'n': 0,'o': 0,'p': 0,'q': 0,'r': 0,'s': 0,'t': 0,'u': 0,'v': 0,'x': 0,'w': 0,'y': 0,'z': 0 }
n = int(input())
input_string = input()
q = int(input())
string_index = [0] * q

for i in range(q):
	string_index[i] = int(input())

for A in input_string[:string_index[0]]:
	result[A] += 1
print(result[input_string[string_index[0]-1]] - 1)

for k in range(1, len(string_index)):
	if(string_index[k] < string_index[k-1]):
		result = {'a': 0, 'b': 0,'c': 0,'d': 0,'e': 0,'f': 0,'g': 0,'h': 0,'i': 0,'j': 0,'k': 0,'l': 0,'m': 0,'n': 0,'o': 0,'p': 0,'q': 0,'r': 0,'s': 0,'t': 0,'u': 0,'v': 0,'x': 0,'w': 0,'y': 0,'z': 0 }
		for A in input_string[:string_index[k]]:
			result[A] += 1
		print(result[input_string[string_index[k]-1]] - 1)

	else:
		for A in input_string[string_index[k-1] : string_index[k]]:
			result[A] += 1
		print(result[input_string[string_index[k]-1]] - 1)




