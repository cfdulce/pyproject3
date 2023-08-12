def gameIntro(): 
    setting=("""POV: It's a sunny day outside. You decide you want to go to the park and enjoy the lovely weather. You put on some shorts and a short sleeve shirt along with your favorite pair of shoes! And of course, your favorite hat! You also pack a backpack with snacks and water just in case you need some for later. As you walk around the park you look around, admiring the beauty of your surroundings. The rays of the sun embracing you in a warm hug, the fresh air and scent of nearby flowers... the laughter of children playing around, and squirrels running up and down trees chasing one another. Then suddenly, you encounter a very peculiar looking bunny in a stripped blue and white vest paired with some dark blue, shiny, shoes. It's fur white as snow and ears pointier than a clock's hands. Intrigued, you decide to walk up to it and take a closer look at it.""") 
    print(setting) 
    print(" ") 
    print("BUNNY: Hello, Hello!!!! What brings you here?") 
    print(" ") 
    print("[You look around and rub your eyes]") 
    print(" ") 
    print("BUNNY: My name is Mallow Bunny! What's your name?")
    print(" ") 
    username=input("[Please enter your name]") 
    print(f"{username}? What a lovely name!! \n Hmm...") 
    questionuser=input("Would you like to play a game? (Y or N)")
    if questionuser == "Y": 
        print("""\nHello! Welcome to EGGSCRAMBLE! \n \n Please read the rules below before playing! \n \n                                      --Game Rules-- \n\n 1.) Capitalize the first letter of every word you unscramble! No punctuation required! \n 2.) Type 'HINT' if you need one! However, you may only get three hints per question. Use them wisely! \n 3.) Keep track of the points earned! The sum of all of your earned points will be used at the end of the game for your reward! \n 6.) You may SURRENDER! , however, you will not receive any points! \n5.) Have fun and be creative!""")
gameIntro() 
#game1()

print("--QUESTION 1--")
print("UNSCRAMBLE: oamblo") 
q1=input("What is the word?") 
while True: 
    if q1=="Abloom": 
        print("Correct! (4 pts)") 
        break 
    elif q1== "HINT 1": 
        print("starts with 'A'") 
        q1=input("What is the word?") 
        print(q1) 
    elif q1=="HINT 2": 
        print("What you call something covered in flowers.") 
        q1=input("What is the word?") 
    elif q1=="HINT 3": 
        print("Synnonym of fluroshing") 
        q1=input("What is the word?") 
    elif q1=="SURRENDER!":
        break
    else: 
        print("Try again") 
        q1=input("What is the word?")
        
print("--QUESTION 2--")        
print("UNSCRAMBLE: rnebviakr")
q2=input("What is the word?") 
while True: 
    if q2=="Riverbank": 
        print("Correct! (6 pts)") 
        break 
    elif q2== "HINT 1": 
        print("starts with 'R'") 
        q2=input("What is the word?") 
        print(q2) 
    elif q2=="HINT 2": 
        print("What you call the ground at the edge of a river.") 
        q2=input("What is the word?") 
    elif q2=="HINT 3": 
        print("Synnonym of riverside") 
        q2=input("What is the word?") 
    elif q2=="SURRENDER!":
        break
    else: 
        print("Try again") 
        q2=input("What is the word?")    

print("--QUESTION 3--")        
print("UNSCRAMBLE: avtdren")
q3=input("What is the word?") 
while True: 
    if q3=="Verdant": 
        print("Correct! (5 pts)") 
        break 
    elif q3== "HINT 1": 
        print("starts with 'R'") 
        q3=input("What is the word?") 
        print(q3) 
    elif q3=="HINT 2": 
        print("What you call something green with grass or green in color.") 
        q3=input("What is the word?") 
    elif q3=="HINT 3": 
        print("Synnonym of leafy")
        q3=input("What is the word?")
    elif q3=="SURRENDER!":
        break
    else: 
        print("Try again") 
        q3=input("What is the word?")    

print("--QUESTION 4--")        
print("UNSCRAMBLE: rcanhb")
q4=input("What is the word?") 
while True: 
    if q4=="Branch": 
        print("Correct! (3 pts)") 
        break 
    elif q4== "HINT 1": 
        print("starts with 'B'") 
        q4=input("What is the word?") 
        print(q4) 
    elif q4=="HINT 2": 
        print("What you call the part of a tree that grows out from the trunk.") 
        q4=input("What is the word?") 
    elif q4=="HINT 3": 
        print("Bigger than a twig")
        q4=input("What is the word?")
    elif q4=="SURRENDER!":
        break
    else: 
        print("Try again") 
        q4=input("What is the word?")    

