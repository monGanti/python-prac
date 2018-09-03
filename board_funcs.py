
board = ['','','','','','','','','','']
board_positions = [1,2,3,4,5,6,7,8,9]
playerUsedPositionsDir = {'X': [] , 'O': []}
getPlayer1List =[]
getPlayer2List =[]
unmarkeredpostions = [1,2,3,4,5,6,7,8,9]
winningList = [[7,5,3],[9,5,1],[7,8,9],[4,5,6],[1,2,3],[7,4,1],[8,5,2],[9,6,3]]

#printing an empty board
def display_board(board):
    print(f'{board[6]} | {board[7]} | {board[8]}')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print(f'{board[0]} | {board[1]} | {board[2]}')


def player_markerTypeSelection():
    markerType = input("Please pick a marker 'X' or 'O'::")
    while ((markerType.upper() !=  'X') and (markerType.upper() != 'O')):
        markerType = input("Please pick only between 'X' or 'O'::")
    return markerType.upper()

def player2_marker(player1MarkerType):
    player2MarkerType = ''
    if (player1MarkerType =='X'):
        player2MarkerType = 'O'
    else :
        player2MarkerType = 'X'
    return player2MarkerType.upper()

def choose_position(board_positions,playerUsedPositionsDir):
    position = int(input("Choose your Position :: "))
    if position not in board_positions:
        return "not a valid value, please make your choice only between 1-9"
    elif position in playerUsedPositionsDir.values():
        print( "this position already has a marker, choose another position" )
        position = int(input("Choose your Position :: "))
        return position
    else:
        return position

def place_marker(position,markerType):
    board[position-1] = markerType
    display_board(board)

def evaluate_Game(playerUsedPositionsDir,player1Marker,player2Marker):
    getPlayer1List = playerUsedPositionsDir[player1Marker]
    getPlayer2List = playerUsedPositionsDir[player2Marker]
    IsPlayer1winner = findmatch(winningList,getPlayer1List)
    IsPlayer2winner = findmatch(winningList,getPlayer2List)
    if (IsPlayer1winner == True and IsPlayer2winner == False):
        return ("PLAYER 1 is WINNER")
    elif (IsPlayer2winner == True and IsPlayer1winner == False):
        return ("PLAYER 2 is WINNER")
    elif(IsPlayer1winner == False and IsPlayer2winner == False and len(unmarkeredpostions)==1):
        return ("its a TIE")
    else:
        return ("game is still on")

def findmatch(nestedList1,list2):
    #value = []
    for num in nestedList1:
        #value = set(num + list2)
        if list2 in num:
            return True
        else:
            continue
    return False




#display the board
display_board(board_positions)

#ask 1st player to choose a marker
player1Marker = player_markerTypeSelection()

#assign the default player with marker
player2Marker = player2_marker(player1Marker)

#revise the assigned markers for clarity
print("Player 1 is :"+player1Marker+"\n"+"Player 2 is :"+player2Marker)

#########
#Game turn 1 : Take position from player1
positionIs = choose_position(board_positions,playerUsedPositionsDir)

# Store that position in our directory
unmarkeredpostions.remove(positionIs)
playerUsedPositionsDir[player1Marker].append(positionIs)
print(playerUsedPositionsDir)
print(unmarkeredpostions)

# Show the board now
place_marker(positionIs,player1Marker)

#########
#Game turn 2 : Take position from player2
positionIs = choose_position(board_positions,playerUsedPositionsDir)

# Store that position in our directory
unmarkeredpostions.remove(positionIs)
playerUsedPositionsDir[player2Marker].append(positionIs)
print(playerUsedPositionsDir)
print(unmarkeredpostions)

# Show the board now
place_marker(positionIs,player2Marker)

#########
#Game turn 3 : Take position from player1
positionIs = choose_position(board_positions,playerUsedPositionsDir)

# Store that position in our directory
unmarkeredpostions.remove(positionIs)
playerUsedPositionsDir[player1Marker].append(positionIs)
print(playerUsedPositionsDir)
print(unmarkeredpostions)

# Show the board now
place_marker(positionIs,player1Marker)

#evaluate
value = evaluate_Game(playerUsedPositionsDir,player1Marker,player2Marker)

#########
#Game turn 4 : Take position from player2
positionIs = choose_position(board_positions,playerUsedPositionsDir)

# Store that position in our directory
unmarkeredpostions.remove(positionIs)
playerUsedPositionsDir[player2Marker].append(positionIs)
print(playerUsedPositionsDir)
print(unmarkeredpostions)

# Show the board now
place_marker(positionIs,player2Marker)

#evaluate
value = evaluate_Game(playerUsedPositionsDir,player1Marker,player2Marker)

#########
#Game turn 5: Take position from player1
positionIs = choose_position(board_positions,playerUsedPositionsDir)

# Store that position in our directory
unmarkeredpostions.remove(positionIs)
playerUsedPositionsDir[player1Marker].append(positionIs)
print(playerUsedPositionsDir)
print(unmarkeredpostions)

# Show the board now
place_marker(positionIs,player1Marker)

#evaluate
value = evaluate_Game(playerUsedPositionsDir,player1Marker,player2Marker)
print(value)

#########
#Game turn 6 : Take position from player2
positionIs = choose_position(board_positions,playerUsedPositionsDir)

# Store that position in our directory
unmarkeredpostions.remove(positionIs)
playerUsedPositionsDir[player2Marker].append(positionIs)
print(playerUsedPositionsDir)
print(unmarkeredpostions)

# Show the board now
place_marker(positionIs,player2Marker)

#evaluate
value = evaluate_Game(playerUsedPositionsDir,player1Marker,player2Marker)
print(value)

#########
#Game turn 7: Take position from player1
positionIs = choose_position(board_positions,playerUsedPositionsDir)

# Store that position in our directory
unmarkeredpostions.remove(positionIs)
playerUsedPositionsDir[player1Marker].append(positionIs)
print(playerUsedPositionsDir)
print(unmarkeredpostions)

# Show the board now
place_marker(positionIs,player1Marker)

#evaluate
value = evaluate_Game(playerUsedPositionsDir,player1Marker,player2Marker)
print(value)

#########
#Game turn 8 : Take position from player2
positionIs = choose_position(board_positions,playerUsedPositionsDir)

# Store that position in our directory
unmarkeredpostions.remove(positionIs)
playerUsedPositionsDir[player2Marker].append(positionIs)
print(playerUsedPositionsDir)
print(unmarkeredpostions)

# Show the board now
place_marker(positionIs,player2Marker)

#evaluate
value = evaluate_Game(playerUsedPositionsDir,player1Marker,player2Marker)
print(value)





