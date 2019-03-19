import random

number = random.randint(1000,9999)

#print(number) #For testing
 
guesses = 0

print("Cows means no. of correct digits in the right place")

print("Bulls means no. of correct digits in the wrong place")

print("Make guesses of 4 digits")

while(True):

	guess = int(input('Type your guess: '))

	numList = [int(d) for d in str(number)]

	guessList = [int(d) for d in str(guess)]

	cows = []

	for i in range (4):

		if numList[i] == guessList[i]:

			cows.append(numList[i])

	cowsNo = len(cows)

	leftovers = [x for x in guessList if x not in cows] #leftover guesses

	bulls = [x for x in numList if x in leftovers ]

	cowsNo = len(cows)

	bullsNo = len(bulls)

	print(f"Cows: {cowsNo}, Bulls: {bullsNo}")

	if cowsNo == 4:

		print ( f"Congratulations! you guessed {number} with {guesses} guesses")

		break



	guesses += 1