print("--QUESTION 5--")        
print("UNSCRAMBLE: ghuslint")
q5=input("What is the word?") 
while True: 
    if q5=="Sunlight": 
        print("Correct!(2 pts)") 
        break 
    elif q5== "HINT 1": 
        print("starts with 'S'") 
        q5=input("What is the word?") 
        print(q5) 
    elif q5=="HINT 2": 
        print("What you call the light from the sun.") 
        q5=input("What is the word?") 
    elif q5=="HINT 3": 
        print("Synnonym of sunshine")
        q5=input("What is the word?")
    elif q5=="SURRENDER!":
        break
    else: 
        print("Try again") 
        q5=input("What is the word?")    

print("--QUESTION 6--")        
print("UNSCRAMBLE: niodasndel")
q6=input("What is the word?") 
while True: 
    if q6=="dandelions": 
        print("Correct! (6 pts)") 
        break 
    elif q6== "HINT 1": 
        print("starts with 'D'") 
        q6=input("What is the word?") 
        print(q6) 
    elif q6=="HINT 2": 
        print("What you call a bright yellow flower with white, hairy seeds.") 
        q6=input("What is the word?") 
    elif q3=="HINT 3": 
        print("This flower can be eaten, and is used for wishes!")
        q6=input("What is the word?")
    elif q6=="SURRENDER!":
        break
    else: 
        print("Try again") 
        q6=input("What is the word?")    

print("--QUESTION 7--")        
print("UNSCRAMBLE: wywaakl")
q7=input("What is the word?") 
while True: 
    if q7=="walkway": 
        print("Correct! (5 pts)") 
        break 
    elif q7== "HINT 1": 
        print("starts with 'W'") 
        q7=input("What is the word?") 
        print(q7) 
    elif q7=="HINT 2": 
        print("What you call a path for walking along.") 
        q7=input("What is the word?") 
    elif q7=="HINT 3": 
        print("Synnonym of sidewalk")
        q7=input("What is the word?")
    elif q7=="SURRENDER!":
        break
    else: 
        print("Try again") 
        q7=input("What is the word?")    

print("--QUESTION 8--")        
print("UNSCRAMBLE: suhb")
q8=input("What is the word?") 
while True: 
    if q8=="Bush": 
        print("Correct!(4 pts)") 
        break 
    elif q8== "HINT 1": 
        print("starts with 'B'") 
        q8=input("What is the word?") 
        print(q8) 
    elif q8=="HINT 2": 
        print("What you call a plant smaller than a tree.") 
        q8=input("What is the word?") 
    elif q8=="HINT 3": 
        print("Synnonym of shrub")
        q8=input("What is the word?")
    elif q8=="SURRENDER!":
        break
    else: 
        print("Try again") 
        q8=input("What is the word?")    

print("--QUESTION 9--")        
print("UNSCRAMBLE: rleirusq")
q9=input("What is the word?") 
while True: 
    if q9=="squirrel": 
        print("Correct!(6 pts)") 
        break 
    elif q9== "HINT 1": 
        print("starts with 'S'") 
        q9=input("What is the word?") 
        print(q9) 
    elif q9=="HINT 2": 
        print("What you call a slender bodies with very long very bushy tails and large eyes.") 
        q9=input("What is the word?") 
    elif q9=="HINT 3": 
        print("No Available hint, sorry!")
        q9=input("What is the word?")
    elif q9=="SURRENDER!":
        break
    else: 
        print("Try again") 
        q9=input("What is the word?")    

print("--QUESTION 10--")        
print("UNSCRAMBLE: gmirdmhunib")
q10=input("What is the word?") 
while True: 
    if q10=="Hummingbird": 
        print("Correct! (9 pts)") 
        break 
    elif q10== "HINT 1": 
        print("starts with 'H'") 
        q10=input("What is the word?") 
        print(q10) 
    elif q10=="HINT 2": 
        print("What you call a small bird with a long, slender bill")
        q10=input("What is the word?") 
    elif q10=="HINT 3": 
        print("No 3 hint for this word!")
        q10=input("What is the word?")
    elif q10=="SURRENDER!":
        break
    else: 
        print("Try again") 
        q10=input("What is the word?")    

ptsquestion=input("How many points do you have in total?")
if ptsquestion==0:
    print("No rewards! Sorry! Good luck next time :(")
elif ptsquestion==50:
    print("Mr. Bunny has given 10 chocolate bunnies! Good Job!")
elif ptsquestion<=50:
    print("Mr. Bunny has given you 5 peeps (marshmallows! Good Job!")

  

