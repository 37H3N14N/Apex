import base64

input_type = input('Enter 1 for encoding or 2 for decoding: ')
input_text = input('Enter string to transform: ')


if input_type == '1':
    byte_data = input_text.encode()
    result = base64.b64encode(byte_data)

    print('-------------------------------------')
    print(result)
    print('-------------------------------------')

if input_type == '2':
    result = base64.b64decode((input_text + '===='))

    print('-------------------------------------')
    print(result)
    print('-------------------------------------')

