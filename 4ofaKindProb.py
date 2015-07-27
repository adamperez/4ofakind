from random import randrange

def dealer():
	deck = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']*4
	cards = []
	i = 0

	while i != 5:
		x = randrange(0,len(deck))
		cards.append(deck[x])
		i = i + 1

	#decklen = len(deck)
	#print(decklen)

	return cards

def stats(countOfHands,FourOfAKinds):
	probability = FourOfAKinds / countOfHands

	print("Number of hands dealt: ",countOfHands)
	print("Four of a Kind's Seen: ",FourOfAKinds)
	print("Probability of Four of a Kind: ",probability*100)
	print('\n')

def matchCheck(dealtCards):
	matched = False	# flag
	i = 0			# count

	while matched != True:
		if i == 5:
			break	# break out of hand, max of 5 cards per hand
		if dealtCards.count(dealtCards[i]) == 4:
			# if card at hand[i] appears 4 times
			matched = True
		else:
			# try again
			i = i + 1

	return matched

def main():
	print("4 of a Kind Probability")
	print("Dealing 1 million hands of 5 card poker")
	hand = [[]]*1000000	# creates list of different hands
	#print(hand)
	probcount = 0		# counts times for probability (factor as assignment stated)
	counter = 0			# total count of hands dealt
	FourOfAKindCount = 0# count of time a four of a kind is found
	# print(hand)
	while counter != 1000000:	# havent made 1m hands yet!
		hand[counter] = dealer()
		if matchCheck(hand[counter]) == True:	# if there is a 4 of a kind present, add to counter
			FourOfAKindCount = FourOfAKindCount + 1
		counter = counter + 1
		probcount = probcount + 1
		if probcount == 10000:	# 10k deals is a stopping point to calcualte stats of program
			stats(counter,FourOfAKindCount)
			probcount = 0
	#print(hand)


main()