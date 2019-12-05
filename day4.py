lowerBound = 172930
upperBound = 683082

validPasswordCount = 0

def neverDecreases(password):
    prev = 0 
    for char in password:
        num = int(char)
        if num < prev:
            return False
        prev = num 

    return True 

def twoDigitsSame(password):
    twoDigitsPass = False
    threeDigitsPass = True
    twoDigitsAndNotThree = False 
    for c in range(1, len(password) - 1):
        if password[c] == password[c - 1] and password[c] == password[c + 1]:
            threeDigitsPass = False
        if password[c] == password[c - 1] or password[c] == password[c + 1]:
            twoDigitsPass = True

    return twoDigitsPass and threeDigitsPass

def maxRepeating(str): 
  
    n = len(str) 
    count = 0
    res = str[0] 
    cur_count = 1
    overallPass = False 
  
    # Traverse string except  
    # last character 
    for i in range(n): 
          
        # If current character  
        # matches with next 
        if (i < n - 1 and 
            str[i] == str[i + 1]): 
            cur_count += 1
  
        # If doesn't match, update result 
        # (if required) and reset count 
        else:
            if cur_count == 2:
                overallPass = True 
            if cur_count > count: 
                count = cur_count 
                res = str[i] 
            cur_count = 1

    return overallPass 


for i in range(lowerBound, upperBound + 1):
    p = str(i)

    if neverDecreases(p) and maxRepeating(p):
        validPasswordCount += 1


print(validPasswordCount) 
