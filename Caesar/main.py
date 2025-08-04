alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt_or_decrypt(type, message, shift):
    code = ""
    if type == "encode":
        for i in message:
            if i in alphabet:
                tmp = (alphabet.index(i) + shift) % 26
                code += alphabet[tmp]
            else:
                code += i
        print(f"암호화한 코드는: {code} 입니다.")
    elif type == "decode":
        for i in message:
            if i in alphabet:
                tmp = (alphabet.index(i) - shift) % 26
                code += alphabet[tmp]
            else:
                code += i
        print(f"해독된 코드는: {code} 입니다.")
    else:
        print("올바르지 않은 타입입니다.")

answer = 'yes'

while answer == 'yes':
    encode_or_decode = input("type input(encode or decode): ")
    message_input = input("input message: ").lower()
    shift_num = int(input("input shift number: "))
    encrypt_or_decrypt(type=encode_or_decode, message=message_input, shift=shift_num)
    answer = input("더 진행하시겠습니까?(yes, no): ")

