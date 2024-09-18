def frequently(list_1):
    counter = 0
    element_frenquent= None
    list_1.sort()    
    for i in list_1:
        if list_1.count(i) > counter :
            counter = list_1.count(i)
            element_frenquent = i 
    print(element_frenquent) 

def sequence(list_2):
    if not list_2 :
        return 0
    max_length = 1 
    current_length = 1

    for i in range(1, len(list_2)): 
        if list_2[i] == list_2[i-1]:
            current_length += 1
        else :
            max_length = max(max_length, current_length)
            current_length = 1

    max_length = max(max_length, current_length)
    print(max_length)



# list_1=[1,3,5,4,1,1]   This is for the other set of number
list_1= [5,3,5,4,4,1]
list_2 = [1,2,3,4,4,2,2,2]
# list_2 = [1,2,3,4,5]

frequently(list_1)
sequence(list_2)

