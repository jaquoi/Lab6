def encode(userinput):
    num = userinput
    new = ""
    for element in num:
        element = int(element)
        element += 3
        new += str(int(element))
    print(new)


def main():
    print("\n"
          "Menu\n"
          "-------------\n"
          "1. Encode\n"
          "2. Decode\n"
          "3. Quit\n"
          "\n")
    user = input("Please enter an option: ")
    while True:
        if user == "1":
            userinput = input("Please enter your password to encode: ")
            print(encode(userinput))
            print("Your password has been encoded and stored!")
        if user == "2":
            pass
        if user == "3":
            break


if __name__ == "__main__":
    main()