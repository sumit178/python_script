import random

num=random.randint(1,20)

	
for b in range(1,6):
    s=int(input("enter your number: "))
	if s < num:
		print( "\nu have chosen lesser number")
	elif s > num:
		print( "\nu have chosen greater number")
	else:
		break
if num==s:
	print("^_^ u won ^_^")
else:
	print( "loss")				

