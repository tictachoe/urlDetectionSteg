# Veranja Jayasundera for CSCI401 FALL 22
# Final Project Prof. Abouali
# Group 3
# 11/24/22 done date
from PIL import Image
import numpy as np

# opening the text file containing popular domains and reading the data
domain_file = open("tlds-alpha-by-domain.txt", "r")
domain = domain_file.read()
domain = domain.split('\n')
domain_file.close()

# opening the image and reading data into numpy array
image = Image.open("sample_640×426.bmp")
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
lsb_arr = []
for i in range(len(bitmap)-1):
    lsb_arr.append(bitmap[i][-1])

# grouping the bits into bytes
c = 1
k = 0
lsb_byte_arr = []
for j in range(len(lsb_arr)-1):
    if(c % 8 == 0):
        lsb_byte_arr.append(lsb_arr[c-8:c])
        k += 1
    c += 1

lsb_ascii_arr = []
lsb_bin_arr = []
lsb_int_arr = []

# joining the bits in the bytes together
for i in lsb_byte_arr:
    lsb_bin_arr.append(''.join(map(str,i)))

# converting the binary into int
for i in lsb_bin_arr:
    lsb_int_arr.append(int(i, base=2))

# converting the int into the ascii characters 
# found in an url: a-z A-Z 0-9 - . _ ~
for i in lsb_int_arr:
    if (i >= 48 and i <=57) or (i >= 65 and i <= 90) or (i >= 97 and i <= 122) or (i >= 45 and i <= 46) or i == 95 or i == 126:
        lsb_ascii_arr.append(chr(i))

# converting the ascii list to a string to use some functions
# exclusive to str
lsb_ascii_str = ''.join(lsb_ascii_arr)

# uncomment these lines for testing
# strings="sffsbdgfsdcf2342c224c4https://www.google.aaasadas"
# l = list(strings)
# lsb_ascii_arr = l + lsb_ascii_arr
# lsb_ascii_str = strings + lsb_ascii_str

url = ''
httpFound = False
httpsFound = False
domainFound = False
http_index = 0
https_index = 0
i = 0
j = 0

# for loop that iterates through the ascii values checking if http:// or https:// is found
# if so that position is marked and a bool is set to true. if a . is found while a http method 
# has been found and domain hasn't been found another for loop iterates through all domain values
# comparing them against lsb_ascii_str, if a domain is found all the chars between the http method
# and the domain are grouped into the str url
for i in range(len(lsb_ascii_arr)-1):
    if i >=7 and lsb_ascii_str[i-7:i] == 'http://' and (httpFound == False and httpsFound == False):
        httpFound = True
        http_index = i
        url = url.join(lsb_ascii_arr[i-7:i])
    if i >=8 and lsb_ascii_str[i-8:i] == 'https://' and (httpFound == False and httpsFound == False):
        httpsFound = True
        https_index = i
        url = url.join(lsb_ascii_arr[i-8:i])
    if lsb_ascii_arr[i] == '.' and domainFound == False and (httpFound == True or httpsFound == True):
        for j in range(len(domain)-1):
            lower_domain = '.'+domain[j].lower()
            if lower_domain in lsb_ascii_str:
                domainFound = True
                k = lsb_ascii_str.find(lower_domain)
                if httpFound == True:
                    url = url + (lsb_ascii_str[http_index:k]) + lower_domain
                    break
                if httpsFound == True:
                    url = url + (lsb_ascii_str[https_index:k]) + lower_domain
                    break
print(url)
