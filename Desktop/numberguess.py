print("Welcome to guess the number")

number = 10

while True :

	guess = int(raw_input("Enter a guess"));

	if guess < number:
		print "Too Low, guess again"
	elif guess > number:
		print "Too High, guess again"
	elif guess == number:
		print "Correct! Well done"
