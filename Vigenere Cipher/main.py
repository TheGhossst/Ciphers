
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
    plainTextNumbers = []
    keyNumbers = []
    cipherTextNumbers = []
    cipherText = []
    
    for c in plainText:
        plainTextNumbers.append((ord(c) - ord('A')) % 26)
    print("Plaintext numbers:", plainTextNumbers)

    for c in key:
        keyNumbers.append((ord(c) - ord('A')) % 26)
    print("Key numbers:", keyNumbers)
    
    for i in range(len(plainText)):
        cipherTextNumbers.append((plainTextNumbers[i] + keyNumbers[i % len(key)]) % 26)
    
    for num in cipherTextNumbers:
        cipherText.append(chr(num + ord('A')))
    print(cipherText)
    
    return ''.join(cipherText)
    
    
def main():
    key = input("Enter the key value : ")
    
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        plainText = ''.join(lines)
    print(plainText)

    #plainText = plainText.upper()
    ptLen = len(plainText)    
    key = generateKey(key,ptLen)
    #key = key.upper()
    print(f"The modified key is : {key}") 
    print(f"The length of the key is : {len(key)}")
    print(f"The length of the plain text is : {ptLen}")  
    
    cipherText = encrypt(plainText,key)
    print(cipherText)
   
if __name__ =="__main__":
    main()