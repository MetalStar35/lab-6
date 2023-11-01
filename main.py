# pwd
# cd documents
# cd lab-6
# get add
# get commit "explain what you did"
# get push
# this will update the versions.

def encode_password(user_password):
    # set encoded password blank
    encoded_password = ""
    for digit in str(user_password):
        # add 3 to the digit but if greater than 6 we have to make seperate rules
        encoded_digit = str((int(digit) + 3) % 10)  # use modulo division to keep it less than or equal to 9
        # add the new digit into the new encoded password
        encoded_password += encoded_digit
    return encoded_password


def decode_password(encoded):
    OG_password = ""
    for digit in str(encoded):
        # subtract 3 from the digit
        password_digit = str((int(digit) - 3) % 10)  #modulo division is still needed so the returned pasword will not be negative
        # add the new digit into the new decoded password
        OG_password += password_digit
    return OG_password


def menu():
    user_option = ""
    encoded = ""
    while user_option != "3":
        print("Menu")
        print("-------------")
        print("1. Encode\n2. Decode\n3. Quit")
        print("")
        print("")

        user_option = input("Please enter an option: ")
        if user_option == "1":
            user_password = input("Enter the password to encode: ")
            encoded = encode_password(user_password)  # Store the encoded password
            print("Your password has been encoded and stored!")
            print("")
            encode_password(user_password)
        if user_option == "2":
            decoded = decode_password(encoded)
            print("The encoded password is " + encoded + " and the original password is " + decoded + ".")
            print("")
        if user_option == "3":
            break

# exampleeeeee



menu()