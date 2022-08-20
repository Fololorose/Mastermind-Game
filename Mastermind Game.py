import random

# Main function to call other functions sequentially.
def main():

    # Welcome message and prompt the player to enter name.
    print('Welcome to the Mastermind Computer Game.')
    print('What should I call you?')
    name = input('Your Name:')

    # Ask the player whether to proceed to the tutorial or skip the tutorial.
    while True:
        print(name,end = '.' + ' Do you want to proceed to the tutorial? (Enter Y for yes and S for skip.)\n')
        tutorial = input()
        if tutorial == 'y' or tutorial == 'Y':
            gameRules(name)
            colourRepresentationTable()
            break
        elif tutorial == 's' or tutorial == 'S':
            colourRepresentationTable()
            break
        else:
            print('Error Selection. Please enter a valid response.')

    play = 1
    while play == 1:
        # Call the colourCodeGenerator function to randomly generate a colour code and store it into a list.
        colourCode_List = colourCodeGenerator()
        print('\nColour code has been generated.')

        # Call the playerGuessing function to prompt player to insert the guess.
        # After that, call the hintGenerator function to generate the hint for each guessing.
        counter = 1
        correct = 0
        while counter <= 11:
            guessing_List = playerGuessing(counter)
            print('\nYour Guessing:', guessing_List)
            correctPosition = hintGenerator(guessing_List, colourCode_List)
            counter = counter + 1
            if correctPosition == 4:
                correct = 1
                break

        # Print the result to the player after finishing guessing.
        if correct == 1:
            print('\nCongratulation!!! Your guessing is correct!')
            print('You make the right guess within', counter-1, 'round(s).')
        else:
            print('\nSorry. You fail to make the correct guess within 11 rounds.')
            print('The colour code is:', colourCode_List)
            
        # Ask the player whether to play again or not.
        while True:
            again = input('\nDo you want to play again? (Enter Y for yes and N for no.)\n')
            if again == 'y' or again == 'Y':
                break
            elif again == 'n' or again == 'N':
                play = 0 
                print(name,end = '. Thank you for playing this game. See you next time.')
                break
            else:
                print('Error Selection. Please enter a valid response.')
                continue

    
    
    

# Define colour type in the Mastermind Computer Game.
colour_List = ['white', 'red', 'blue', 'green', 'yellow', 'orange', 'violet', 'pink']

# Explain the game rules.
def gameRules(name):
    print('\nGame Rules:')
    print('\nHi,', name, end = '.')
    print('\n\nFor each game, a colour code consists of 4 colours will be randomly generated from a total of 8 colours.')
    print('\nReminder: Duplicated colours may exists !!!\n')
    print(name,end = '. As the codebreaker, you need to guess the pattern of colours within 11 rounds.\n')
    print('\nFor every guess, you need to enter 4 colours in ascending order coresponding to the colour code.')
    print('\nAfter each guess, a hint will be given to you.')
    print('\nRepeat the guessing until you get the right answer.')
    print('\nOnce you exceed 11 times of guessing, you will be automatically considered to fail the game.')
    print('\nGOOD LUCK !!!')

# Display a table that show the representation by abbreviation of each colours for the convenience of player.
def colourRepresentationTable():
    print('\nYou just need to enter the representation alphabets based on the colours that you want to select.')
    print('\nDuring guessing, you may also enter U for undo and C for clearing the current list to reset your guessing.')
    print('\nBelow is the table for you to refer to.\n')
    print('%2s' % 'No', '%10s' % 'Colour', '%16s' % 'Representation')
    for row in range (0, len(colour_List)):
        print('%2d' % (row + 1), '%10s' % colour_List[row].upper(), '%10s' % (colour_List[row][:1]))
    
# Generate random colour code for player.
def colourCodeGenerator():
    colourCode_List = []
    for x in range (1,5):
        colourCode_List.append(colour_List[random.randint(0, len(colour_List)-1)])
    return colourCode_List

# Ask player to insert their guessing and assign it into a list.
def playerGuessing(counter):
    print('\nRound', counter)
    order_List = ['first', 'second', 'third', 'fourth']
    guessing_List = []
    i = 0
    while i < 4:
        valid = 0
        guessing = input(f'Please insert the {order_List[i]} colour:')
        if guessing.lower() == 'u':
            if i > 0:
                guessing_List.pop(len(guessing_List)-1)
                i = i - 1
            else:
                i = 0
        elif guessing.lower() == 'c':
            guessing_List[:] = []
            i = 0
        else:
            for x in range(0,len(colour_List)):
                if guessing.lower() == colour_List[x][0]:
                     guessing = colour_List[x]
                     valid = valid + 1
            if valid == 1:
                guessing_List.append(guessing)
                i = i + 1
            else:
                print('Error Selection. Please insert a valid colour.')
    return guessing_List

# Match the guessing with correct colour code to generate hint.
def hintGenerator(guessing_List, colourCode_List):
    compare_List = colourCode_List[:]
    correctPosition_List = []
    # Check whether the guessing is matched in both colour and position. 
    for x in range(0, 4):
        if guessing_List[x] == compare_List[x]:
            correctPosition_List.append(guessing_List[x])
    # Check whether the guessing is matched with one of the colour.
    for y in range(0, 4):
        z = 0
        while z < len(compare_List):
            if guessing_List[y] == compare_List[z]:
                compare_List.pop(z)
                break
            else:
                z = z + 1
                    
    correctPosition = len(correctPosition_List)
    wrongPosition = 4 - len(compare_List) - correctPosition

    if correctPosition == 4:
        return correctPosition
    else:
        print('\nCorrect Colour in Correct Position:', correctPosition)
        print('Correct Colour in Wrong Position:', wrongPosition)

main()


    
