# def sum_of_digits(lst):
#     result = []
#     for num in lst:
#         digit_sum = 0
#         while num > 0:
#             digit_sum += num % 10 if (num % 10)% 2 == 0 else 0
#             num //= 10
#         result.append(digit_sum)
#     return result


# input_list = [202, 89, 112, 88]
# output_list = sum_of_digits(input_list)
# print(output_list) 


    

#check if array is subset of another array or not . if the arr2 contains elements mwhich are there in arr1 then it is a sunset of an array
#arr1 = [1, 2, 3, 4, 5]
#arr2 = [2,4,3,1,7,5,15]
list1 = [ ]
list2 = [2,4,3,1,7,5,15]
# flag = True
# for i in list1:
#     if i not in list2:
#         flag = False
#         print("not a subset of")
#         break
    
#     if flag == True:
#         print("is a subset of")
        
def is_subset(list1, list2):
    return set(list1).issubset(set(list2))

list1 = [1, 3, 4, 5, 2,99]
list2 = [2, 4, 3, 1, 7, 5, 15]

if is_subset(list1, list2):
    print("arr1 is a subset of arr2")
else:
    print("arr1 is not a subset of arr2")
  
    
    
    