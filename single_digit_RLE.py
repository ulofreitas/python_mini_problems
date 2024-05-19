"""
Your goal is to implement Single digit Run-length decoding! We'll start by looking at the following resources
to learn more about it, and its advantages/drawbacks.

https://api.video/what-is/run-length-encoding/
https://www.dremio.com/wiki/run-length-encoding/

The encoding step has been provided for you (runLengthEncoding()), but feel free to delete the current approach at the end
and try to implement it on your own! It's a great practice!

Your main take will be to implement the runLengthSingleDigitDecoding() function!
There are two warm up tasks repeatedCharacter() and extractAndExpandDigitAndChar() which can be helpful for you to
practice string concepts before moving onto the full algorithm.

# This is a first step to the world of compression/encoding information! Learn more via Khan Academy below:
# https://www.khanacademy.org/computing/computers-and-internet/xcae6f4a7ff015e7d:digital-information/xcae6f4a7ff015e7d:data-compression/a/file-compression-introduction
"""
# Part 0: Warmup Challenges
# We'll start with some warm up problems to ground some concepts about strings

# Warmup Task 1: Character Multiplication
def repeatedCharacter(character, count):
    """
    Task: Write a function that takes a character and a number (integer), and returns the character repeated that number of times.

    For example...
    - repeatedCharacter('a', 2) should return "aa"
    - repeatedCharacter('B', 8) should return "BBBBBBBB"
    """
    output = ""
    # TODO: Add your code here!
    return output


# Warmup Task 2: Extract a single digit and character, then expand it with character multiplication
def extractAndExpandDigitAndChar(inputString):
    """
    Task: take in the inputString, which will be a string of the format of a single-digit number followed by a character
    and return a string of the character repeated that many times. (e.g. inputString = "2A")

    Note: This may feel similar to task 1, but notice what's different about the inputs

    Examples:
    - extractAndExpandDigitAndChar("2A") should return "AA"
    - extractAndExpandDigitAndChar("9B") should return "BBBBBBBBB"
    """
    output = ""
    # TODO: Add your code here!
    return output

def runLengthEncoding(textToEncode):
    """
    Takes a string (plaintext/normal text) and returns the run-length encoding.

    PROVIDED
    Go through the provided text.
    For each character in the input, see if the current character is the same as the next to help you
    increment the count. If the current character is different from the next, then add the current
    character to the encoding. This approach works for both single and multi digit encoding

    PROVIDED
    Question: After completing this coding task, try deleting and coding this runLengthEncoding() function from scratch!
    """
    # PROVIDED CODE: Once you get decoding to work, delete this and see if you can code it from scratch!
    encodedString = ""
    count = 1
    currChar = ""
    for i in range(len(textToEncode) - 1):
        currChar = textToEncode[i]
        nextChar = textToEncode[i + 1]
        if currChar == nextChar:
            count += 1
        else:
            newPart = f"{count}{currChar}"
            encodedString += newPart
            count = 1

    currChar = textToEncode[len(textToEncode) - 1]
    newPart = f"{count}{currChar}"
    encodedString += newPart
    # PROVIDED CODE: Once you get decoding to work, delete this and see if you can code it from scratch!
    return encodedString


def runLengthSingleDigitDecoding(encodedString):
    """
    For this task we'll only have single digits of repeated characters (0-9). That means that for decoding
    you'll always have the pattern of a number, then the character.
    - First get the number, then copy the character

    Something to think about: what Python concept(s) are useful here?
    """
    decodedString = ""
    # TODO: Add your code here!
    return decodedString


# Tests to verify your code's behavior. Feel free to add more tests to different parts!
def testRepeatedCharacter(character, count, solution):
    # PROVIDED CODE: Don't modify
    errorMessage = f"Your code returned: {repeatedCharacter(character, count)}\n                  Expected string: {solution}"
    assert(repeatedCharacter(character, count) == solution), errorMessage

def testExtractAndExpandDigitAndChar(inputString, solution):
    # PROVIDED CODE: Don't modify
    errorMessage = f"Your code returned: {extractAndExpandDigitAndChar(inputString)}\n                  Expected string: {solution}"
    assert(extractAndExpandDigitAndChar(inputString) == solution), errorMessage


def testRunLengthEncoding(textToEncode, encodedStr):
    # PROVIDED CODE: Don't modify
    errorMessage = f"Your encoder gave: {runLengthEncoding(textToEncode)}\n                  Expected string: {encodedStr}"
    assert(runLengthEncoding(textToEncode) == encodedStr), errorMessage


