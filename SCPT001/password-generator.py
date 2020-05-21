import sys
import random
import string


#   Password length
length = 8

#   Numbers
num = True

#   Small characters
smallChar = True

#   Capitalized characters
capChar = True

#   Punctuations
punc = True

#   Generated result
result = ""



#   Main generation algorithm
def generate():
    global result
    global length
    global num
    global smallChar
    global capChar
    global punc

    for i in range(length):
        result += genChar(genType(num, smallChar, capChar, punc))



#   Return a generation type based on options
def genType(num, smallChar, capChar, punc):
    val = random.randint(0, 3)

    if not num and val == 0:
        val = genType(num, smallChar, capChar, punc)
    elif not smallChar and val == 1:
        val = genType(num, smallChar, capChar, punc)
    elif not capChar and val == 2:
        val = genType(num, smallChar, capChar, punc)
    elif not punc and val == 3:
        val = genType(num, smallChar, capChar, punc)

    return val




#   Return a random character based on options
def genChar(type):

    #   Generate values based on current generation type
    if type == 0:
        val = random.randint(0, 9)
    elif type == 1:
        val = random.choice(string.ascii_lowercase)
    elif type == 2:
        val = random.choice(string.ascii_uppercase)
    elif type == 3:
        val = random.choice(string.punctuation)

    return str(val)




#   Check if the generated password meets all the requirements
#   If not, randomly replace a character and restart the check procedure
def checking():
    global result
    global num
    global smallChar
    global capChar
    global punc

    changed = False
    hasNum = False
    hasSmallChar = False
    hasCapChar = False
    hasPunc = False

    for _ in result:
        if _ in string.digits:
            hasNum = True
        elif _ in string.ascii_lowercase:
            hasSmallChar = True
        elif _ in string.ascii_uppercase:
            hasCapChar = True
        elif _ in string.punctuation:
            hasPunc = True

    replace_index = random.randint(0, len(result) - 1)

    if not hasNum and num:
        result = result[:replace_index] + genChar(0) + result[replace_index + 1:]
        changed = True
    if not hasSmallChar and smallChar:
        result = result[:replace_index] + genChar(1) + result[replace_index + 1:]
        changed = True
    if not hasCapChar and capChar:
        result = result[:replace_index] + genChar(2) + result[replace_index + 1:]
        changed = True
    if not hasPunc and punc:
        result = result[:replace_index] + genChar(3) + result[replace_index + 1:]
        changed = True

    if changed:
        checking()
    else:
        return



#   Main Menu
def menu():
    global result
    global length
    global num
    global smallChar
    global capChar
    global punc


    #   Clear screen
    from os import system, name
    if name == "nt":
        system("cls")
    else:
        system("clear")

    print("Yeahlowflicker Production")
    print("SCPT001 - Password Generator\n\n")


    print("Password Length: {}\n".format(length))


    print("Options:")

    if num:
        print("[X] 0: Numbers")
    else:
        print("[ ] 0: Numbers")

    if smallChar:
        print("[X] 1: Small Characters")
    else:
        print("[ ] 1: Small Characters")

    if capChar:
        print("[X] 2: Capitalized Characters")
    else:
        print("[ ] 2: Capitalized Characters")

    if punc:
        print("[X] 3: Punctuations")
    else:
        print("[ ] 3: Punctuations")


    print("\nEnter option index to toggle options.")
    print("Enter 'length' to modify password length.")
    print("Enter 'quit' to exit.")
    print("Enter 'start' to generate.\n")

    option = raw_input("Your option: ")


    if option == "0":
        num = not num
        menu()

    elif option == "1":
        smallChar = not smallChar
        menu()

    elif option == "2":
        capChar = not capChar
        menu()

    elif option == "3":
        punc = not punc
        menu()

    elif option == "length":
        length = input("Enter new password length: ")

        #   Limit password length (Range: 4 - 100)
        if length < 4:
            length = 4
            print("\nPassword too short, set to 4 (minimum) automatically.")
            raw_input("Press any key to advance...")

        elif length > 100:
            length = 100
            print("\nPassword too long, set to 100 (maximum) automatically.")
            raw_input("Press any key to advance...")

        menu()

    elif option == "quit":
        return

    elif option == "start":
        #   If no option is selected, show error and stop program
        if not num and not smallChar and not capChar and not punc:
            print("ERROR: No generation type is selected.")
            return

        #   Otherwise, generate and display password
        generate()
        checking()
        print("\nGenerating...")
        print("\nGenerated Password:\n---------------------\n{}\n\n".format(result))

    else:
        menu()





#   Main Program
if __name__ == "__main__":
    menu()
    raw_input("Press any key to exit...")
    sys.exit()
