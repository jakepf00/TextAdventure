print
def title():
	print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print ("Welcome to the Mountain of Mysteriousness")
	print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print ("~~~By~J~Cornelius~Fifelolz~~~~~~~~~~~~~~~")
title()

print
name = raw_input("What is your name? ")
if name == "Jacob": 
	print ("Jacob you're awesome")
elif name == "Jake":
	print ("Jake, that's a pretty cool name.")
else: 
	print (name + ", what a crappy name")

print
print ("Anyway...")
type = raw_input("Are you a knight, wizard, or a troll? ")
if type == "knight":
	a, d, h = 6, 4, 50
elif type == "wizard":
	a, d, h = 8, 1, 40
elif type == "troll":
	a, d, h = 5, 4, 45
else:
	print ("Wow. Just wow.")
print ("sir " + name + " the " + type + ", are you ready for adventure?")
