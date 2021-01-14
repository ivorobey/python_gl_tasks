# Find the anonymous function in the given array and use the function to process the rest members of array (like map does)

# find_function([lambda a: a+2,9,3,1,0]) # [11,5,3,2]
# find_function([9,3,lambda a: a/2.0,1,0]) #[4.5,1.5,0.5,0.0]

# Итого: есть лист, в нём один из элементов (неизвестно какой именно) - lambda функция. Её надо найти и использовать на всех остальных элементах списка.

# from inspect import isfunction


def find_lambda(*args, **kwargs):
    
    for i in args:
        for lam in i:
            print(lam,'----')
            for j in lam:
                if hasattr(j, '__call__'):
                    print(j)
            list(map(j,lam))  
            
   
     

print(find_lambda([lambda a: a+2, 9, 3, 1, 0]))  # [11, 5, 3, 2]
# print(find_lambda([9, 2, 3, lambda a: a/2.0, 1, 0]))  # [4.5, 1, 1.5, 0.5, 0.0]




# lst=[9,3,1,0]
# print(list(map(lambda a:a+2,lst)))



