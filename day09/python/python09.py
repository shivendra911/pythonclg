# f = open("day09/python/hello.txt", "r+")
# content = f.read()

# f.seek(0)          # move pointer to start
# f.write("this is new input from python09.py")
# f.truncate()       # remove leftover old content

# print(content)
# f.close()

# f = open("day09/python/hello.txt", "a+")
# f.write("\nthis is third input from python09.py")
# f.seek(0)
# content = f.read()
# print(content)

# with open("day09/python/hello.txt", "r") as f:
#     data = f.read()
# print(data)

# with open("day09/python/hello.txt", "r") as f:
#     for line in f:
        
#         print(line.strip())


# import os
# check = os.path.exists("day09/python/hello.txt")
# # print(check)
# if check:
#     print("file found")
# else:
#     print("file not found")

# import os
# check = os.path.exists("day09/python/hello1.txt")
# if check:
#     os.rename("day09/python/hello1.txt", "day09/python/hello2.txt")
#     print("file renamed")
# else:
#     print("file not found")

# import os
# check = os.path.exists("day09/python/hello2.txt")
# if check:
#     os.remove("day09/python/hello2.txt")
#     print("file deleted")
# else:
#     print("file not found")


# #using binary mode
# f = open("day09/python/catimg.png", "rb")
# data = f.read()
# print(data)
# f.close()


def detect_file_type(path):
    with open(path, "rb") as f:
        header = f.read(8)

    if header.startswith(b"\x89PNG"):
        return "PNG image"
    elif header.startswith(b"\xFF\xD8\xFF"):
        return "JPEG image"
    elif header.startswith(b"%PDF"):
        return "PDF document"
    elif header.startswith(b"PK\x03\x04"):
        return "ZIP archive"
    elif header.startswith(b"MZ"):
        return "Windows EXE"
    elif header.startswith(b"\x7fELF"):
        return "Linux ELF binary"
    else:
        return "Unknown file type"
    
file_path = "day09/python/hello.txt"
file_type = detect_file_type(file_path)
print(f"The file type of '{file_path}' is: {file_type}")
