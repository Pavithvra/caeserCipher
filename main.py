alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

import art

print(art.logo)


def encode(word, shift, continue_choice):
    encode_text = ""
    for i in word:
        if i in alphabet:
            position = alphabet.index(i)
            new_position = position + shift
            if new_position > 25:
                new_position = new_position - 26
            encode_text += alphabet[new_position]
        else:
            encode_text += i
    print(f"The encoded text is {encode_text}")
    # choice=input("Do you want to encode or decode? Type 'Yes' or 'No' \n").lower()
    # if choice=="No":
    #   continue_choice = False


def decode(word, shift, continue_choice):
    decode_text = ""
    for i in word:
        if i in alphabet:
            position = alphabet.index(i)
            new_position = position - shift
            if new_position < 0:
                new_position = new_position + 26
            decode_text += alphabet[new_position]
        else:
            decode_text += i
    print(f"The decoded text is {decode_text}")


continue_choice = True
while continue_choice:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    word = input(f"Enter the word to be {direction}: ")
    shift = int(input("Enter the shift number: "))

    if direction == "encode":
        encode(word, shift, continue_choice)
        choice = input("Do you want to encode or decode? Type 'Yes' or 'No' \n").lower()
        if choice == "no":
            continue_choice = False
    else:
        decode(word, shift, continue_choice)
        choice = input("Do you want to encode or decode? Type 'Yes' or 'No' \n").lower()
        if choice == "no":
            continue_choice = False
