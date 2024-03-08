keyMatrix = [[0] * 3 for i in range(3)]
messageVector = [[0] for i in range(3)]
cipherMatrix = [[0] for i in range(3)]

def getKeyMatrix(key):
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1

def encrypt(message, key):
    getKeyMatrix(key)
    
    for i in range(3): 
        messageVector[i][0] = ord(message[i]) % 65
    
    for i in range(3):
        cipherMatrix[i][0] = 0
        for j in range(3):
            cipherMatrix[i][0] += (keyMatrix[i][j] * messageVector[j][0])
        cipherMatrix[i][0] = cipherMatrix[i][0] % 26
   
    CipherText = []
 
    for i in range(3):
        CipherText.append(chr(cipherMatrix[i][0] + 65))

    print("Ciphertext: ", "".join(CipherText))
 
def main():
    encrypt("HELLO", "GYBNQKURP")
    
if __name__ == '__main__':
    main()