def testSingleDigitRunLengthDecoding(textToDecode, decodedStr):
    # PROVIDED CODE: Don't modify
    errorMessage = f"Your decoder gave: {runLengthSingleDigitDecoding(textToDecode)}\n                  Expected string: {decodedStr}"
    assert(runLengthSingleDigitDecoding(textToDecode) == decodedStr), errorMessage


# Part 0) WarmUp Challenges
print("\nRunning Warm Up Challenges Tests....")
testRepeatedCharacter(character='a', count=2, solution="aa")
testRepeatedCharacter(character='B', count=8, solution="BBBBBBBB")
# This should should also work for very large counts (we won't deal with theis for our single digit RLE, but it's good to test to make sure your code handles it!)
testRepeatedCharacter(character='c', count=14, solution="cccccccccccccc")
testRepeatedCharacter(character='o', count=140, solution="oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")

testExtractAndExpandDigitAndChar(inputString="2a", solution="aa")
testExtractAndExpandDigitAndChar(inputString="8B", solution="BBBBBBBB")

print("🛑 TODO: Add at least 2 custom tests for either function to test your code")
# Feel free to add your own test cases!
print("✅ Part 0) Warmup Challenges looks good! ✅")


# Part 1) Encoding
print("\nRunning Part 1 Encoding Tests....")
testRunLengthEncoding(textToEncode="meet", encodedStr="1m2e1t")
testRunLengthEncoding(textToEncode="Hi", encodedStr="1H1i")
testRunLengthEncoding(textToEncode="Hello world", encodedStr="1H1e2l1o1 1w1o1r1l1d")
testRunLengthEncoding(textToEncode="python", encodedStr="1p1y1t1h1o1n")
testRunLengthEncoding(textToEncode="Tennis", encodedStr="1T1e2n1i1s")
testRunLengthEncoding(textToEncode="ABBCCCDDDDEEEEEFFFFFF", encodedStr="1A2B3C4D5E6F")

print("🛑 TODO: Add at least 2 custom tests for either function to test your code")
# Feel free to add your own test cases!
print("✅ Part 1) Encoding looks good! ✅")


# Part 2) Single Digit Decoding
print("\nRunning Part 2 Single Digit Decoding Tests....")
testSingleDigitRunLengthDecoding(textToDecode="1m2e1t", decodedStr="meet")
testSingleDigitRunLengthDecoding(textToDecode="1H1i", decodedStr="Hi")
testSingleDigitRunLengthDecoding(textToDecode="1H1e2l1o1 1w1o1r1l1d", decodedStr="Hello world")
testSingleDigitRunLengthDecoding(textToDecode="1p1y1t1h1o1n", decodedStr="python")
testSingleDigitRunLengthDecoding(textToDecode="1T1e2n1i1s", decodedStr="Tennis")
testSingleDigitRunLengthDecoding(textToDecode="1A2B3C4D5E6F", decodedStr="ABBCCCDDDDEEEEEFFFFFF")

print("🛑 TODO: Add at least 2 custom tests for either function to test your code")
# Feel free to add your own test cases!
print("✅ Part 2) Single Digit Decoding looks good! ✅")

print("Amazing you have a working single digit running length decoder! Try testing it on some more text")

# This structure tests the full flow, you should be able to encode and decode messages
originalText = """The fifty U.S. states, in alphabetical order: Alabama, Alaska, Arizona, Arkansas, California,, Colorado, Connecticut, Delaware, Florida, Georgia, Hawaii, Idaho, Illinois, Indiana, Iowa, Kansas, Kentucky, Louisiana, Maine, Maryland, Massachusetts, Michigan, Minnesota, Mississippi, Missouri, Montana, Nebraska, Nevada, New Hampshire, New Jersey, New Mexico, New York, North Carolina, North Dakota, Ohio, Oklahoma, Oregon, Pennsylvania, Rhode Island, South Carolina, South Dakota, Tennessee, Texas, Utah, Vermont, Virginia, Washington, West Virginia, Wisconsin, Wyoming"""
encodedText = runLengthEncoding(originalText)
decodedText = runLengthSingleDigitDecoding(encodedText)
assert(originalText == decodedText)

# This is a first step to the world of compression/encoding information! Learn more via Khan Academy below:
# https://www.khanacademy.org/computing/computers-and-internet/xcae6f4a7ff015e7d:digital-information/xcae6f4a7ff015e7d:data-compression/a/file-compression-introduction

# A good follow up to encoding data is the idea of encrypting data! See below for more
# https://www.khanacademy.org/computing/computers-and-internet/xcae6f4a7ff015e7d:online-data-security/xcae6f4a7ff015e7d:data-encryption-techniques/v/the-internet-encryption-and-public-keys
