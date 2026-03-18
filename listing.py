def match_words(words):
    counter=0
    
    for word in words:
        if word in words:
            
            if len(word) > 1 and word[0] == word[-1]:
                
                counter +=1
    return counter

print(match_words(["abc","21","long","tat","cbc"]))



n = 5

for i in range(n):
    for j in range(i):
        print("* ", end="")
    print('')
    

for i in range(n,0,-1):
    for j in range(i):
        print("* ", end="")
    print('')