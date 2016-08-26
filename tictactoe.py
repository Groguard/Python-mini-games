#board
freespace = ['_',' ']
board = ['_','_','_','_','_','_',' ',' ',' '] 
def current_board():
	print '   a   b   c \n1 _%s_|_%s_|_%s_\n2 _%s_|_%s_|_%s_\n3  %s | %s | %s' % (board[0],board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8])
def player_start():
	who = raw_input('Who will go first? Type X or O.: ')
	if who.upper() == 'X':
		current_board()
		player_x()
	elif who.upper() == 'O':
		current_board()
		player_o()
	else:
		print "You didn't type X or an O, please enter again."
		player_start()
#player X
def player_x():
	move = raw_input('Player X enter the space you want.: ')
	if move == 'a1' and board[0] in freespace:
		board[0] = 'X'
		current_board()
		winner()
		player_o()
	elif move == 'b1' and board[1] in freespace:
		board[1] = 'X'
		current_board()
		winner()
		player_o()
	elif move == 'c1' and board[2] in freespace:
		board[2] = 'X'
		current_board()
		winner()
		player_o()
	elif move == 'a2' and board[3] in freespace:
		board[3] = 'X'
		current_board()
		winner()
		player_o()
	elif move == 'b2' and board[4] in freespace:
		board[4] = 'X'
		current_board()
		winner()
		player_o()
	elif move == 'c2' and board[5] in freespace:
		board[5] = 'X'
		current_board()
		winner()
		player_o()
	elif move == 'a3' and board[6] in freespace:
		board[6] = 'X'
		current_board()
		winner()
		player_o()
	elif move == 'b3' and board[7] in freespace:
		board[7] = 'X'
		current_board()
		winner()
		player_o()
	elif move == 'c3' and board[8] in freespace:
		board[8] = 'X'
		current_board()
		winner()
		player_o()
	else:
		print 'Error, this space is taken or you entered an incorrect space.'
		player_x()
#player O
def player_o():
	move = raw_input('Player O enter the space you want.: ')
	if move == 'a1' and board[0] in freespace:
		board[0] = 'O'
		current_board()
		winner()
		player_x()
	elif move == 'b1' and board[1] in freespace:
		board[1] = 'O'
		current_board()
		winner()
		player_x()
	elif move == 'c1' and board[2] in freespace:
		board[2] = 'O'
		current_board()
		winner()
		player_x()
	elif move == 'a2' and board[3] in freespace:
		board[3] = 'O'
		current_board()
		winner()
		player_x()
	elif move == 'b2' and board[4] in freespace:
		board[4] = 'O'
		current_board()
		winner()
		player_x()
	elif move == 'c2' and board[5] in freespace:
		board[5] = 'O'
		current_board()
		winner()
		player_x()
	elif move == 'a3' and board[6] in freespace:
		board[6] = 'O'
		current_board()
		winner()
		player_x()
	elif move == 'b3' and board[7] in freespace:
		board[7] = 'O'
		current_board()
		winner()
		player_x()
	elif move == 'c3' and board[8] in freespace:
		board[8] = 'O'
		current_board()
		winner()
		player_x()
	else:
		print 'Error, this space is taken or you entered an incorrect space.'
		player_o()
#checks for a winner		
def winner():
    if board[0] == 'X' and board[1] == 'X' and board[2] == 'X' or \
       board[3] == 'X' and board[4] == 'X' and board[5] == 'X' or \
       board[6] == 'X' and board[7] == 'X' and board[8] == 'X' or \
       board[0] == 'X' and board[3] == 'X' and board[6] == 'X' or \
       board[1] == 'X' and board[4] == 'X' and board[7] == 'X' or \
       board[2] == 'X' and board[5] == 'X' and board[8] == 'X' or \
       board[0] == 'X' and board[4] == 'X' and board[8] == 'X' or \
       board[2] == 'X' and board[4] == 'X' and board[6] == 'X':
        current_board()
        print 'Winner is X'
        play_again()
    elif board[0] == 'O' and board[1] == 'O' and board[2] == 'O' or \
         board[3] == 'O' and board[4] == 'O' and board[5] == 'O' or \
         board[6] == 'O' and board[7] == 'O' and board[8] == 'O' or \
         board[0] == 'O' and board[3] == 'O' and board[6] == 'O' or \
         board[1] == 'O' and board[4] == 'O' and board[7] == 'O' or \
         board[2] == 'O' and board[5] == 'O' and board[8] == 'O' or \
         board[0] == 'O' and board[4] == 'O' and board[8] == 'O' or \
         board[2] == 'O' and board[4] == 'O' and board[6] == 'O':
        current_board()
        print 'Winner is O'
        play_again()
    elif board[0] != '_' and board[1] != '_' and board[2] != '_' and \
	     board[3] != '_' and board[4] != '_' and board[5] != '_' and \
		 board[6] != ' ' and board[7] != ' ' and board[8] != ' ':
        current_board()
        print 'This game is a draw.'
        play_again()
#resets the board after every game		
def reset_board():
	board[0] = '_'
	board[1] = '_'
	board[2] = '_'
	board[3] = '_'
	board[4] = '_'
	board[5] = '_'
	board[6] = ' '
	board[7] = ' '
	board[8] = ' '
#asks if you want to play again	and resets the game
def play_again():
	playagain = raw_input('Would you like to play again? Enter Y or N: ')
	
	if playagain.upper() == 'Y':
		reset_board()
		player_start()
	elif playagain.upper() == 'N':
		quit()
	else:
		print "You didn't type Y on N, please try again."
		play_again()
player_start()
