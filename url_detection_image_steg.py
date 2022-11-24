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


lsbAsciiStr = ''.join(lsbasciiarray)

strings="sffsbdgfsdcf2342c224c4https://www.google.aaasadas"
l = list(strings)
lsbasciiarray = l + lsbasciiarray
lsbAsciiStr = strings + lsbAsciiStr
url = ''
httpFound = False
httpsFound = False
domainFound = False
httpIndex = 0
httpsIndex = 0
i = 0
j = 22
for i in range(len(lsbasciiarray)-1):
    if i >=7 and lsbAsciiStr[i-7:i] == 'http://' and (httpFound == False and httpsFound == False):
        httpFound = True
        httpIndex = i
        url = url.join(lsbasciiarray[i-7:i])
        print(url)
    if i >=8 and lsbAsciiStr[i-8:i] == 'https://' and (httpFound == False and httpsFound == False):
        httpsFound = True
        httpsIndex = i
        print(url)
        url = url.join(lsbasciiarray[i-8:i])
        print(url)
    if lsbasciiarray[i] == '.' and domainFound == False and (httpFound == True or httpsFound == True):
        for j in range(len(domain)-1):
            lowerDomain = '.'+domain[j].lower()
            if lowerDomain in lsbAsciiStr:
                domainFound = True
                k = lsbAsciiStr.find(lowerDomain)
                print(k)
                if httpFound == True:
                    url = url + (lsbAsciiStr[httpIndex:k]) + lowerDomain
                    break
                if httpsFound == True:
                    url = url + (lsbAsciiStr[httpsIndex:k]) + lowerDomain
                    break
print(url)
