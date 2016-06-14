# Dictionary with Key = Position and Value = X , O or empty space

theBoard = {'TL': ' ', 'TM': ' ', 'TR': ' ', 'ML': ' ', 'MM': ' ', 'MR': ' ', 'BL': ' ', 'BM': ' ', 'BR': ' '}

# Dictionary that contains 'No' until the game is over, in which case it will change to 'Yes'

over = {'Check' : 'No'}
Xcount = 0
Ocount = 0
GameOver = False



# Function that detects when TicBot is near defeat and acts accordingly

while GameOver == False:
    
    # Function that prints the updated GUI

    def play(theBoard):
        print('')
        print(theBoard['TL'] + '|' + theBoard['TM'] + '|' + theBoard['TR'])
        print ('-----')
        print(theBoard['ML'] + '|' + theBoard['MM'] + '|' + theBoard['MR'])
        print ('-----')
        print(theBoard['BL'] + '|' + theBoard['BM'] + '|' + theBoard['BR'])
        print('')
        
    def nearLoss(theBoard):
        
        global Ocount
        
        # Top loss
        if theBoard['TL'] == 'X' and theBoard['TM'] == 'X' and Ocount < Xcount:
            if theBoard['TR'] == ' ':
                theBoard['TR'] = 'O'
                Ocount = Ocount + 1
        elif theBoard['TM'] == 'X' and theBoard['TR'] == 'X' and Ocount < Xcount:
            if theBoard['TL'] == ' ':
                theBoard['TL'] = 'O'
                Ocount = Ocount + 1
        elif theBoard['TL'] == 'X' and theBoard['TR'] == 'X' and Ocount < Xcount:
            if theBoard['TM'] == ' ':
                theBoard['TM'] = 'O'
                Ocount = Ocount + 1
        

        # Mid loss 1
        if theBoard['ML'] == 'X' and theBoard['MM'] == 'X' and theBoard['MR'] == ' ' and Ocount < Xcount:
            theBoard['MR'] = 'O'
            Ocount = Ocount + 1
        elif theBoard['MM'] == 'X' and theBoard['MR'] == 'X' and theBoard['ML'] == ' ' and Ocount < Xcount:
            theBoard['ML'] = 'O'
            Ocount = Ocount + 1
        elif theBoard['ML'] == 'X' and theBoard['MR'] == 'X' and theBoard['MM'] == ' ' and Ocount < Xcount:
            theBoard['MM'] = 'O'
            Ocount = Ocount + 1

        # Bot loss
        if theBoard['BL'] == 'X' and theBoard['BM'] == 'X' and theBoard['BR'] == ' 'and Ocount < Xcount:
            theBoard['BR'] = 'O'
            Ocount = Ocount + 1
        elif theBoard['BM'] == 'X' and theBoard['BR'] == 'X' and theBoard['BL'] == ' 'and Ocount < Xcount:
            theBoard['BL'] = 'O'
            Ocount = Ocount + 1
        elif theBoard['BL'] == 'X' and theBoard['BR'] == 'X' and theBoard['BM'] == ' 'and Ocount < Xcount:
            theBoard['BM'] = 'O'
            Ocount = Ocount + 1

        # Left loss
        if theBoard['TL'] == 'X' and theBoard['ML'] == 'X' and theBoard['BL'] == ' ' and Ocount < Xcount:
            theBoard['BL'] = 'O'
            Ocount = Ocount + 1
        elif theBoard['ML'] == 'X' and theBoard['BL'] == 'X' and theBoard['TL'] == ' 'and Ocount < Xcount:
            theBoard['TL'] = 'O'
            Ocount = Ocount + 1
        elif theBoard['TL'] == 'X' and theBoard['BL'] == 'X' and theBoard['ML'] == ' 'and Ocount < Xcount:
            theBoard['ML'] = 'O'
            Ocount = Ocount + 1

        # Mid loss 2
        if theBoard['TM'] == 'X' and theBoard['MM'] == 'X' and theBoard['BM'] == ' ' and Ocount < Xcount:
            theBoard['BM'] = 'O'
            Ocount = Ocount + 1
        elif theBoard['MM'] == 'X' and theBoard['BM'] == 'X' and theBoard['TM'] == ' ' and Ocount < Xcount:
            theBoard['TM'] = 'O'
            Ocount = Ocount + 1
        elif theBoard['TM'] == 'X' and theBoard['BM'] == 'X' and theBoard['MM'] == ' ' and Ocount < Xcount:
            theBoard['MM'] = 'O'
            Ocount = Ocount + 1

        # Right loss
        if theBoard['TR'] == 'X' and theBoard['MR'] == 'X' and theBoard['BR'] == ' ' and Ocount < Xcount:
            theBoard['BR'] = 'O'
            Ocount = Ocount + 1
        elif theBoard['MR'] == 'X' and theBoard['BR'] == 'X' and theBoard['TR'] == ' ' and Ocount < Xcount:
            theBoard['TR'] = 'O'
            Ocount = Ocount + 1
        elif theBoard['TR'] == 'X' and theBoard['BR'] == 'X' and theBoard['MR'] == ' ' and Ocount < Xcount:
            theBoard['MR'] = 'O'
            Ocount = Ocount + 1

        # Diagnol loss 1
        if theBoard['TL'] == 'X' and theBoard['MM'] == 'X' and theBoard['BR'] == ' ' and Ocount < Xcount:
            theBoard['BR'] = 'O'
            Ocount = Ocount + 1
        elif theBoard['BR'] == 'X' and theBoard['MM'] == 'X' and theBoard['TL'] == ' ' and Ocount < Xcount:
            theBoard['TL'] = 'O'
            Ocount = Ocount + 1
        elif theBoard['TL'] == 'X' and theBoard['BR'] == 'X' and theBoard['MM'] == ' ' and Ocount < Xcount:
            theBoard['MM'] = 'O'
            Ocount = Ocount + 1
            
        # Diagnol loss 2
        elif theBoard['TR'] == 'X' and theBoard['MM'] == 'X' and theBoard['BL'] == ' '  and Ocount < Xcount:
            theBoard['BL'] = 'O'
            Ocount = Ocount + 1
        elif theBoard['TR'] == 'X' and theBoard['BL'] == 'X' and theBoard['MM'] == ' '  and Ocount < Xcount:
            theBoard['MM'] = 'O'
            Ocount = Ocount + 1
        elif theBoard['BL'] == 'X' and theBoard['MM'] == 'X' and theBoard['TR'] == ' '  and Ocount < Xcount:
            theBoard['TR'] = 'O'
            Ocount = Ocount + 1


    # Function that detects when TicBot is near victory and acts accordingly

    def nearWin(theBoard):
        
        global Ocount
        
        # Top win
        if theBoard['TL'] == 'O' and theBoard['TM'] == 'O' and Ocount < Xcount:
            if theBoard['TR'] == ' ':
                theBoard['TR'] = 'O'
                Ocount = Ocount + 1
        elif theBoard['TM'] == 'O' and theBoard['TR'] == 'O' and Ocount < Xcount:
            if theBoard['TL'] == ' ':
                theBoard['TL'] = 'O'
                Ocount = Ocount + 1
        elif theBoard['TL'] == 'O' and theBoard['TR'] == 'O' and Ocount < Xcount:
            if theBoard['TM'] == ' ':
                theBoard['TM'] = 'O'
                Ocount = Ocount + 1

        # Mid win 1
        if theBoard['ML'] == 'O' and theBoard['MM'] == 'O' and Ocount < Xcount:
            if theBoard['MR'] == ' ':
                theBoard['MR'] = 'O'
                Ocount = Ocount + 1
        elif theBoard['MM'] == 'O' and theBoard['MR'] == 'O' and Ocount < Xcount:
            if theBoard['ML'] == ' ':
                theBoard['ML'] = 'O'
                Ocount = Ocount + 1
        elif theBoard['ML'] == 'O' and theBoard['MR'] == 'O' and Ocount < Xcount:
            if theBoard['MM'] == ' ':
                theBoard['MM'] = 'O'
                Ocount = Ocount + 1

        # Bot win
        if theBoard['BL'] == 'O' and theBoard['BM'] == 'O' and Ocount < Xcount:
            if theBoard['BR'] == ' ':
                theBoard['BR'] = 'O'
                Ocount = Ocount + 1
        elif theBoard['BM'] == 'O' and theBoard['BR'] == 'O' and Ocount < Xcount:
            if theBoard['BL'] == ' ':
                theBoard['BL'] = 'O'
                Ocount = Ocount + 1
        elif theBoard['BL'] == 'O' and theBoard['BR'] == 'O' and Ocount < Xcount:
            if theBoard['BM'] == ' ':
                theBoard['BM'] = 'O'
                Ocount = Ocount + 1

        # Left win
        if theBoard['TL'] == 'O' and theBoard['ML'] == 'O' and Ocount < Xcount:
            if theBoard['BL'] == ' ':
                theBoard['BL'] = 'O'
                Ocount = Ocount + 1
        elif theBoard['ML'] == 'O' and theBoard['BL'] == 'O' and Ocount < Xcount:
            if theBoard['TL'] == ' ':
                theBoard['TL'] = 'O'
                Ocount = Ocount + 1
        elif theBoard['TL'] == 'O' and theBoard['BL'] == 'O' and Ocount < Xcount:
            if theBoard['ML'] == ' ':
                theBoard['ML'] = 'O'
                Ocount = Ocount + 1

        # Mid win 2
        if theBoard['TM'] == 'O' and theBoard['MM'] == 'O' and Ocount < Xcount:
            if theBoard['BM'] == ' ':
                theBoard['BM'] = 'O'
                Ocount = Ocount + 1
        elif theBoard['MM'] == 'O' and theBoard['BM'] == 'O' and Ocount < Xcount:
            if theBoard['TM'] == ' ':
                theBoard['TM'] = 'O'
                Ocount = Ocount + 1
        elif theBoard['TM'] == 'O' and theBoard['BM'] == 'O' and Ocount < Xcount:
            if theBoard['MM'] == ' ':
                theBoard['MM'] = 'O'
                Ocount = Ocount + 1

        # Right win
        if theBoard['TR'] == 'O' and theBoard['MR'] == 'O' and Ocount < Xcount:
            if theBoard['BR'] == ' ':
                theBoard['BR'] = 'O'
                Ocount = Ocount + 1
        elif theBoard['MR'] == 'O' and theBoard['BR'] == 'O' and Ocount < Xcount:
            if theBoard['TR'] == ' ':
                theBoard['TR'] = 'O'
                Ocount = Ocount + 1
        elif theBoard['TR'] == 'O' and theBoard['BR'] == 'O' and Ocount < Xcount:
            if theBoard['MR'] == ' ':
                theBoard['MR'] = 'O'
                Ocount = Ocount + 1

        # Diagnol win 1
        if theBoard['TL'] == 'O' and theBoard['MM'] == 'O' and Ocount < Xcount:
            if theBoard['BR'] == ' ':
                theBoard['BR'] = 'O'
                Ocount = Ocount + 1
        elif theBoard['BR'] == 'O' and theBoard['MM'] == 'O' and Ocount < Xcount:
            if theBoard['TL'] == ' ':
                theBoard['TL'] = 'O'
                Ocount = Ocount + 1
        elif theBoard['TL'] == 'O' and theBoard['BR'] == 'O' and Ocount < Xcount:
            if theBoard['MM'] == ' ':
                theBoard['MM'] = 'O'
                Ocount = Ocount + 1
            
        # Diagnol win 2
        if theBoard['TR'] == 'O' and theBoard['MM'] == 'O' and Ocount < Xcount:
            if theBoard['BL'] == ' ':
                theBoard['BL'] = 'O'
                Ocount = Ocount + 1
        elif theBoard['TR'] == 'O' and theBoard['BL'] == 'O' and Ocount < Xcount:
            if theBoard['MM'] == ' ':
                theBoard['MM'] = 'O'
                Ocount = Ocount + 1
        elif theBoard['BL'] == 'O' and theBoard['MM'] == 'O' and Ocount < Xcount:
            if theBoard['TR'] == ' ':
                theBoard['TR'] = 'O'
                Ocount = Ocount + 1

    # Function that detects when player has made a move that is not of immediate threat to TicBot and acts accordingly based on future threat            
            
    def checknoob(theBoard):
        
        global Ocount
        
        # O Center X diagnol play 1
        if theBoard['TR'] == 'X' and theBoard['BL'] == 'X' and theBoard['MM'] == 'O' and Xcount < 3 and Ocount < Xcount:
            theBoard['TM'] = 'O'
            Ocount = Ocount + 1
                
        # O Center X diagnol play 2
        elif theBoard['BR'] == 'X' and theBoard['TL'] == 'X' and theBoard['MM'] == 'O' and Xcount < 3 and Ocount < Xcount:
            theBoard['TM'] = 'O'
            Ocount = Ocount + 1

        # O Left X diagnol play 
        elif theBoard['MM'] == 'X' and theBoard['TL'] == 'O' and theBoard['BR'] == 'X' and Xcount < 4 and Ocount < Xcount:
            theBoard['TR'] = 'O'
            Ocount = Ocount + 1
            
        # O Center X topbot play
        elif theBoard['MM'] == 'O' and theBoard['TM'] == 'X' and theBoard['BM'] == 'X' and Xcount < 3 and Ocount < Xcount:
            theBoard['ML'] = 'O'
            Ocount = Ocount + 1
            
        # O Center X topbot play continued
        elif theBoard['MM'] == 'O' and theBoard['TM'] == 'X' and theBoard['BM'] == 'X' and theBoard['MR'] == 'X' and theBoard['ML'] == 'O' and Xcount < 4 and Ocount < Xcount:
            theBoard['BR'] = 'O'
            Ocount = Ocount + 1
            
        # O Center X leftright play 
        elif theBoard['MM'] == 'O' and theBoard['ML'] == 'X' and theBoard['MR'] == 'X' and Xcount < 3 and Ocount < Xcount:
            theBoard['TM'] = 'O'
            Ocount = Ocount + 1

        # O Center X leftright play continued
        elif theBoard['MM'] == 'O' and theBoard['ML'] == 'X' and theBoard['MR'] == 'X' and theBoard['BM'] == 'X' and Xcount < 4 and Ocount < Xcount:
            theBoard['BR'] = 'O'
            Ocount = Ocount + 1
            
        # Center O oddplay ML + TM
        elif theBoard['MM'] == 'O' and theBoard['ML'] == 'X' and theBoard['TM'] == 'X' and Xcount < 3 and Ocount < Xcount:
            if theBoard['TL'] == ' ':
                theBoard['TL'] = 'O'
                Ocount = Ocount + 1
                
        # Center O oddplay ML + TR      
        elif theBoard['MM'] == 'O' and theBoard['ML'] == 'X' and theBoard['TR'] == 'X' and Ocount < Xcount:
            if Xcount < 3 and theBoard['BM'] == ' ':
                theBoard['BM'] = 'O'
                Ocount = Ocount + 1

        # Center O oddplay ML + BM
        elif theBoard['MM'] == 'O' and theBoard['ML'] == 'X' and theBoard['BM'] == 'X' and Xcount < 3 and Ocount < Xcount:
            if theBoard['TL'] == ' ':
                theBoard['TL'] = 'O'
                Ocount = Ocount + 1
                
        # Center O oddplay ML + BR       
        elif theBoard['MM'] == 'O' and theBoard['ML'] == 'X' and theBoard['BR'] == 'X' and Ocount < Xcount:
            if Xcount < 4 and theBoard['BL'] == ' ':
                theBoard['BL'] = 'O'
                Ocount = Ocount + 1

        # Center O oddplay MR + TM
        elif theBoard['MM'] == 'O' and theBoard['MR'] == 'X' and theBoard['TM'] == 'X' and Xcount < 3 and Ocount < Xcount:
            if theBoard['BR'] == ' ':
                theBoard['BR'] = 'O'
                Ocount = Ocount + 1
                
        # Center O oddplay MR + TL
        elif theBoard['MM'] == 'O' and theBoard['MR'] == 'X' and theBoard['TL'] == 'X' and Xcount < 3 and Ocount < Xcount:
            if theBoard['TM'] == ' ':
                theBoard['TM'] = 'O'
                Ocount = Ocount + 1
        
        # Center O oddplay  MR + BM
        elif theBoard['MM'] == 'O' and theBoard['MR'] == 'X' and theBoard['BM'] == 'X' and Ocount < Xcount:
            if theBoard['BR'] == ' ':
                theBoard['BR'] = 'O'
                Ocount = Ocount + 1
                
        # Center O oddplay MR + BL
        elif theBoard['MM'] == 'O' and theBoard['MR'] == 'X' and theBoard['BL'] == 'X' and Ocount < Xcount:
            if theBoard['BR'] == ' ':
                theBoard['BR'] = 'O'
                Ocount = Ocount + 1
        
        # Center O oddplay TM + BL
        elif theBoard['MM'] == 'O' and theBoard['TM'] == 'X' and theBoard['BL'] == 'X'  and Xcount < 3 and Ocount < Xcount:
            if theBoard['TL'] == ' ':
                theBoard['TL'] = 'O'
                Ocount = Ocount + 1
                
        # Center O oddplay TM + BR
        elif theBoard['MM'] == 'O' and theBoard['TM'] == 'X' and theBoard['BR'] == 'X'  and Xcount < 3 and Ocount < Xcount:
            if theBoard['TL'] == ' ':
                theBoard['TL'] = 'O'
                Ocount = Ocount + 1

        # Center O oddplay BM + TR
        elif theBoard['MM'] == 'O' and theBoard['BM'] == 'X' and theBoard['TR'] == 'X'  and Xcount < 3 and Ocount < Xcount:
            if theBoard['BR'] == ' ':
                theBoard['BR'] = 'O'
                Ocount = Ocount + 1
                
        # Center O oddplay BM + TL       
        elif theBoard['MM'] == 'O' and theBoard['BM'] == 'X' and theBoard['TL'] == 'X'  and Xcount < 3 and Ocount < Xcount:
            if theBoard['BL'] == ' ':
                theBoard['BL'] = 'O'
                Ocount = Ocount + 1

        # Center O oddplay TM + BR + BL
        elif theBoard['MM'] == 'O' and theBoard['TM'] == 'X' and theBoard['BL'] == 'X' and theBoard['BR'] == 'X' and Xcount < 4 and theBoard['TL'] == ' ' and Ocount < Xcount:
            if theBoard['ML'] == ' ':
                theBoard['ML'] = 'O'
                Ocount = Ocount + 1
                
        # Center O oddplay BM + TR + TL
        elif theBoard['MM'] == 'O' and theBoard['TL'] == 'X' and theBoard['TR'] == 'X' and theBoard['BM'] == 'X' and Xcount < 4 and theBoard['BL'] == ' ' and Ocount < Xcount:
            if theBoard['ML'] == ' ':
                theBoard['ML'] = 'O'
                Ocount = Ocount + 1

        # Center O oddplay ML + TR + BR
        elif theBoard['MM'] == 'O' and theBoard['TR'] == 'X' and theBoard['BR'] == 'X' and theBoard['ML'] == 'X' and Ocount < Xcount:
            if theBoard['MR'] == ' ':
                theBoard['MR'] = 'O'
                Ocount = Ocount + 1
                
        # Center O oddplay MR + TL + BL
        elif theBoard['MM'] == 'O' and theBoard['TL'] == 'X' and theBoard['BL'] == 'X' and theBoard['MR'] == 'X' and Ocount < Xcount:
            if theBoard['TM'] == ' ':
                theBoard['TM'] = 'O'
                Ocount = Ocount + 1

    # Function that checks for any moves unaccounted for by checknoob

    def finalcheck(theBoard):
        global Ocount
        if Xcount != Ocount:
            if theBoard['TL'] == ' ' and Ocount < Xcount:
                theBoard['TL'] = 'O'
                Ocount = Ocount + 1
            elif theBoard['TM'] == ' ' and Ocount < Xcount:
                theBoard['TM'] = 'O'
                Ocount = Ocount + 1
            elif theBoard['TR'] == ' ' and Ocount < Xcount:
                theBoard['TR'] = 'O'
                Ocount = Ocount + 1
            elif theBoard['ML'] == ' ' and Ocount < Xcount:
                theBoard['ML'] = 'O'
                Ocount = Ocount + 1
            elif theBoard['MM'] == ' ' and Ocount < Xcount:
                theBoard['MM'] = 'O'
                Ocount = Ocount + 1
            elif theBoard['MR'] == ' ' and Ocount < Xcount:
                theBoard['MR'] = 'O'
                Ocount = Ocount + 1
            elif theBoard['BL'] == ' ' and Ocount < Xcount:
                theBoard['BL'] = 'O'
                Ocount = Ocount + 1
            elif theBoard['BM'] == ' ' and Ocount < Xcount:
                theBoard['BM'] = 'O'
                Ocount = Ocount + 1
            elif theBoard['BR'] == ' ' and Ocount < Xcount:
                theBoard['BR'] = 'O'
                Ocount = Ocount + 1

                
    # Function that detects when the game is over and changes the over check value to 'Yes'

    def end(theBoard):
        
        # If top row is all X's or O's, then change the status of over[Check] to Yes.
            if theBoard['TL'] == 'X' and theBoard['TM'] == 'X' and theBoard['TR'] == 'X':
                over['Check'] = 'Yes'
            if theBoard['TL'] == 'O' and theBoard['TM'] == 'O' and theBoard['TR'] == 'O':
                over['Check'] = 'Yes'
                
        # If middle row is all X's or O's, then change the status of over[Check] to Yes.
            if theBoard['ML'] == 'X' and theBoard['MM'] == 'X' and theBoard['MR'] == 'X':
                over['Check'] = 'Yes'
            if theBoard['ML'] == 'O' and theBoard['MM'] == 'O' and theBoard['MR'] == 'O':
                over['Check'] = 'Yes'
        # If bottom row is all X's or O's, then change the status of over[Check] to Yes.
            if theBoard['BL'] == 'X' and theBoard['BM'] == 'X' and theBoard['BR'] == 'X':
                over['Check'] = 'Yes'
            if theBoard['BL'] == 'O' and theBoard['BM'] == 'O' and theBoard['BR'] == 'O':
                over['Check'] = 'Yes'
                
        # If left column is all X's or O's, then change the status of over[Check] to Yes.
            if theBoard['TL'] == 'X' and theBoard['ML'] == 'X' and theBoard['BL'] == 'X':
                over['Check'] = 'Yes'
            if theBoard['TL'] == 'O' and theBoard['ML'] == 'O' and theBoard['BL'] == 'O':
                over['Check'] = 'Yes'

        # If middle column is all X's or O's, then change the status of over[Check] to Yes.
            if theBoard['TM'] == 'X' and theBoard['MM'] == 'X' and theBoard['BM'] == 'X':
                over['Check'] = 'Yes'
            if theBoard['TM'] == 'O' and theBoard['MM'] == 'O' and theBoard['BM'] == 'O':
                over['Check'] = 'Yes'

        # If right column is all X's or O's, then change the status of over[Check] to Yes.
            if theBoard['TR'] == 'X' and theBoard['MR'] == 'X' and theBoard['BR'] == 'X':
                over['Check'] = 'Yes'
            if theBoard['TR'] == 'O' and theBoard['MR'] == 'O' and theBoard['BR'] == 'O':
                over['Check'] = 'Yes'
                
        # If diagnol 1 is all X's or O's, then change the status of over[Check] to Yes.
            if theBoard['TL'] == 'X' and theBoard['MM'] == 'X' and theBoard['BR'] == 'X':
                over['Check'] = 'Yes'
            if theBoard['TL'] == 'O' and theBoard['MM'] == 'O' and theBoard['BR'] == 'O':
                over['Check'] = 'Yes'
                
        # If diagnol 2 is all X's or O's, then change the status of over[Check] to Yes.
            if theBoard['TR'] == 'X' and theBoard['MM'] == 'X' and theBoard['BL'] == 'X':
                over['Check'] = 'Yes'
            if theBoard['TR'] == 'O' and theBoard['MM'] == 'O' and theBoard['BL'] == 'O':
                over['Check'] = 'Yes'    
        
    # Tutorial message at the beginning of each gameloop

    print('Time to play Tic Tac Toe! Please enter a position:')
    print('TL = Top Left')
    print('TM = Top Middle')
    print('TR = Top Right')
    print('ML = Middle Left')
    print('MM = Middle Middle')
    print('MR = Middle Right')
    print ('BL = Bottom Left')
    print ('BM = Bottom Middle')
    print ('BR = Bottom Right')

    '''
    While the game is not over:
    1. Accept key input, then place X in the chosen key if there is no existing value.
    2. Then check to see if TicBot is near victory. If so, enter O into winning key.
    3. Check to see if the game is over based on causes listed the 'end' function. If so, display the board and break out of loop.
    4. If TicBot was not near victory and did not win, check to see if he is near defeat. If so, enter O into appropriate key.
    6. If TicBot is not near victory or defeat, check to see if player made a move that is not a immediate threat to TicBot.
    7. Make appropriate move based on future threats and possibility of victory.
    '''
    
    while over['Check'] != 'Yes':
        choice = input().upper()
        if theBoard['MM'] == ' ' and choice != 'MM' and (choice == 'TL' or choice == 'TM' or choice == 'TR' or choice == 'ML' or choice == 'MR' or choice == 'BL' or choice == 'BM' or choice == 'BR'):
            theBoard['MM'] = 'O'
            Ocount = Ocount + 1
        elif choice == 'X' and Xcount == 0 :
            theBoard['TL'] = 'O'
            Ocount = Ocount + 1
        if choice == 'TL' and theBoard['TL'] == ' ':
            theBoard['TL'] = 'X'
            Xcount = Xcount + 1
            nearWin(theBoard)        
            end(theBoard)
            if over['Check'] == 'Yes':
                play(theBoard)
                break
            nearLoss(theBoard)
            end(theBoard)
            if over['Check'] == 'Yes':
                play(theBoard)
                break
            checknoob(theBoard)
            finalcheck(theBoard)
        elif choice == 'TM' and theBoard['TM'] == ' ':
            theBoard['TM'] = 'X'
            Xcount = Xcount + 1
            nearWin(theBoard)
            end(theBoard)
            if over['Check'] == 'Yes':
                play(theBoard)
                break
            nearLoss(theBoard)
            end(theBoard)
            if over['Check'] == 'Yes':
                play(theBoard)
                break
            checknoob(theBoard)
            finalcheck(theBoard)
        elif choice == 'TR' and theBoard['TR'] == ' ' :
            theBoard['TR'] = 'X'
            Xcount = Xcount + 1
            nearWin(theBoard)
            end(theBoard)
            if over['Check'] == 'Yes':
                play(theBoard)
                break
            nearLoss(theBoard)
            end(theBoard)
            if over['Check'] == 'Yes':
                play(theBoard)
                break
            checknoob(theBoard)
            finalcheck(theBoard)
        elif choice == 'ML' and theBoard['ML'] == ' ':
            theBoard['ML'] = 'X'
            Xcount = Xcount + 1
            nearWin(theBoard)
            end(theBoard)
            if over['Check'] == 'Yes':
                play(theBoard)
                break
            nearLoss(theBoard)
            end(theBoard)
            if over['Check'] == 'Yes':
                play(theBoard)
                break
            checknoob(theBoard)
            finalcheck(theBoard)
        elif choice == 'MR' and theBoard['MR'] == ' ':
            theBoard['MR'] = 'X'
            Xcount = Xcount + 1
            nearWin(theBoard)
            end(theBoard)
            if over['Check'] == 'Yes':
                play(theBoard)
                break
            nearLoss(theBoard)
            end(theBoard)
            if over['Check'] == 'Yes':
                play(theBoard)
                break
            checknoob(theBoard)
            finalcheck(theBoard)
        elif choice == 'MM' and theBoard['MM'] == ' ' :
            theBoard['MM'] = 'X'
            Xcount = Xcount + 1
            nearWin(theBoard)
            end(theBoard)
            if over['Check'] == 'Yes':
                play(theBoard)
                break
            nearLoss(theBoard)
            end(theBoard)
            if over['Check'] == 'Yes':
                play(theBoard)
                break
            checknoob(theBoard)
            finalcheck(theBoard)
        elif choice == 'BL' and theBoard['BL'] == ' ' :
            theBoard['BL'] = 'X'
            Xcount = Xcount + 1
            nearWin(theBoard)
            end(theBoard)
            if over['Check'] == 'Yes':
                play(theBoard)
                break
            nearLoss(theBoard)
            end(theBoard)
            if over['Check'] == 'Yes':
                play(theBoard)
                break
            checknoob(theBoard)
            finalcheck(theBoard)
        elif choice == 'BM' and theBoard['BM'] == ' ' :
            theBoard['BM'] = 'X'
            Xcount = Xcount + 1
            nearWin(theBoard)
            end(theBoard)
            if over['Check'] == 'Yes':
                play(theBoard)
                break
            nearLoss(theBoard)
            end(theBoard)
            if over['Check'] == 'Yes':
                play(theBoard)
                break
            checknoob(theBoard)
            finalcheck(theBoard)
        elif choice == 'BR' and theBoard['BR'] == ' ' :
            theBoard['BR'] = 'X'
            Xcount = Xcount + 1
            nearWin(theBoard)
            end(theBoard)
            if over['Check'] == 'Yes':
                play(theBoard)
                break
            nearLoss(theBoard)
            end(theBoard)
            if over['Check'] == 'Yes':
                play(theBoard)
                break
            checknoob(theBoard)
            finalcheck(theBoard)       

    # Request valid input or if the board is full, end the game.
    
        else:
            print('\nInvalid input, try again.\n')
        if theBoard['TL'] != ' ' and theBoard['TM'] != ' ' and theBoard['TR'] != ' ' and theBoard['ML'] != ' ' and theBoard['MM'] != ' ' and theBoard['MR'] != ' ' and theBoard['BL'] != ' ' and theBoard['BM'] != ' ' and theBoard['BR'] != ' ':
            play(theBoard)
            break
        play(theBoard)
        
    # Taunt players and ask if they want to continue. Keep requesting until Y or N is entered.
    
    print("You can't win!\nTry again?")
    print ('Press Y to continue or N to exit.')
    askcontinue = input().upper()
    while askcontinue != 'N' and askcontinue != 'Y':
        print ('Press Y to continue or N to exit.')
        askcontinue = input().upper()
        
    # If player wants to continue, reset all variables including board, over-status, Xcount and Ocount.
    
    if askcontinue == 'Y':
        theBoard = {'TL': ' ', 'TM': ' ', 'TR': ' ', 'ML': ' ', 'MM': ' ', 'MR': ' ', 'BL': ' ', 'BM': ' ', 'BR': ' '}
        over = {'Check' : 'No'}
        Xcount = 0
        Ocount = 0
        GameOver = False
    elif askcontinue == 'N':
        GameOver = True

quit()            
        
        
    

    
        

    
    
