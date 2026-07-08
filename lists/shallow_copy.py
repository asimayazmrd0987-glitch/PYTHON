original_list = ["Inception", "Matrix", "Interstellar"]

backup_list = original_list.copy()

backup_list.append("Avatar")

print(original_list) # Output: ['Inception', 'Matrix', 'Interstellar'] (safe)
print(backup_list)   # Output: ['Inception', 'Matrix', 'Interstellar', 'Avatar']