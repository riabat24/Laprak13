# def check_all_same(t): 
#     if len(t) < 1: 
#         return True # Tuple kosong dianggap semua anggota sama 
#     first_element = t[0] 
#     for element in t: 
#         if element != first_element: 
#             return False 
#     return True 

# # Contoh penggunaan 
# A = (90, 90, 90, 90) 
# tB = (10, 20, 30, 40) 
# tc = () # Tuple kosong 
# print(check_all_same(tA)) # Output: True 
# print(check_all_same(tB)) # Output: False 
# print(check_all_same(tC)) # Output: Trues



def check_all_same(t):
    if len(t) < 1:
        return True  # Tuple kosong dianggap sama semua
    first_element = t[0]
    for element in t:
        if element != first_element:
            return False
    return True

# Contoh penggunaan
A = (90, 90, 90, 90)
B = (10, 20, 30, 40)
C = ()  # Tuple kosong

print(check_all_same(A))  # Output: True
print(check_all_same(B))  # Output: False
print(check_all_same(C))  # Output: True
