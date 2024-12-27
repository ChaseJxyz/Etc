# Check allow list txt file for IP addresses that need removing/removes them if found/updates txt file
# Assumes allow list has no duplicates

# Specify allow list
import_file = "allow_list.txt"

# Specify remove list
remove_list = ["foo","bar"]

# Import allow list txt to Python + convert str to list
with open(import_file,"r") as file:
    ip_addresses = file.read()

ip_addresses = ip_addresses.split()

# Updating script
for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)

# Turning list back into string + file writing
ip_addresses = "\n".join(ip_addresses)

with open(import_file,"w") as file:
    file.write(ip_addresses)