# Create a function that reverses a string:
# 'Hi My name is Andrei' should be:
# 'ierdnA si eman yM iH'

def reverse(string):
	assert type(string) == str, 'Hmm that is not good'

	return ''.join([string[i] for i in range(len(string)-1, -1, -1)])
	# result = []
	# for i in range(len(string)-1, -1, -1):
	# 	result.append(string[i])
	# return ''.join(result)

def reverse2(string):
	assert type(string) == str, 'Hmm that is not good'
	
	result = list(string)
	result.reverse()
	return ''.join(result)

print(reverse('Hi My name is Andrei'))
print(reverse2('Hi My name is Andrei'))

# print()
# print(reverse(123))