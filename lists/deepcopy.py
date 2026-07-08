import copy 

server_configs = [
    ["Web_Server", "Nginx"], 
    ["Database", "PostgreSQL"]
]
backup_configs = copy.deepcopy(server_configs)

backup_configs[0][1] = "Apache"

print(server_configs)
# Output: [['Web_Server', 'Nginx'], ['Database', 'PostgreSQL']] 
# The original is perfectly safe. Complete memory isolation.