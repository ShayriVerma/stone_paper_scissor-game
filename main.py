#stone paper scissor game :-

import random
list = ['Stone' , 'Paper' , 'Scissor']

total_chance = 5    #declaring and initializing all the variables here
no_of_chance = 0
human_score = 0
comp_score = 0

while no_of_chance < total_chance :
    human = input ('Stone , Paper , Scissor : ')
    comp = random.choice(list)

    if human == comp :
        print ("its a tie both scored 0 points \n")
    elif human == "Stone" and comp == "Paper" :
        comp_score = comp_score + 1
        print (f"you selected {human} and computer selected {comp} \n")
        print ("Computer wins 1 point \n")
    elif human == "Stone" and comp == "Scissor" :
        human_score = human_score + 1
        print (f"you selected {human} and computer selected {comp} \n")
        print ("You won 1 point \n")
    elif human == "Paper" and comp == "Stone" :
        human_score = human_score + 1
        print (f"you selected {human} and computer selected {comp} \n")
        print ("You won 1 point \n")
    elif human == "Paper" and comp == "Scissor" :
        comp_score = comp_score + 1
        print (f"you selected {human} and computer selected {comp} \n")
        print (f"Computer wins 1 point \n")
    elif human == "Scissor" and comp == "Paper" :
        human_score = human_score + 1
        print (f"you selected {human} and computer selected {comp} \n")
        print ("You won 1 point \n")
    elif human == "Scissor" and comp == "Stone" :
        comp_score = comp_score + 1
        print (f"you selected {human} and computer selected {comp} \n")
        print ("Computer wins 1 point \n")
    else :
        print ("Please enter a valid input")

    no_of_chance = no_of_chance + 1
    print (f"You have {total_chance - no_of_chance} chances left out of {total_chance} \n")

print ("Gave Over!")

if comp_score > human_score :
    print ("Computer wins you loose!")

elif comp_score < human_score :
    print ("You won computer loose!")

else :
    print ("its a tie")

print (f"you scored {human_score} and computer scored {comp_score}")