import time
import random
 
current_strikes = 6
won_games = 0
word_list = ['acres', 'adult', 'advice', 'arrangement', 'attempt', 'August', 'Autumn', 'border', 'breeze', 'brick', 'calm', 'canal', 'Casey']
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
blanks = ['_']

def intro():
	print('   ___\n  |   | You are playing Hangman!\n  |   0\n  |  /|\\\n  |  / \ \n__|__________________________')
	new_game = raw_input('Would you like to play a new game y/n?: ')
	if new_game.lower() == 'yes' or new_game.lower() == 'y':
		get_word()
	else:
		print('It looks like you didn\'t enter y or yes')
		intro()

def get_word():
	global random_word
	random_word = random.choice(word_list)
	print('Welcome, the game has begun!\nGetting a new random word for you...\nYou have won %s games.' % won_games)
	hang_man_track(current_strikes)
	
def player_guess(current_strikes):
	for let in random_word:
		print blanks[0],
	print '\n'
	print ''.join(letters)
	guess = raw_input('You currently have %s strike(s) left before you will be hanged.\nGuess a letter.: ' % current_strikes)
	for letter in letters:
		if guess in letter:
			letters.remove(guess)
	for l in random_word:
		if guess in l:
			blanks.append(guess)
			print('Congrats! You guessed a letter!')
			hang_man_track(current_strikes)
		else:
			print('Sorry, you didn\'t guess a letter. One strike for you!')
			current_strikes -= 1
			hang_man_track(current_strikes)

def hang_man_track(current_strikes):
	time.sleep(1)
	if current_strikes == 6:
		print ('   ___\n  |   | \n  |   \n  |  \n  |    \n__|__________________________')
		player_guess(current_strikes)
	elif current_strikes == 5:
		print ('   ___\n  |   | \n  |   0\n  | \n  |    \n__|__________________________')
		player_guess(current_strikes)
	elif current_strikes == 4:
		print ('   ___\n  |   | \n  |   0\n  |   |\n  |    \n__|__________________________')
		player_guess(current_strikes)	
	elif current_strikes == 3:
		print ('   ___\n  |   | \n  |   0\n  |  /|\n  |    \n__|__________________________')
		player_guess(current_strikes)
	elif current_strikes == 2:
		print ('   ___\n  |   | \n  |   0\n  |  /|\\\n  |    \n__|__________________________')
		player_guess(current_strikes)
	elif current_strikes == 1:
		print ('   ___\n  |   | \n  |   0\n  |  /|\\\n  |  /  \n__|__________________________')
		player_guess(current_strikes)
	elif current_strikes == 0:
		print ('   ___\n  |   | \n  |   0\n  |  /|\\\n  |  / \ \n__|__________________________')
		print('Hangman! You lost..')
		blanks = ['']
		letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
		intro()
intro()
   
   
