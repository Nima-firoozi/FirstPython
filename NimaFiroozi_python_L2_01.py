import getpass

FinalScore = 0
commonPasswords = ["123456", "12345678", "12345", "111111", "123456789", "qwerty", "asdfgh", "zxcvbnm", "password", "admin", "P@s$w0rd"]
LowwerAlphabet = "abcdefghijklmnopqrstuvwxyz"
UpperAlphabet = LowwerAlphabet.upper()
SpecialCharacter = "@!$"

#never give up


user = {
    "userName" : "",
    "password" : "",
    "birthday" : ""
}

user["userName"] = input("Please enter your username:")
while not user["userName"]:
    print("⚠️ Username cannot be empty. Please try again.")
    user["userName"] = input("Please enter your username:\n")




user["password"] = getpass.getpass("Please enter your password:")
while not user["password"]:
    print("⚠️ password cannot be empty. Please try again.")
    user["password"] = getpass.getpass("Please enter your password:\n")


user["birthday"] = input("Please enter your birthday:")
while not user["birthday"]:
    print("⚠️ birthday cannot be empty. Please try again.")
    user["birthday"] = input("Please enter your birthday:\n")


print("\nFilter checks:\n")


if len(user["password"]) < 8:
    print("❌ Password is shorter than 8 characters.")
else:
    print("✅ Password is 8 characters or longer.")
    FinalScore += 1


for i in range(len(LowwerAlphabet)):

    find = False

    for j in range(len(user["password"])):
        
        if user["password"][j] == LowwerAlphabet[i]:
            find = True
            print("✅ Password contains English letters.")
            FinalScore +=1
            break

    if find:
        break

    if i == len(LowwerAlphabet)-1:
        print("❌ Password does not contain any English letters.")  


for i in range(len(SpecialCharacter)):

    find = False

    for j in range(len(user["password"])):
        
        if user["password"][j] == SpecialCharacter[i]:
            find = True
            print("✅ Password contains special characters.")
            FinalScore +=1
            break

    if find:
        break
    
    if i == len(SpecialCharacter)-1:
        print("❌ Password does not contain any special characters.")


for i in range(len(UpperAlphabet)):

    find = False

    for j in range(len(user["password"])):
        
        if user["password"][j] == UpperAlphabet[i]:
            find = True
            print("✅ Password contain uppercase letters.")
            FinalScore +=1
            break

    if find:
        break
    
    if i == len(UpperAlphabet)-1:
        print("❌ Password does not contain any uppercase letters.")


if user["userName"] == user["password"]:
    print("❌ Password is identical to the username.")
else:
    print("✅ Password is not identical to the username.")
    FinalScore += 1

if user["userName"] == user["password"].swapcase():
    print("❌ Password is the swapcase version of the username.")
else:
    print("✅ Password is not the swapcase version of the username.")
    FinalScore += 1

if len(user["password"]) == len(user["userName"]) and user["userName"] != user["password"]:

    isMatch = True
    isSpecial = False
    
    for i in range(len(user["password"])):

        if user["password"][i] == "@":

            if user["userName"][i] == "a" :
                isSpecial = True
            elif user["userName"][i] != "@":
                isMatch = False
                break

        elif user["password"][i] == "$":

            if user["userName"][i] == "s" :
                isSpecial = True
            elif user["userName"][i] != "$":
                isMatch = False
                break

        elif user["password"][i] == "!":

            if user["userName"][i] == "i" :
                isSpecial = True
            elif user["userName"][i] != "!":
                isMatch = False
                break

        elif user["password"][i] == "a":
            if user["userName"][i] == "@" :
                isSpecial = True
            elif user["userName"][i] != "a":
                isMatch = False
                break
        
        elif user["password"][i] == "s":
            if user["userName"][i] == "$" :
                isSpecial = True
            elif user["userName"][i] != "s":
                isMatch = False
                break
        
        elif user["password"][i] == "i":
        
            if user["userName"][i] == "!" :
                isSpecial = True
            elif user["userName"][i] != "!":
                isMatch = False
                break

        elif user["password"][i] == "0":
                
            if user["userName"][i] == "o" :
                isSpecial = True
            elif user["userName"][i] != "0":
                isMatch = False
                break

        elif user["password"][i] == "o":
                
            if user["userName"][i] == "0" :
                isSpecial = True
            elif user["userName"][i] != "o":
                isMatch = False
                break

        elif user["userName"][i] != user["password"][i]:
            isMatch = False
            break

    if (isMatch) and (isSpecial):
        print("❌ Is a special-character version of the username")
    else:
        print("✅ Is not a special-character version of the username")
        FinalScore += 1

    
else:
    print("✅ Is not a special-character version of the username")
    FinalScore += 1


for i  in range(len(commonPasswords)):

    if commonPasswords[i] == user["password"]:
        print("❌ Password is one of the most common passwords.")
        break
    elif i == len(commonPasswords)-1:
        print("✅ Password is not one of the most common passwords.")
        FinalScore += 1


if user["password"].find(user["birthday"]) != -1:
    print("❌ Password contains your birth year.")
else:
    print("✅ Password does not contain your birth year.")
    FinalScore += 1


print("\n",f"🔐 Final Score: {FinalScore} out of 9")

if FinalScore == 0:
    level = "Very Weak"
elif FinalScore == 1:
    level = "Weak"
elif FinalScore == 2:
    level = "Fair"
elif FinalScore == 3:
    level = "Moderate"
elif FinalScore == 4:
    level = "Average"
elif FinalScore == 5:
    level = "Good"
elif FinalScore == 6:
    level = "Strong"
elif FinalScore == 7:
    level = "Very Strong"
elif FinalScore == 8:
    level = "Excellent"
elif FinalScore == 9:
    level = "Perfect"

print(f"🔒 Security Level: {level}")

if FinalScore <= 2:
    print("⚠️ Your password is weak. Please consider improving it based on the checks above.")
elif FinalScore < 9:
    print("👍 Your password is decent, but could still be improved.")
else:
    print("🎉 Congratulations! Your password is highly secure and passed all security checks.")
