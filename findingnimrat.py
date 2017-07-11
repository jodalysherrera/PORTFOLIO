start='''
	You're on a boat that is sinking. In order to survive you have to find Nimrat. 
	Nimrat could be anything depending on how your journey goes.
	'''
	def dead():
		print("(That wasn't an option. You end up drowning because you're indecisive, and achieve the silliest game over. Good job.)")
print(start)
print("Your boat has completely sunk. Do you swim or find a floatation device and stick around?")

print("Type either swim or find")

user_input = input()

if user_input == "find":
	print(" You have successfully found a floatation device and now you're are just chilling in the middle of the ocean. A shark is coming for you. Do you punch it or brace yourself? Type either punch or brace.")

if user_input == "swim":
print("You figure it's best to start swimming and see what you can do. Luckily enough, you start to see something nearby form in the distance...looking closer, you see that it's an island!")
print("It's getting late...you decide that your best options are either building another boat and continuing your journey, or building shelter to stay the night.")
print("(Type either 'build shelter' or 'build boat' to choose.)")
else:
dead()

if swim-1 == input()
if swim-1 == "build boat":
print("You decide to build a boat and continue your journey. Perhaps you'll be lucky enough to find Nimrat...")
elif swim-1 == "build shelter":
print()
print("You decide that it's best to build shelter and make the best of this place. It's can't be THAT bad.")
print("Well, it turns out, it IS that bad. There's no food on the island - or at least, nothing you can grab and eat easily. While searching the island, you find a monkey!")
print("It doesn't seem hostile...but it doesn't look that friendly either. You figure you could take a chance and befriend it...or you could try and knock it out and decide what to do with it later.")
print("(Type either 'befriend it' or 'punch it' to choose.)")
else:
dead()

monkey = input()
#The monkey sucks either way. Just saying. There is no happy ending.
if monkey == "befriend it":
print()
print("Just kidding! Turns out it's a friendly monkey. Seeing that you're not going to hurt it, the monkey runs off.")
print("An hour or so later, the monkey comes back and has a bundle of dark colored fruits!")
print("Actually, you're suspicious. Where did the monkey even get these from? You wonder whether you should eat it or not...")
print("(Type 'eat' or 'don't' to choose.)")
elif monkey == "punch it":
print("Why would you actually punch it? The heck?")
print("Well, congrats, you've ticked it off. The monkey begins to chase you! As you're running you realize...this monkey is Nimrat!")
print("You're scared that, as you're running, you run straight off a cliff and into the ocean!")
print()
print("(Game over. You've found Nimrat - and chose to punch Nimrat in the face. Nice.)")
else:
dead()

eat = input()
#Lol the monkey still sucks
if eat == "don't":
print()
print("The monkey looks offended, and runs away. As it does, you realize...this monkey is Nimrat!")
print("You chase the monkey, but it easily outruns you. You're left in an unfamiliar part of the island, with no sound or food around you...")
print("Eventually, you end up starving to death.")
print()
print("(Game over. You've found Nimrat - but because you didn't trust Nimrat, you died. Nice.")
if eat == "eat":
print()
print("You eat the food the monkey has given you. As you eat and watch the monkey move around, you realize...this monkey is Nimrat!")
print("However, before you can say anything, you start to feel sleepy. You can't find any strength to move or talk.")
print("What kind of person would eat poisionous fruit?? It was dark colored for a reason??")
print("You end up dying of the poison.")
print()
print("(Game over. You've found Nimrat - and even though you trusted Nimrat, it led to your death. Maybe Nimrat is actually something else?")
else:
dead()


swim1 = input()

if swim1=="punch":
	print("You have angered the shark and he ate you. GAME OVER. Type python3 findingnimrat.py to play again!")

elif swim1=="brace": 
	print("OMG the shark is actually a Dolpin!!! You found Nimrat!! Do you befriend him or befriend him??")

swim2 = input()
if swim2=="befriend":
	print("You and Nimrat have become BFFs. Nimrat takes you to shore and saves your life and you live happily ever after :)")
