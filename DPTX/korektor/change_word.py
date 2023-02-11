def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1  
        
        
# Driver code   
a = open("slowa500k_1M.txt","r")
b = open("b.txt","w+")
c = listToString(a.readlines())
c = c.replace('\n','"|"')

b.write(c)

a.close()
b.close()
