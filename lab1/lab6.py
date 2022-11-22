name = input("Give me a word and I'll tell you if it's a palindrome:")

if name[::-1] == name[0:]:
  
	print(name, " is a palindrome")

else:
  
	print(name, " is not a palindrome")
