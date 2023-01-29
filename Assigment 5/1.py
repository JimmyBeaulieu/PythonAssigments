# Convert a non-negative integer num to its English words representation.
# Example 1:
# Input: num = 123
# Output: "One Hundred Twenty Three"


def tensgiver(input):
    if int(input[0] + input[1]) == 0:
        return ""
    else:
        if int(input[0]) < 2:
            return str(single[int(input[0]) + int(input[1])])
        else:
            return str(tens[int(input[0])] + " " + single[int(input[1])])


def hundredgiver(input):
    if int(input[0] + input[1] + input[2]) == 0:
        return ""
    else:
        tempnum = [input[1], input[2]]
        return str(single[int(input[0])] + " Hundred " + tensgiver(tempnum))


def thousandgiver(input):
    temp = [input[0], input[1], input[2]]
    temp2 = [input[3], input[4], input[5]]
    return hundredgiver(temp) + " Thousand " + hundredgiver(temp2)


stringUserInput = input("Please enter a number (1, 2, 3): ")

single = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
          "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty",
        "Sixty", "Seventy", "Eighty", "Ninety"]

userInputSplit = []

for letter in stringUserInput:
    userInputSplit.append(letter)

intUserInput = int(stringUserInput)

if len(userInputSplit) > 7:
    print("Number too high! maximum is 9 999 999!")

else:

    if len(userInputSplit) <= 2 and intUserInput < 20:
        print(single[intUserInput])

    else:
        if len(userInputSplit) == 2:
            print(tensgiver(userInputSplit))

        if len(userInputSplit) == 3:
            print(hundredgiver(userInputSplit))

        if len(userInputSplit) == 4:
            temp = [ userInputSplit[1], userInputSplit[2], userInputSplit[3]]
            print(single[int(userInputSplit[0])] + " Thousand " + hundredgiver(temp))

        if len(userInputSplit) == 5 and int(userInputSplit[0]+userInputSplit[1]) < 20:
            temp = str(userInputSplit[2]) + str(userInputSplit[3]) + str(userInputSplit[4])
            print(single[int(userInputSplit[0] + userInputSplit[1])] + " Thousand " + hundredgiver(temp))

        if len(userInputSplit) == 5 and int(userInputSplit[0]+userInputSplit[1]) > 20:
            temp = str(userInputSplit[2]) + str(userInputSplit[3]) + str(userInputSplit[4])
            print(tensgiver(userInputSplit[0] + userInputSplit[1]) + " Thousand " + hundredgiver(temp))

        if len(userInputSplit) == 6:
            print(thousandgiver(userInputSplit))

        if len(userInputSplit) == 7:
            if int(userInputSplit[1] + userInputSplit[2] + userInputSplit[3] + userInputSplit[4] + userInputSplit[5] +
                   userInputSplit[6]) == 0:
                print(single[int(userInputSplit[0])] + " Million")
            else:
                temp = [userInputSplit[1], userInputSplit[2], userInputSplit[3], userInputSplit[4],
                        userInputSplit[5], userInputSplit[6]]
                print(single[int(userInputSplit[0])] + " Million " + thousandgiver(temp))

