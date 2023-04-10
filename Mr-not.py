from random import *
import os 
u_pwd = input("Enter a password: ")
pwd=['a','b','c','d','e','f','g','h','i','1','2','3','4','5','6']

pw=" "
while(pw!=u_pwd):
	pwd=" "
	for letter in range(len(u_pwd)):
		guess_pwd = pwd[randint(0,17)]
		pw=str(guess_pwd)+str(pw)
		print(pw)
		print("cracking Password...Please    os.system")("cls")
print("Your Password Is :",pw)
		
