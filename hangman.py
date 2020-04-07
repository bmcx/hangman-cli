import random
man = [
"""______
|    |
|    |
|    
|   
|     
|   
|
|=========""",
"""______
|    |
|    |
|    \O
|   
|     
|   
|
|=========""",
"""______
|    |
|    |
|    \O
|     |
|     |  
|    
|
|=========""",
"""______
|    |
|    |
|    \O
|   \/|
|     |  
|    
|
|=========""",
"""______
|    |
|    |
|    \O
|   \/|\/
|     |  
|    
|
|=========""",
"""______
|    |
|    |
|    \O
|   \/|\/
|     |  
|   _/ 
|
|=========""",
"""______
|    |
|    |
|    \O
|   \/|\/
|     |  
|   _/ \_
|
|========="""
]

def drawLevel(man, word, mistakes, answer, letterCount, tried, score):
    print(man[mistakes])
    print(' '.join(answer) if letterCount > 0 else ' '.join(answer)+"\n\nCongratulations!!\n The word is correct" )
    print( "\nSorry you are DEAD!! x_x \n The word is "+word if mistakes >= 6 else '')
    if(tried and letterCount > 0):
        print("X : " + ' '.join(tried))

def getInput(tried):
    ok = False
    while not ok:
        letter = str(input('\nTry a letter: ')).lower()
        if not(letter in tried):
            ok = True
            return letter
        print("You already tried '"+letter+"'")
    


play = True
score = 0
while(play):

    with open('words.txt') as f:
        words = f.readlines()
        word = words[random.randrange(0, 80000)]

    letterCount = len(word)-1
    mistakes = 0
    tried = []
    rand = random.randrange(1,len(word))

    out = [ ( word[i-1] if ( rand == i ) else '_' ) for i in range(1,len(word)) ]

    while(letterCount > 0 and mistakes < 6):
        letter  = word[rand-1] if(letterCount == len(word)-1) else getInput(tried)

        tried.append(letter)
        for idx,el in enumerate(word):
            if el == letter:
                out[idx] = el
                letterCount -= 1
        
        if letter not in word:
            mistakes += 1

        drawLevel(man, word, mistakes, out, letterCount, tried, score)

    score = score+len(word)*2 if mistakes < 6 else score
    
    ask = input("Score : "+str(score)+"\nAny key to continue, Q to quit : ")
    if ask.lower() == 'q':
        exit()
