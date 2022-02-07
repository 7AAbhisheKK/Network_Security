import pyDes
import matplotlib.pyplot as plt
def bitDifference(a,b):                   #Function to calculate Hamming Distance
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count = count +1
    return count

def getOnebitDifferString(s):            # get string differ by one bit(just next character)
    temp = ""
    for j in range(len(s)):
        if j == 0:
            t = int(ord(s[0])+1)
            if t > ord('z'):
                t = ord('a')
            x = t
            temp = temp + chr(x)
        else:
            temp = temp + s[j]
    print(temp,"temp is here")
    return temp


## 5 different plaintext
plot1 = {}
x = set()
key = "qazwsxed"
plaintext_list = ['abcdefgh','adcdefgh','aecdefgh','afcdefgh','agcdefgh']
for plaintext in plaintext_list:
    a = pyDes.des(key)
    ciphertext = a.encrypt(plaintext)
    bit_ciphertext_ref = a.String_to_BitList(ciphertext)
    temp = []
    text = plaintext
    for i in range(1,17):
        text = getOnebitDifferString(text)     ##get a string which is one bit different from previous one
        a = pyDes.des(key)                      
        b = a.encrypt(text)
        bit_ciphertext = a.String_to_BitList(b)
        differ = bitDifference(bit_ciphertext_ref,bit_ciphertext)    ##calculating hamming distance
        temp.append([i,differ])                                     ##storing hamming distance
    plot1[plaintext] = temp
for plot_plain in plaintext_list:
    print(plot1[plot_plain])
    plt.boxplot(plot1[plot_plain])
    plt.title("for plaintext "+ plot_plain)
    plt.ylabel("Hamming Distance")
    plt.xlabel("Rounds")
    plt.show()


#5 different key
key_list = ['abcdefgh','adcdefgh','aecdefgh','afcdefgh','agcdefgh']
plaintext = "plmoknij"
plot2 ={}
for key in key_list:
    a = pyDes.des(key)
    ciphertext = a.encrypt(plaintext)
    bit_ciphertext_ref = a.String_to_BitList(ciphertext)
    temp = []
    text = key
    for i in range(1,17):
        text = getOnebitDifferString(text)              ##get a string which is one bit different from previous one
        a = pyDes.des(text)
        b = a.encrypt(plaintext)
        bit_ciphertext = a.String_to_BitList(b)
        differ = bitDifference(bit_ciphertext_ref,bit_ciphertext)    ##calculating hamming distance
        temp.append([i,differ])                                     ##storing hamming distance
    plot2[key] = temp

for key in key_list:
    print(plot2[key])
    plt.boxplot(plot2[key])
    plt.title("for Key " +key)
    plt.ylabel("Hamming Distance")
    plt.xlabel("Rounds")
    plt.show()



##5 different hamming distance
hamming_distance = [1,2,3,4,5]

plaintext = "abcdefgh"
key = "plmoknij"
plot3 ={}
for h in hamming_distance:
    a = pyDes.des(key)
    ciphertext = a.encrypt(plaintext)
    bit_ciphertext_ref = a.String_to_BitList(ciphertext)
    temp = []
    text = key
    for i in range(1,17):
        for i in range(h):                            # for h hamming distance we need to make h changes in the previous string
            text = getOnebitDifferString(text)
        a = pyDes.des(key)
        b = a.encrypt(text)
        bit_ciphertext = a.String_to_BitList(b)
        differ = bitDifference(bit_ciphertext_ref,bit_ciphertext)   ##calculating hamming distance
        temp.append([i,differ])                                     ##storing hamming distance
    plot3[h] = temp
for h in hamming_distance:
    plt.boxplot(plot3[h])
    plt.title("for hamming distance " + str(h))
    plt.ylabel("Hamming Distance")
    plt.xlabel("Rounds")
    plt.show()
