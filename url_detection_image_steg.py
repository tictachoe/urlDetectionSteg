import sys
from PIL import Image, ImageOps
import numpy as np
import re

#np.set_printoptions(threshold = sys.maxsize)

domain_file = open("tlds-alpha-by-domain.txt", "r")
domain = domain_file.read()
domain = domain.split('\n')
domain_file.close()
# opening the image and reading data into numpy array
image = Image.open("Cat02.jpg")
np_img = np.array(image)

# creating a bitmap array taking each bit from the image
bitmap = []
for i in np_img:
    for j in i:
        for k in j:
            bitmap.append(np.binary_repr(k))

bitmap = np.array(bitmap)
#print(np_img)
#print(len(bitmap))
#print(i,j,k)
# print(bitmap[1])
# print(bitmap[1][0])
# print(bitmap[1][1])
# print(bitmap[1][2])
# print(bitmap[1][3])
# print(bitmap[1][4])
# print(bitmap[1][5])
# print(bitmap[1][6])
# print(bitmap[2][-1])
# print(len(bitmap))
# print(bitmap[len(bitmap)- 1])
# print(bitmap[1685])
# print(bitmap[1686])
# print(len(bitmap[0]))
# greaterthan8 = 0
# for i in bitmap:
#     if (len(i) > 8) or (len(i) < 8):
#         greaterthan8 = greaterthan8 + 1
# print(greaterthan8)

# creating an array with the least significant bits
lsbarray = []
for i in range(len(bitmap)-1):
    lsbarray.append(bitmap[i][-1])

# collecting the bits into bytes
c = 1
k = 0
lsbbytearray = []
for j in range(len(lsbarray)-1):
    #lsbbytearray
    if(c % 8 == 0):
        lsbbytearray.append(lsbarray[c-8:c])
        k += 1
    c += 1


# print(lsbbytearray[0])

# print(len(lsbarray))
# print(lsbbytearray[0])

# print(''.join(map(str,lsbbytearray[0])))
#print('{0:08b}'.format(''.join(map(str,lsbbytearray[0]))))

lsbasciiarray = []
lsbbinarray = []
lsbintarray = []
for i in lsbbytearray:
    lsbbinarray.append(''.join(map(str,i)))

for i in lsbbinarray:
    lsbintarray.append(int(i, base=2))

for i in lsbintarray:
    if (i >= 48 and i <=57) or (i >= 65 and i <= 90) or (i >= 97 and i <= 122) or (i >= 45 and i <= 46) or i == 95 or i == 126:
        lsbasciiarray.append(chr(i))
    #lsbasciiarray.append(chr(int(''.join(map(str,i)),base=2)))

# large = 0
# small = 0
# for i in lsbintarray:
#     if i > 127:
#         large += 1
#     elif i < 0:
#         small +=1
# print(large,' ',small)
# i = 0
# for i in range(len(lsbasciiarray)-1):
#     print(lsbasciiarray[i],' ',lsbintarray[i])
#print(lsbintarray)
#print(lsbasciiarray)
# print(chr(int(''.join(map(str,lsbbytearray[0])),base=2)))

# a=0s
# for i in lsbbytearray:
#     if len(i) == 8:
#         a += 1
# print(a)

# np.array(lsbarray)
# a = lsbarray.astype(int)
# print(a)

# for i in domain:
#     print (i)
print(domain[0])
print(domain[1])
print(domain[2])
print(domain[3])
print(domain[4])
#print(domain[5])

lsbAsciiStr = ''.join(lsbasciiarray)

httpFound = False
httpsFound = True
i = 0
# for i in range(len(lsbasciiarray)-1):
#     if (i-4 == 'h' and i-3 == 't' and i-2 == ' t' and i-1 == 'p' and i == ':'):
#         httpFound = True
#     # if (i-5 == 'h' and i-4 == 't' and i-3 == ' t' and i-2 == 'p' and i-1 == 's' and i == ':'):
#     #     httpsFound = True
    
# for i in domain:
#     if httpFound == True

print(type(domain))
#print(''.join(lsbasciiarray))
lsbAsciiStr = ''.join(lsbasciiarray)
print(lsbAsciiStr)
print('$Im7$$I' in lsbAsciiStr)

k = 'NIN'
url = re.findall("mkf(.*)NIN", lsbAsciiStr)

# for i in domain:
#     if (i in lsbAsciiStr):
#         url = re.search('mKf(.*)'+re.escape(k), lsbAsciiStr)

print(url)