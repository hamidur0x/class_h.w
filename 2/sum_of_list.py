def sum_of_list(lst):
    return sum(lst)

nums = input("Enter numbers separated by spaces: ")
lst = [int(x) for x in nums.split()]
print("Sum:", sum_of_list(lst))
