
def generateKey(key,ptLen):
    modifiedKey = list(key)
    keyLen = len(key)
    
    if(keyLen == ptLen):
        return key
    
    for i in range(ptLen - keyLen):
        modifiedKey.append(modifiedKey[i % keyLen])
        
    key = "".join(modifiedKey)
    return key

def encrypt(plainText, key):
    plainText = plainText.replace(' ', '')
    key = generateKey(key,len(plainText))
    plainTextNumbers = []
    keyNumbers = []
    cipherTextNumbers = []
    cipherText = []
    
    for c in plainText:
        plainTextNumbers.append((ord(c) - ord('A')) % 26)

    for c in key:
        keyNumbers.append((ord(c) - ord('A')) % 26)
    
    for i in range(len(plainText)):
        cipherTextNumbers.append((plainTextNumbers[i] + keyNumbers[i % len(key)]) % 26)
    
    for num in cipherTextNumbers:
        cipherText.append(chr(num + ord('A')))
    
    
    return ''.join(cipherText)
    
    
def main():
    fileName = input("Enter the name of the file (without extentions) :")
    key = input("Enter the key value : ")
    
    with open(fileName + ".txt", 'r') as file:
        lines = file.readlines()
        plainText = ''.join(lines)
    
    cipherText = encrypt(plainText,key)

    with open(fileName + "-enc.txt", 'w') as file:
        file.write(cipherText)

if __name__ =="__main__":
    main()