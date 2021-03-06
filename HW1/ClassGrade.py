
# =============================================================================
# ClassGrade
# =============================================================================
#  

def drop_minimum(grade1, grade2, grade3):
    
    if grade1<grade2 and grade2<grade3:
        av1 = (grade2 + grade3) / 2 
        
    elif grade2<grade1 and grade2<grade3:
         av1 = (grade1 + grade3) / 2 
    else:
        av1 = (grade2 + grade1) / 2 
        
    return (av1)

    
    
def change_weights(grade1, grade2, grade3):
    av2 = grade1 * 0.45 + grade2 * 0.3 + grade3 * 0.25
    return (av2)



def compare_results(av1, av2):
    
    max_point = 0
    if av1 < av2:
        max_point = av2
    else:
        max_point = av1
        
    return (max_point)


def main():
    '''
    You can test your implementations using the function calls here.
    These are here only to help you test your functions.
    What matters is whether your drop_minimum, change_weights and 
    compare_results functions are correct.
    '''
    grade1= float(input("grade1:"))    
    grade2= float(input("grade2:"))
    grade3= float(input("grade3:"))
    av1 = drop_minimum(grade1,grade2,grade3)
    av2 = change_weights(grade1,grade2,grade3)
    result = compare_results(av1,av2)
    print('Result for drop_minimum is',av1)
    print('Result for change_weights is',av2)
    print('Final grade is',result)
    

################################################################ 

'''
DO NOT EDIT BELOW THIS LINE
'''
if __name__ == '__main__':
    main()


