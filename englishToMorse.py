def userHelp():
    morsecodeChart = ["A = .-", "B = -...", "C = -.-.", "D = -..", "E = .", "F = ..-.", "G = --.", "H = ....", "I = ..", "J = .---",
                      "K = -.-", "L = .-..", "M = --", "N = -.", "O = ---", "P = .--.", "Q = --.-", "R = .-.", "S = ...", "T = -",
                      "U = ..-", "V = ...-", "W = .--", "X = -..-", "Y = -.--", "Z = --..", "1 = .----", "2 = ..---", "3 = ...--",
                      "4 = ....-", "5 = .....", "6 = -....", "7 = --...", "8 = ---..", "9 = ----.", "0 = -----"]
    help = input("Do you want to see the morse code chart? (y/n): ")

    if help == "y":
        print(morsecodeChart)
    elif help == "n":
        print("Okay.")
    else:
        print("Invalid Response!")

    start = input("Do you want to start? (y/n): ")

    if start == "y":
        englishToMorseCode()
    elif start == "n":
        userHelp()
    else:
        print("Invalid Input")



def englishToMorseCode(morsecodeDict):
    morsecodeDict = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": ".....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "0": "-----",
        " ": " / ",
    }

    while True:
        repeat = input("Do you want to do it again? (y/n): ")

        if repeat == "y":
            print("Translating Enligh to Morse Code.")
            phrase = input("What phrase would you like to translate? (ENTER IN ALL CAPS): ")

            for letter in phrase:
                print(morsecodeDict[letter], end = " ")
                
            print()
        elif repeat == "n":
            break
        else:
            print("Invalid Answer!")


userHelp()
