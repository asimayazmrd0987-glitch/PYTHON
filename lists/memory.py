original_list = ["Inception", "Matrix", "Interstellar"]

backup_list = original_list 

backup_list.append("Avatar")

print(original_list) 
# Output: ['Inception', 'Matrix', 'Interstellar', 'Avatar'] 
# why did the original change?! Because they share the same memory.