def prime_numbers(n):
    
    for i in range(n+1):
        if i < 2:
            continue
        elif i ==2:
            print(i)
        else:
            for j in range(2,i+1):
                
                if j == i:
                    print(i)
                elif  i % j == 0:
                    break
               
                
            

                
                
    
    
def main():   
     '''
     You can test your implementations using the function calls here.
     These are here only to help you test your functions.
     '''
     prime_numbers(7)
     #prime_numbers(20)
     #prime_numbers(50)

   
################################################################ 

'''
DO NOT EDIT BELOW THIS LINE
'''
if __name__ == '__main__':
    main()
