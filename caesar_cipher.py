"""
Your task here is to build a Caeser Cipher!
Find a video explanation here: https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/caesar-cipher

As well as an interactive working example here: https://www.khanacademy.org/computing/computer-science/cryptography/crypt/pi/caesar-cipher-exploration
"""

def caesarCipher(message, shiftNumber):
    """
    Take in the message (string) as well as the shiftNumber (integer) and return the cipheredText (use the shiftNumber to do the Caeser Cipher logic!)
    """
    ALPHABET = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    cipheredText = ""

    # TODO: Add your code here!
    return cipheredText

# An example of a test, add more to test your program and ensure it works!
shift = 6
originalMessage = "I hope you have a great summer!"
encryptedMessage = caesarCipher(message=originalMessage, shiftNumber=shift)
decryptedMessage = caesarCipher(message=encryptedMessage, shiftNumber=-shift)
print(f"Original: {originalMessage}\nEncrypted:{encryptedMessage}\nDecrypted:{decryptedMessage}")
