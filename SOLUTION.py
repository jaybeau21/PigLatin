#Project 4
#Due Date: 10/17/2018, 11:59PM
########################################
#                                      
# Name: Jarod Beaumariage
# Collaboration Statement:             
# 	I worked on my own while referencing the Python documentation.         
#
########################################



message = input('Enter your message to be translated: ') 
word_list = message.split(" ")
output = ""
vowels = "aeiouy"

for word in word_list:
	if word[0] in vowels:
			word = word + 'yay'
	else:
		i = 0

		for letter in word:
			if letter not in vowels:
				word = word + letter
				i += 1 
			else:
				break
		word = word[i:] + "ay "

	output += word + " "
		
print(output)


