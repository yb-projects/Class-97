intro = input("Write about you: ")
characterCount = 0
wordCount = 1

for i in intro:
    characterCount = characterCount + 1
    if (i == " "):
        wordCount = wordCount + 1
    
print(characterCount)
print("Words:", wordCount)
