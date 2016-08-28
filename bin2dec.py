import binascii

def jpeg_to_decimal(jpeg_loc, as_rgb=True):
    '''
    Takes the location of a jpeg and returns it as a list of decimal values.

    :param jpeg_loc: The location of the Jpeg to read
    :param as_rgb: If True, returns rgb tuples.
    :return: A list of decimals representing the jpeg.
    '''
    with open(jpeg_loc, 'rb') as f:
        content = f.read()

    hex = binascii.b2a_hex(content)
    str_hex = str(hex)[2:]  # Skip the first 2 chars as its the binary flag.
    split_string_hex = map(''.join, zip(*[iter(str_hex)]*2))

    decimal_values = []
    for s in split_string_hex:
        dec = int(s, 16)
        decimal_values.append(dec)
    if as_rgb:
        return zip(*[decimal_values[i::3] for i in range(3)])  # This branch gives an iterable
    else:
        return decimal_values # This branch gives a list


jpeg_to_decimal(r'C:\Users\Alex\Downloads\images.jpg')
