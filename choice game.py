from tkinter.messagebox import YES


print("WELCOME TO OUR GAME PORTABLE")
GAME = input("would yo like to play our game: (yes/no)?)")
score =0
total_questions = 3

GAME.lower==YES
GAME = input("which fruit are you like to purchase in mall: ")
if GAME == 'mango':
    score +=1
    print('correct')
else:
    print('hoo missed it')

GAME = input("which is your favourite animal: ")
if GAME == 'lion':
    score +=1
    print('correct')
else:
    print('hoo missed it')

GAME = input("which city call mini swizerland: ")
if GAME == 'sivamogga':
    score +=1
    print('correct')
else:
    print('hoo missed it')

print("THANK YOU GIVING TIME WITH US")
mark = (score/total_questions)*100
print("marks obtained: ",mark)
print("BYE")