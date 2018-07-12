a=str(input())
v=['a','e','i','o','u','A','E','I','O','U']
if(a>='a' and a<='z') or(a>='A'and a<='Z'):
	if a in v:
		print("Vowel")
	else:
		print("Consonant")
else:
	print("invalid")
