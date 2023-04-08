file_path = 'text_Chekhov2.txt'

with open(file_path, 'r', encoding='utf-8') as author_file:
    data = author_file.read()

j = 0
i=0 
for j in enumerate(data):
    i +=1

print(i)