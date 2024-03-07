
def generateKey(key,ptLen):
    modifiedKey = list(key)
    keyLen = len(key)
    
    if(keyLen == ptLen):
        return key
    
    for i in range(ptLen - keyLen):
        modifiedKey.append(modifiedKey[i % keyLen])
    key = "".join(modifiedKey)
    return key
   
def main():
    key = input("Enter the key value : ")
    #plainText = "Hello World"

    with open('input.txt', 'r') as file:
        lines = file.readlines()
        plainText = ''.join(lines)
    print(plainText)

    
    ptLen = len(plainText)    
    key = generateKey(key,ptLen)
    print(f"The modified key is : {key}") 
    print(f"The length of the key is : {len(key)}")
    print(f"The length of the plain text is : {ptLen}")  
    
if __name__ =="__main__":
    main()