import sys
from PIL import Image, ImageOps
import numpy as np
import re

#np.set_printoptions(threshold = sys.maxsize)

# opening the text file containing popular domains and reading the data
domain_file = open("tlds-alpha-by-domain.txt", "r")
domain = domain_file.read()
domain = domain.split('\n')
domain_file.close()

# opening the image and reading data into numpy array
image = Image.open("Cat02.jpg")
np_img = np.array(image)
image.close()

# creating a bitmap array by reading each bit from the image
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

# grouping the bits into bytes
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

# joining the bits in the bytes together
for i in lsbbytearray:
    lsbbinarray.append(''.join(map(str,i)))

# converting the binary into int
for i in lsbbinarray:
    lsbintarray.append(int(i, base=2))

# converting the int into the ascii characters 
# found in an url: a-z A-Z 0-9 - . _ ~
for i in lsbintarray:
    if (i >= 48 and i <=57) or (i >= 65 and i <= 90) or (i >= 97 and i <= 122) or (i >= 45 and i <= 46) or i == 95 or i == 126:
        lsbasciiarray.append(chr(i))

print(lsbbytearray[0:10])
print(lsbasciiarray[0:10])
print(lsbbinarray[0:10])
print(lsbintarray[0:10])

# converting the ascii list to a string to use some functions
# exclusive to str
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
j = 0

# for loop that iterates through the ascii values checking if http:// or https:// is found
# if so that position is marked and a bool is set to true. if a . is found while a http method 
# has been found and domain hasn't been found another for loop iterates through all domain values
# comparing them against lsbAsciiStr, if a domain is found all the chars between the http method
# and the domain are grouped into the str url
for i in range(len(lsbasciiarray)-1):
    if i >=7 and lsbAsciiStr[i-7:i] == 'http://' and (httpFound == False and httpsFound == False):
        httpFound = True
        httpIndex = i
        url = url.join(lsbasciiarray[i-7:i])
    if i >=8 and lsbAsciiStr[i-8:i] == 'https://' and (httpFound == False and httpsFound == False):
        httpsFound = True
        httpsIndex = i
        url = url.join(lsbasciiarray[i-8:i])
    if lsbasciiarray[i] == '.' and domainFound == False and (httpFound == True or httpsFound == True):
        for j in range(len(domain)-1):
            lowerDomain = '.'+domain[j].lower()
            if lowerDomain in lsbAsciiStr:
                domainFound = True
                k = lsbAsciiStr.find(lowerDomain)
                if httpFound == True:
                    url = url + (lsbAsciiStr[httpIndex:k]) + lowerDomain
                    break
                if httpsFound == True:
                    url = url + (lsbAsciiStr[httpsIndex:k]) + lowerDomain
                    break
print(url)
