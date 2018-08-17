print("")
const = 65
result = ''
string = input("enter the string:")
key = input("enter the key: ")

if string.isalpha():
    for i in string:
        char_in=ord(i.upper())-const
        if key.isdecimal():
            enc_no=(char_in+int(key))%26
            result+=chr(enc_no+const)

        else:
            print('Not valid key')

    print('your encrepted text for"{}"is"{}"'.format(string.upper(),result))
