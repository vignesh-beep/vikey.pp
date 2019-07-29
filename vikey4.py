def printString(strn, ch, count): 
    occ, i = 0, 0
  
    
    if (count == 0): 
        print(strn) 
  
     
    for i in range(len(strn)): 
  
          
        
        if (strn[i] == ch): 
            occ += 1
  
        
        
        if (occ == count): 
            break
  
    
    
    if (i < len(strn)- 1): 
        print(strn[i + 1: len(strn) - i + 2]) 
  
    
    else: 
        print("Empty string") 
