tic_tac_toe_List = ["1", "2", "3", "4", "5", "6", "7", "8", "9"] 

turn = 0
while turn < 9:
    print( tic_tac_toe_List[0] + '|' + tic_tac_toe_List[1] + '|' + tic_tac_toe_List[2])
    print('-------')
    print( tic_tac_toe_List[3] + '|' + tic_tac_toe_List[4] + '|' + tic_tac_toe_List[5])
    print('-------')
    print( tic_tac_toe_List[6] + '|' + tic_tac_toe_List[7] + '|' + tic_tac_toe_List[8])
    
    userturn = input("Enter a number Between 0-8 to Mark the index postition for your Turn")
    numconverter = int(userturn)


    tic_tac_toe_List.insert(numconverter, 'X')
    turn += 1