def generateKey(key,ptLen):
    modifiedKey = list(key)
    keyLen = len(key)
    
    if(keyLen == ptLen):
        return key
    
    for i in range(ptLen - keyLen):
        modifiedKey.append(modifiedKey[i % keyLen])
    key = "".join(modifiedKey)
    return key