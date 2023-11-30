# This is a sample Python script.
morseEncryptDict = {'A': '.-', 'B': '-...',
                    'C': '-.-.', 'D': '-..', 'E': '.',
                    'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-',
                    'L': '.-..', 'M': '--', 'N': '-.',
                    'O': '---', 'P': '.--.', 'Q': '--.-',
                    'R': '.-.', 'S': '...', 'T': '-',
                    'U': '..-', 'V': '...-', 'W': '.--',
                    'X': '-..-', 'Y': '-.--', 'Z': '--..',
                    '1': '.----', '2': '..---', '3': '...--',
                    '4': '....-', '5': '.....', '6': '-....',
                    '7': '--...', '8': '---..', '9': '----.',
                    '0': '-----', ', ': '--..--', '.': '.-.-.-',
                    '?': '..--..', '/': '-..-.', '-': '-....-',
                    '(': '-.--.', ')': '-.--.-', '\'': '----'}

morseDecryptDict = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
                    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
                    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
                    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
                    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
                    '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
                    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
                    '-----': '0', '--..--': ', ', '.-.-.-': '.', '..--..': '?', '-..-.': '/', '-....-': '-',
                    '-.--.': '(', '-.--.-': ')', '.----.': '\''}


def encrypt(inputString):
    outputString = ''
    inputString = inputString.upper()

    for i in range(len(inputString)):
        if (inputString[i] != ' '):
            outputString += morseEncryptDict[inputString[i]]
            if (i != len(inputString) - 1):
                if (inputString[i + 1] != ' '):
                    outputString += ' '
        else:
            outputString += ' '
    return outputString


def decrypt(inputString):
    outputString = ''
    characterBuffer = ''

    for i in range(len(inputString)):
        if (inputString[i] == ' '):
            if characterBuffer != "":
                outputString += morseDecryptDict[characterBuffer]
                characterBuffer = ''
        else:
            characterBuffer += inputString[i]
        if i == len(inputString) - 1 and characterBuffer != '':
            outputString += morseDecryptDict[characterBuffer]

    return outputString


def main():
    userInput = input('Please select one of the following options Encrypt/Decrypt/Exit:\n').upper()
    if userInput == 'ENCRYPT' or userInput == '1':
        userInput = input('Please enter the string that you would like to encrypt:\n')
        print(encrypt(userInput))
    elif userInput == 'DECRYPT' or userInput == '2':
        userInput = input('Please enter the string that you would like to decrypt:\n')
        print(decrypt(userInput))
    elif userInput == 'EXIT' or userInput == '3':
        print('Exiting program')
    else:
        print("invalid user input!")
    return


main()