#Initialize Array
#tile = 'abc'
#x = [[tile for i in range(10)] for j in range(10)]
"""
tile001 = {'Name': 'tile001', 'Filled': 'false', 'Played': 'false', 'exits': ['left','right','top','bottom']};
tile002 = {'Name': 'tile002', 'Filled': 'false', 'Played': 'false', 'exits': ['left','right']};
tile003 = {'Name': 'tile003', 'Filled': 'false', 'Played': 'false', 'exits': ['top','bottom']};
tile004 = {'Name': 'tile004', 'Filled': 'false', 'Played': 'false', 'exits': ['right','top']};
tile005 = {'Name': 'tile005', 'Filled': 'false', 'Played': 'false', 'exits': ['left','bottom']};

print "tile001['Name']: ", tile001['Name'];
print "tile001['Filled']: ", tile001['Filled'];
print "tile001['Played']: ", tile001['Played'];
print "tile001['exits']: ", tile001['exits'];"""

from collections import defaultdict
tileset = defaultdict(dict)

#Create the tiles as an array of dictionaries:
tileset['tile001']['title'] = 'tile001'
tileset['tile001']['played'] = 'false'
tileset['tile001']['filled'] = 'false'
tileset['tile001']['exits'] = ['left','right','up','down']

tileset['tile002']['title'] = 'tile002'
tileset['tile002']['played'] = 'false'
tileset['tile002']['filled'] = 'false'
tileset['tile002']['exits'] = ['up','down']

tileset['tile003']['title'] = 'tile003'
tileset['tile003']['played'] = 'false'
tileset['tile003']['filled'] = 'false'
tileset['tile003']['exits'] = ['left','right']

tileset['tile004']['title'] = 'tile004'
tileset['tile004']['played'] = 'false'
tileset['tile004']['filled'] = 'false'
tileset['tile004']['exits'] = ['left','down']

#Once created, they can be accessed like this:
"""print tileset['tile001']
print tileset['tile002']
print tileset['tile003']
print tileset['tile004']
print tileset['tile001']['exits']
print tileset['tile002']['filled']"""

board = []
hiddenboard = []

for x in range(0,12):
    board.append(["O"] * 12) #adds 5 'O's to each row in list board[]
    hiddenboard.append(["O     0"] * 12) #adds 5 'O's to each row in list board[]
 
def print_board(board):
    for row in board:       #for loop puts the rows in a grid format
        print " ".join(row)

# gets x,y coords of a given tile.
def find_tile(target_tile):
	x = 0
	for str in hiddenboard:
		x += 1
		if target_tile in str:
			column_found = (str.index("tile001") + 1)
			row_found = x
			print "%s found at column : %s" % (target_tile, column_found)
			print "%s found at row : %s" % (target_tile, row_found)

def find_coord(x,y):
	x -= 1
	y -= 1
	print hiddenboard[x][y]

def play_tile(current_tile):
	target_row = input("Target Row:")-1
	target_col = input("Target Col:")-1
	#Mark an X on the visible board for where the user played:
	board[target_row][target_col] = "X" # the title for the tile played is added to grid at the target location. 
	hiddenboard[target_row][target_col] = current_tile
	tileset[current_tile]['played'] = 'true' # mark the tile as played.

Finished = False

while Finished == False:
	print " \n \n \n Visible"
	print_board(board)
	print " \n \n \n Hidden"
	print_board(hiddenboard)
	Finished = True

current_tile = tileset['tile001']['title']  # later this will rotate as the tiles pop off the stack
play_tile(current_tile)

current_tile = tileset['tile002']['title'] # Set the next tile as active

print " \n \n \n Visible"
print_board(board)
print " \n \n \n Hidden"
print_board(hiddenboard)


target_tile = "tile001"
find_tile(target_tile)
print tileset[target_tile]

find_coord(3,3)