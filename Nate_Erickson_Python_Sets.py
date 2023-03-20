#Sets assignment
#<Nate Erickson>

#Prompt the user to input 2 English words 
word1 = input("Enter first word:")
print("First word is: " + word1)
word2 = input("Enter second word:")
print("Second word is: "+word2)

#Make two sets -- From each word make a set of letters in that word
set1 = set(word1)
set2 = set(word2)
#print the sets
print('The letters from the first word are:')
print(set1)
print('The letters from the second word are:')
print(set2)

#display the letters that the 2 words have in common
print('The common letters from the two words are: ')
intersect = set1.intersection(set2)
print(intersect)


#display the letters that are in the first word
#but not in the second
print('The letters that are in the first word but not the second are: ')
differ = set1 - set2
print(differ)


#display the letters of the alphabet that are in neither
#of the two words
set3 = {'a', 'b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
print('The letters from the alphabet that are in neither word are: ')
set4 = set1.union(set2)
set5 = set3-set4
print(set5)


#displays the letters of that are either in the first word
#or in the second word but not in both
print('The letters that are in both words but not shared are: ')
set6 = set1 ^ set2
print(set6)

#determines if ALL the letters of the first word
#are contained in the second word or not. Print an appropriate sentence indicating this
#***use a for loop to do this**
print('Are all letters from the first word contained in the second word?')
common = []
for letter in set1:
        if(letter in set2) and not (letter in common):
            common.append(letter)

if len(common) == len(set1):
    print('Yes all letters from the first word are contained in the second word')
else:
    print('No, all letters from the first word are not contained in the second word! Try again!')

#if ALL the letters in the first word are NOT contained in the 2nd word -
# display ONE of the letters in the first word that is NOT in the 2nd word 
if len(common) != len(set1):
    uncommon = []
    for char in set1:
        if(char not in set2) and not (char in uncommon):
            uncommon.append(char)

if len(common) != len(set1):
    print('One letter that is not in the second word is: '+uncommon[0])



        


