# https://coderbyte.com/information/Longest%20Word
# Have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty. 

# TestCase
# "fun&!! time" => time
# "I love dogs" => love

# Available characters are alphabets(lower/upper), blank, and numbers
def availableChars(char):
	if char == ' ':
		return True
	elif ord(char) in range(ord('a'), ord('z')+1):
		return True
	elif ord(char) in range(ord('A'), ord('Z')+1):
		return True
	elif ord(char) in range(ord('0'), ord('9')+1):
		return True
	else:
		return False

def LongestWord(sen):
	assert type(sen) == str
	assert len(sen) > 0

	if len(sen) == 1:
		return sen

	sen = ''.join([c for c in sen if availableChars(c)])
	maxLen = 0
	maxWord = ''

	for word in sen.split():
		if maxLen < len(word):
			maxLen = len(word)
			maxWord = word

	return maxWord


print(LongestWord('fun&!! time'))
print(LongestWord('I love dogs'))
print(LongestWord('123456789 98765432'))