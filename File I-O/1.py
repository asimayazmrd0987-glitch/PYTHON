f = open("/mnt/sda4/5 Goal_Dream_Aim/PYTHON/File I-O/1.txt", "r")
gui = f.readline()
print(gui)

gui2= f.readline()
print(gui2)
f.close()
# /mnt/cfc2943f-24ee-4835-9138-678eac423d3c/5 Goal_Dream_Aim/PYTHON/File I-O/1.py --> this is fedora

#     open(filename, mode, encoding)

#     # MODES
#     "r"   # read only (default)         — file must exist
#     "w"   # write only                  — creates file, WIPES if exists
#     "a"   # append                      — creates file, adds to end
#     "x"   # exclusive create            — fails if file already exists
#     "r+"  # read AND write              — file must exist
#     "w+"  # read AND write              — wipes existing content

#     # Binary versions (images, PDFs, executables)
#     "rb"  # read binary
#     "wb"  # write binary