# Tic - Tac - Toe
# 1. We need to print a board.
# 2. Take in player input.
# 3. Place their input on the board.
# 4. Check if the game is won,tied, lost, or ongoing.
# 5. Repeat c and d until the game has been won or tied.
# 6. Ask if players want to play again.


#global variables
board = ['','','','','','','','','','']
board_positions = [1,2,3,4,5,6,7,8,9]
playerUsedPositionsDir = {'X': [] , 'O': []}
getPlayer1List =[]
getPlayer2List =[]
unmarkeredpostions = [1,2,3,4,5,6,7,8,9]
winningList = [[7,5,3],[9,5,1],[7,8,9],[4,5,6],[1,2,3],[7,4,1],[8,5,2],[9,6,3]]

# function to print an empty board
def display_board(board):
    print(f'{board[6]} | {board[7]} | {board[8]}')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print(f'{board[0]} | {board[1]} | {board[2]}')

#First player's marker selection
def player_markerTypeSelection():
    markerType = input("Please pick a marker 'X' or 'O'::")
    while ((markerType.upper() !=  'X') and (markerType.upper() != 'O')):
        markerType = input("Please pick only between 'X' or 'O'::")
    return markerType.upper()

#2nd Players default marker selection based on First player's choice
def player2_marker(player1MarkerType):
    player2MarkerType = ''
    if (player1MarkerType =='X'):
        player2MarkerType = 'O'
    else :
        player2MarkerType = 'X'
    return player2MarkerType.upper()

#Show the board again based on current marker positions
def place_marker(position,markerType):
    board[position-1] = markerType
    display_board(board)

#Evaluate is the position chosen by player falls within 1-9 positions and un-used positions
def evaluate_position(position):
    while(position not in (board_positions and unmarkeredpostions)):
        print("not a valid Position, please chose again")
        position = int(input("Choose your Position :: "))
    return position

#Evaluate if the game has a Winner/Tie/Game is still ON
def evaluate_Game(player1Marker,player2Marker):
    getPlayer1List = playerUsedPositionsDir[player1Marker]
    getPlayer2List = playerUsedPositionsDir[player2Marker]
    IsPlayer1winner = findmatch2(winningList,getPlayer1List)
    IsPlayer2winner = findmatch2(winningList,getPlayer2List)
    if (IsPlayer1winner == True and IsPlayer2winner == False):
        print ("PLAYER 1 is WINNER")
        return True
    elif (IsPlayer2winner == True and IsPlayer1winner == False):
        print ("PLAYER 2 is WINNER")
        return True
    elif(IsPlayer1winner == False and IsPlayer2winner == False and len(unmarkeredpostions)==0):
        print ("its a TIE")
        return True
    else:
        print ("game is still on")
        return False

def findmatch(winninglst,playerlst):
    value = False
    for num in winninglst:
        if set(num) in set(playerlst):
            value = True
            break
        else:
            value = False

    return value

def findmatch2(winninglst,playerlst):
    for num in winninglst:
        result =  all(elem in playerlst  for elem in num)
        if result == True:
            break
        else:
            continue
    return result

#Few Pre-set actions to be taken before game start
def game_turn_actions(playerMarker):
    chosenPosition = int(input("Choose your Position :: "))
    evaledPosition = evaluate_position(chosenPosition)

    # Store that position in our directory
    unmarkeredpostions.remove(evaledPosition)
    playerUsedPositionsDir[playerMarker].append(evaledPosition)
    print(playerUsedPositionsDir)
    print(unmarkeredpostions)

    # Show the board now
    place_marker(evaledPosition,playerMarker)


def  tic_tac_toe():
    i = 1
    finalResult = False
    #display the board
    display_board(board_positions)

    #ask 1st player to choose a marker
    player1Marker = player_markerTypeSelection()

    #assign the default player with marker
    player2Marker = player2_marker(player1Marker)

    #revise the assigned markers for clarity
    print("Player 1 is :"+player1Marker+"\n"+"Player 2 is :"+player2Marker)

    while ((i <= 9) and finalResult == False):

        if (i%2 != 0):
            # Player 1' s turn
            game_turn_actions(player1Marker)

            #evaluate
            finalResult = evaluate_Game(player1Marker,player2Marker)

        else:
            #Player 2's turn
            game_turn_actions(player2Marker)

            #evaluate
            finalResult = evaluate_Game(player1Marker,player2Marker)

        i = i+1


tic_tac_toe()