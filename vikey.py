def find_n_smooth(L, R): 
      
     
     
    global n_smooth 
    if L <= n_smooth[-1]: 
          
         
         
        for w in n_smooth : 
            if w > R : break
            if w >= L and w <= R : 
                  
                
                print(w, end =" ") 
                  
        print() 
