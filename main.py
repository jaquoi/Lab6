def encode(userinput):
    num = userinput
    new = ""
    for element in num:
        element = int(element)
        element += 3
        new += str(int(element))
    return new

def decode(encoded_pass): #Zara Haruna
    old = " "
    for num in encoded_pass: # Subtracts 3 from each digit in encoded password
        num = str(int(num) - 3)
        old += num # Concatenates new digits together in empty string
    return old

def main():

    while True:
        print("Menu\n"
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit\n")
        user = input("Please enter an option: ")
        if user == "1":
            global userinput # Allows original password to be applied to the encode and decode functions
            userinput = input("Please enter your password to encode: ")
            print(encode(userinput))
            print("Your password has been encoded and stored!")
        if user == "2":
            print(f"The encoded password is {encode(userinput)}, and the original password is{decode(encode(userinput))}.")
        if user == "3":
            break


if __name__ == "__main__":
    main()