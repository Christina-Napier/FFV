import binascii
import sys
import sys
#sys.stdout=open("test.txt","w")
filename = 'images.jpg'
with open(filename, 'rb') as f:
    content = f.read()
print(binascii.hexlify(content))
hexfile =(binascii.b2a_hex(content))

print hexfile
a =(int(hexfile,16))
s = str(a)
a = int(''.join(str(i) for i in s))
it = iter(s)
for x in it:
 print(x, next(it))

#sys.stdout.close()




