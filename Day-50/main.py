# f = open('myfile.txt','r')

# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)
# num = [[55,56,57],[58,59,60],[61,62,63]]
# f = open('myfile1.txt', 'w')
# f.write(str(num))
# f.close()

# f = open('myfile1.txt','r')
# i = 0

# while True:
#     line = f.readline()
#     if not line:
#         break
#     m1 = int(line.split(",")[0])
#     m2 = int(line.split(",")[1])
#     m3 = int(line.split(",")[2])

#     print(f"marks of student {i} in maths is : {m1}")
#     print(f"marks of student {i} in english is : {m2}")
#     print(f"marks of student {i} in sst is : {m3}")

#     print(line)

# import json

# with open('myfile1.txt', 'r') as f:
#     data = json.load(f)

# for i, row in enumerate(data):
#     m1, m2, m3 = row
#     print(f"marks of student {i} in maths is : {m1}")
#     print(f"marks of student {i} in english is : {m2}")

f = open("myfile2.txt",'w')

lines = [[1,2,3],[4,5,6],[7,8,9]]

# for line in lines:
#     f.write(str(line) +'\n')

# f.close()

for i, row in enumerate(lines):
    for j , col in enumerate(row):
        print(f"at  {i} , {j} : {col}")

f.close()

