
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt(massage_e, shift_e):
    encode_massage = ""
    for letter in massage_e:

        if letter == " ":
            encode_massage += " "
        else:
            letter_index = alphabet.index(letter)
            encode_massage += alphabet[(letter_index + shift_e)%26]
    return encode_massage

def decode(massage_d, shift_d):
    decode_massage = ""
    for letter in massage_d:

        if letter == " ":
            decode_massage += " "
        else:
            letter_index = alphabet.index(letter)
            decode_massage += alphabet[(letter_index - shift_d)%26]
    return decode_massage




operation_choice = input(r"Type 'encode' to encrypt, type 'decode' to decrypt: ")
if operation_choice == "encode":
    massage = input("Enter a massage to encode: ")
    shift = int(input("Enter shift value: "))
    encode_massage = encrypt(massage, shift)
    print(f"Encrypted massage: {encode_massage}")

elif operation_choice == "decode":
    message = input("Enter a message to decode: ")
    shift = int(input("Enter shift value: "))
    decode_massage = decode(message, shift)
    print(f"Decrypted massage: {decode_massage}")


