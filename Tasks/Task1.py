def no_duplicates(in_list):
    unique = set()  #O(1)
    out_list = []   # O(1)
    for i in in_list:  # O(len(in_list))
        if not (i in unique):  #O(1)
            out_list.append(i) #O(1)
            unique.add(i) #O(1)
    return out_list

#Resulting complexity is O(N), where N is the legth of the input list.