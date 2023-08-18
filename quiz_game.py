print("Quiz game")
score = 0
playing = input("Do you want to play? ")

if playing.lower() == "yes":
    print("Let's play")
    
    answer = input("What is the capital of France? ")
    if answer.lower() == "paris":
        print("Correct")
        score += 1
    else: 
        print("Incorrect")
        
    answer = input("Who wrote Romeo and Juliet? ")
    if answer.lower() == "william shakespeare":
        print("Correct")
        score += 1
    else: 
        print("Incorrect")
        
    answer = input("What is the chemical symbol for gold? ")
    if answer.lower() == "au":
        print("Correct")
        score += 1
    else: 
        print("Incorrect")
        
    answer = input("Which planet is known as the Red Planet? ")
    if answer.lower() == "mars":
        print("Correct")
        score += 1
    else: 
        print("Incorrect")
        
    answer = input("Who is credited with the invention of the telephone? ")
    if answer.lower() == "alexander graham bell":
        print("Correct")
        score += 1
    else: 
        print("Incorrect")
    
elif playing.lower() == "no":
    print("Quitting the game.")
else:
    print("Please respond with yes or no.")

print("Your score:", score)
