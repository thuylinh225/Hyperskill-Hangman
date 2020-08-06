import random
word_list = ['python', 'java', 'kotlin', 'javascript']
print("H A N G M A N")
while True:
    text = input("Type 'play' to play the game, 'exit' to quit: ")
    if text == "play":
        random.seed()
        word = random.choice(word_list)
        word_dic = set(word)
        string = "-" * len(word)
        count = 8
        inputSet = set()
        letterSet = set()
        print()
        while True:
            print(string)
            letter = input("Input a letter: ")
            newMatch = ""
            if len(letter) > 1:
                print("You should input a single letter")
            elif letter.isascii() == False or letter.islower() == False:
                print("It is not an ASCII lowercase letter")
            elif letter in letterSet:
                print("You already typed this letter")
            elif letter not in word_dic:
                count -= 1
                print("No such letter in the word")
            elif letter in word_dic and letter not in string:
                inputSet.add(letter)
                for i in range(len(word)):
                    if word[i] in inputSet:
                        newMatch += word[i]
                    else:
                        newMatch += "-"
                string = newMatch
            letterSet.add(letter)
            if count >= 0 and string == word:
                print("You guessed the word {}!".format(string))
                print("You survived!")
                break
            if count == 0 and string != word:
                print("You are hanged!")
                break
            print("\n")
    else:
        break
