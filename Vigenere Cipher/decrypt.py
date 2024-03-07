def generateKey(key,ptLen):
    modifiedKey = list(key)
    keyLen = len(key)
    
    if(keyLen == ptLen):
        return key
    
    for i in range(ptLen - keyLen):
        modifiedKey.append(modifiedKey[i % keyLen])
    key = "".join(modifiedKey)
    return key

def decrypt(cipherText, key):
    cipherTextNumbers = []
    keyNumbers = []
    plainTextNumbers = []
    plainText = []

    for c in cipherText:
        cipherTextNumbers.append((ord(c) - ord('A')) % 26)

    for c in key:
        keyNumbers.append((ord(c) - ord('A')) % 26)

    for i in range(len(cipherText)):
        plainTextNumbers.append((cipherTextNumbers[i] - keyNumbers[i % len(key)]) % 26)

    for num in plainTextNumbers:
        plainText.append(chr(num + ord('A')))

    return ''.join(plainText)


    

def main():
    fileName = input("Enter the name of the file (without extentions) :")
    key = input("Enter the key value : ")
    
    with open(fileName + "-enc.txt", 'r') as file:
        lines = file.readlines()
        cipherText = ''.join(lines)
        
    ctLen = len(cipherText)    
    key = generateKey(key,ctLen)
    plainText = decrypt(cipherText,key)

    with open(fileName + "-dec.txt", 'w') as file:
        file.write(plainText)

if __name__ =="__main__":
    main()