helping_dict = {'a': 0, 'b': 0,'c': 0,'d': 0,'e': 0,'f': 0,'g': 0,'h': 0,'i': 0,'j': 0,'k': 0,'l': 0,'m': 0,'n': 0,'o': 0,'p': 0,'q': 0,'r': 0,'s': 0,'t': 0,'u': 0,'v': 0,'x': 0,'w': 0,'y': 0,'z': 0 }
n = int(input())
input_string = input()
result_array = [0] * len(input_string)
for A in range(0, len(input_string)):
	helping_dict[input_string[A]] += 1
	result_array[A] = helping_dict[input_string[A]]
q = int(input())
while(q != 0):
	p = int(input())
	print(result_array[p - 1] - 1)
	q -= 1
