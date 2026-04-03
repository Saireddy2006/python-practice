def find_median_sorted_array(list1, list2):
    final_list = sorted(list1 + list2)
    length_final_list = len(final_list)
    mid_value = length_final_list//2
    n = length_final_list
    if n%2 == 1:
        return final_list[mid_value]
    else:
        return (final_list[mid_value - 1] + final_list[mid_value])/2
    
list1 = [1, 2]
list2 = [7, 10]
print(find_median_sorted_array(list1, list2))