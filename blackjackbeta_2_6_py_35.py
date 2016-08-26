import random
import sys
import os


def clear():
	if sys.platform == 'linux':
		os.system('clear')
	elif sys.platform == 'win32':
		os.system('cls')
	else:
		pass
	
	
#Builds the deck
suit = ['Spades', 'Hearts', 'Diamonds','Clubs']
rank = ['Ace','King','Queen','Jack',10,9,8,7,6,5,4,3,2]
deck = ['%s of %s' % (r,s) for r in rank for s in suit]

#Dictionary to compare text to int value
card_value = {'Ace':1, '2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'Jack':10,'Queen':10,'King':10}

#Player coins
coins = 100

#Full text values for cards
player_hand = []
dealer_hand = []

#Standalone text score value for cards
player_value = []
dealer_value = []

#Standalone int values for cards
player_card_int = []
deal_card_int = []


class the_deck:

	def __init__(self):
		self.betting()
		
	def deal(self):
		global crd, d_crd
		
		crd = random.sample(deck,2)
		deck.remove(crd[0])
		deck.remove(crd[1])
		player_hand.append(crd[0])
		player_hand.append(crd[1])
		
		d_crd = random.sample(deck,2)
		deck.remove(d_crd[0])
		deck.remove(d_crd[1])
		dealer_hand.append(d_crd[0])
		dealer_hand.append(d_crd[1])
		
		self.hand_track()
		print ('You drew the %s and the %s. Your hand total is %s \nThe Dealer is showing the %s' % (crd[0],crd[1], sum,d_crd[0]))
		self.check1()
		self.hit_stay()
	def split_hand():
		pass
		
	def dbl_down():
		pass
		
		
	def hit_stay(self):
		user_hit_stay = input('Would you like the hit or stay? Type [H]it or [S]tay to continue.: ')
		if user_hit_stay.lower() == 'h':
			self.hit()
			
			
		elif user_hit_stay.lower() == 's':
			print ('The dealer turns over his hidden card to reveal a %s' % (dealer_hand[1]))
			self.dealer_turn()
			
	
		else:
			print ('It looks like you didn\'t type h or s')
			self.hit_stay()
			
	def dealer_turn(self):
		if int(sum1) < 17:
			d_draw1 = random.choice(deck)
			dealer_hand.append(d_draw1)
			deck.remove(d_draw1)
			print ('Dealer drew a %s' % (d_draw1))
			del player_value[:]
			del player_card_int[:]
			del deal_card_int[:]
			del dealer_value[:]
			self.hand_track()
			self.checkbust()
			self.dealer_turn()
		elif int(sum1) >= 17:
			self.checkfinal()
		else:
			print ('That was outright wrong!')


		
	def hit(self):
		global new_crd
		new_crd = random.choice(deck)
		
		deck.remove(new_crd)
		player_hand.append(new_crd)
		
		#removes the previous values in the list and runs hands track to get the most current values of the hand
		del player_value[:]
		del player_card_int[:]
		del deal_card_int[:]
		del dealer_value[:]
		
		
		self.hand_track()
		print ('You drew %s. Your Hand total is %d' %(new_crd, sum))
		self.checkbust()
		
		self.hit_stay()
		

	def hand_track(self):
		for i,card in enumerate(player_hand):
			v_crd1 = player_hand[i].split(' of')[0]
			player_value.append(v_crd1)
			
		for j,dcard in enumerate(dealer_hand):
			v_dcrd1 = dealer_hand[j].split(' of')[0]
			dealer_value.append(v_dcrd1)
			
		self.get_value()
	
	def get_value(self):
		global sum
		global sum1
		
		sum = 0
		sum1 = 0
		
		for key in player_value:
			player_card_int.append(card_value[key])
			
			

		for num in player_card_int:
			sum += num
			
		if 'Ace' in player_value and sum < 12:
			sum += 10
			
		#Dealer get_value		
		for key1 in dealer_value:
			deal_card_int.append(card_value[key1])
		
		for num1 in deal_card_int:
			sum1 += num1
			
		if 'Ace' in dealer_value and sum1 < 12:
			sum1 += 10
				
	def checkbust(self):
		global coins
		global bet
		if sum1 > 21:
			print ('The Dealer busted with %d, you win!' % (sum1))
			coins = coins + (int(bet)*2)
			print ('You won %d coins! You now have a total of %d coins.' % (int(bet), int(coins)))
			bet = 0
			self.reset()
		
		elif sum > 21:
			print ('You busted, Dealer wins.')
			
			
			print ('You lost %d coins. You now have a total of %d coins.' % (int(bet), int(coins)))
			bet = 0
			self.reset()

			
	def checkfinal(self):
		global coins
		global bet
		if int(sum1) > int(sum) and sum1 <= 21:
			print ('Dealer Wins with %d!' % (sum1))
			print ('You lost %d coins. You now have a total of %d coins.' % (int(bet), int(coins)))
			bet = 0
			self.reset()

		elif int(sum) > int(sum1) and int(sum) <= 21:
			print ('You Win!')
			coins = int(coins) + (int(bet)*2)
			print ('You won %d coins! You now have a total of %d coins.' % (int(bet), int(coins)))
			bet = 0
			self.reset()
		elif int(sum) == int(sum1):
			print ('You and the dealer have tied. -Push')
			coins = int(coins) + int(bet)
			print ('You get your %d coin bet back. You now have a total of %d coins.' % (int(bet), int(coins)))
			bet = 0
			self.reset()
	def check1(self):
		global coins
		global bet
		if int(sum1) == 21:
			print ('The dealer reveals his hidden card the %s' % (dealer_hand[1]))
			print ('Dealer has Blackjack!')
			print ('You lost %d coins. You now have a total of %d coins.' % (int(bet), int(coins)))
			bet = 0
			self.reset()
		#minus from bankroll
		#deal again
		
		if int(sum) == 21:
			print ('You have Blackjack!')
			coins = int(coins) + (int(bet)*2)
			print ('You won %d coins! You now have a total of %d coins.' % (int(bet), int(coins)))
			bet = 0
			self.reset()
		#plus bet to bankroll
	
	def betting(self):
		global coins
		global bet
		if len(deck) < 18:
			self.shuffle()
		elif coins == 0:
				self.no_coins()
		else:
			try: 
				bet = input('\n\nHow much would you like to bet? You currently have %d coins.: ' % (coins))
			except:
				print ('It looks like you did not enter a number. Stop being a jackass!! Try again...')
				self.betting()
			if int(bet) > int(coins):
				print ('You dont have that many coins! Try again...')
				self.betting()
			else:
				coins = int(coins) - int(bet)
				print ('You bet %d coins.' % (int(bet)))
				self.deal()
	
	def reset(self):
		user_reset = input('Would you like to play again? Y/N: ') 
	
		if user_reset.upper() == 'Y':
			clear()
			del player_hand[:]
			del dealer_hand[:]
			del player_value[:]
			del dealer_value[:]
			del player_card_int[:]
			del deal_card_int[:]
			print ('Dealing a new hand!')
			self.betting()
		elif user_reset.upper() == 'N':
			print ('Closing the game will reset your coins.')
			A = input('Are you sure you want to close? Y/N: ')
			if A.lower() == 'y':
				exit()
			elif A.lower() == 'n':
				self.reset()
			else:
				print ('It looks like you didn\'t enter Y/N')
				self.reset()
		else:
			print ('It looks like you didn\'t enter Y/N')
			self.reset()
			
	def shuffle(self):
		global deck
		print ('\n\nAlmost out of cards')
		print ('Shuffling the deck')
		deck = ['%s of %s' % (r,s) for r in rank for s in suit]
		self.betting()
		
	def no_coins(self):
		global coins
		print ('\n\nYou have no more coins.')
		nocoin_reset = input('Would like you like to reset your coins or quit?\nType R for reset or Q for quit.: ')
		if nocoin_reset.upper() == 'R':
			coins = 100
			print ('Your coins have been reset. You now have %d coins' % (coins))
			self.betting()
		elif nocoin_reset.upper() == 'Q':
			exit()
		else:
			print ('It looks like you didn\'t type R or Q. Try again.')
			self.no_coins()
chosecard = the_deck()


	
	
	#todo extras

	# - check for a split
	# - double down feature
	# - multiple players
	
	
	
	
	
	
