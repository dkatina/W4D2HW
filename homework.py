
def ispalindrome(word):
    cut_word = ""                               # the for loop is O(n) because it iterates once per character aka linear 
    for char in word:                           # .lower() is O(1) when acting on a single character
        if char.isalpha(): 
            char = char.lower()                     #after reading some doc it appears .isAlpha is O(1) when comparing single character values
            cut_word += char
              
    left = 0
    right = len(cut_word) - 1

    while left <= right:                       #I would say the while loop is O( log n) because it iterates .5 times per character
        if cut_word[left] != cut_word[right]:    #Everyhting that happens in the while loop is O(1)
            return False
        right -= 1
        left += 1
    return True

print(ispalindrome('A man, a plan, a canal: Panama'))
                                                    
                                                    #Over all time complexity is O(n) beacause the to main consumers are the for loop(O(n)) and the while loop (O(log n)) 
                                                    #And the O(n) kind of overides our O(log n)