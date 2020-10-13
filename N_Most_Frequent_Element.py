# -*- coding: utf-8 -*-
"""
Data Assessment 
Question 3d

@author: Philip
"""
def n_most_frequent(str_array):
    
    print("Given array:", str_array)
    #show the array given. 

    N = int(input("Enter the value of N:"))
    #input the N 
    
    n_unique_element = len(set(str_array))
    #calculate the number of unique element
    
    if(1 <= N <= n_unique_element):
        
        freq_element_array = []
        #create an empty array
    
        for x in range(1, N+1):
            freq_element = max(set(str_array), key = str_array.count)
            #get the most recurring element in current array
            
            freq_element_array.append(freq_element)
            #add the most recurring element in new array, freq_element_array
            
            while freq_element in str_array: str_array.remove(freq_element)
            #remove the most recurring element from array given
            
        return print("{a} are the {b} most recurring strings.\n".format(a=freq_element_array, b=N))
        
    else:
        print("Invalid value N, please try again")
        return n_most_frequent(str_array)
    

str_array = ["malaysia", "singapore", "usa", "malaysia", "singapore", "korea"]
n_most_frequent(str_array)


str_array = ["do", "you", "like", "apple", "do", "do", "do", "apple", "like", "like"]
n_most_frequent(str_array)

