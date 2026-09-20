# file = open("1.txt", "r") # r, w(overwrite), a, x, b, t

# # content = file.read()
# # print(content)

# line1 = file.readline()
# print(line1)
# line2 = file.readline()
# print(line2)


# file = open("1.txt", "w")

# file.write("201,David,7000\n")
# file.write("202,Sara,8000\n")

# file = open("1.txt", "a")

# file.write("104,Mike,65000\n")

# file.close()

# file.write("105,Yash,75000\n")

# with open("1.txt", "a") as file:
#     # content = file.read()
#     # print(content)
#     file.write("106,Java,8777")

# print(content)

### File Pointer --> tells you where you are in the file

# with open("1.txt", "r") as file:
    # print(file.read(10)) # read first 10 chars
    # print(file.read(10)) # next 10 char

    # file.seek(13) # go to beginning
    # print(file.read(5))

    # print(file.tell())

    # for line in file:
    #     # emp_id, name, salary = line.strip().split(",") # 201,David,7000
    #     emp_id, name, salary = [ x.strip() for x in line.split(",") ]
    #     print(f"ID: {emp_id}, name: {name}, salary: {salary}")



# with open("1.txt", "r") as file:
    # lines = file.readlines()
    # line3 = lines[2]
    # print(line3.split(",")[1])

    # print(file.tell())

    # file.seek(2) # 0 start, 1, current, 2 end

# unique = set()

# with open("1.txt", "r") as file:
#     for line in file:
#         emp_id, name, salary = [ x.strip() for x in line.split(",") ]
#         record = (emp_id, name, salary)

#         if record not in unique:
#             unique.add(record)

# print(unique)

# unique = {}

# with open("1.txt", "r") as file:
#     for line in file:
#         emp_id, name, salary = [ x.strip() for x in line.split(",") ]

#         if emp_id not in unique:
#             unique[emp_id] = (name, salary)

# print(unique)


unique = set()

with open("1.txt", "r") as infile, open("unique.txt", "w") as outfile:
    for line in infile:
        normalize = tuple(x.strip() for x in line.split(","))
        print(normalize)
        if normalize not in unique:
            unique.add(normalize)
            outfile.write(line)

