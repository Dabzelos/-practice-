import matplotlib.pyplot as plt
import numpy as np

#data test
""" 
with open("input_data.txt", 'r', encoding='utf-8') as data_file:
    data = data_file.read()
   
    amount_of_speach_const = 0
    sentences = 0
    word_count = 0
    other_chars = 0
    med_len_of_sentences = 0

    for j, char in enumerate(data):
        if char == ",":
            amount_of_speach_const += 1
        elif char in ".!?":
            sentences += 1
        elif char in " \n":
            word_count += 1
        else:
            other_chars += 1
        
        prev_char = data[j-1]
        if (prev_char in ' \n') and (char in ' -–—\n'):
            word_count -= 1
 
    
    med_len_of_word = round(other_chars / word_count, 2)
    med_len_of_sentences = round(other_chars/sentences, 3)  
   
 """

def read_data(file):
    x_values = []
    y_values = []
    for line in file:
        x, y = map(float, line.split(sep=' '))

        x_values.append(x)
        y_values.append(y)
    return x_values, y_values


with open("res_text_Chekhov.txt", "r") as chekhov_file:
    X1, Y1 = read_data(chekhov_file)

with open("res_text_Tolstoy.txt", "r") as tolstoy_file:
    X2, Y2 = read_data(tolstoy_file)


"""def line_coeff(X1: list, Y1: list, X2: list, Y2: list):
    best_k = 0
    best_b = 0
    max_cnt = 0
    cnt_1 = 0
    cnt_2 = 0
    cnt = 0
    
    range_of_coeff = [x / 10 for x in range(-2000, 2000+1)]
    for k in range_of_coeff:
        for b in range_of_coeff:
            for i in range(len(X1)):
                
                if (Y1[i] < ((k*X1[i])+b)):
                    cnt_1 +=1
                
                if (Y2[i] >((k*X2[i])+b)):
                    cnt_2 +=1
                cnt = cnt_1+cnt_2
                if (cnt >=max_cnt):
                    max_cnt= max(max_cnt, cnt)
                    best_b = b
                    best_k = k
                if cnt >2:
                    print(cnt, best_k, best_b)
                cnt_1 = 0
                cnt_2 = 0
                cnt = 0


    return best_k, best_b
k, b = line_coeff(X1, Y1, X2, Y2)
print('end')
print(k,b)
x = np.linspace(-5,5,100)

print(k,b)
"""
"""x*2.741)-2.997""" """x*4.16)-9.99"""
cnt_1 = 0
cnt_2 = 0
for i in range (len(X1)):
    if (Y1[i] < ((12.73*X1[i])-58.98)):
                    cnt_1 +=1
                
    if (Y2[i] > ((12.73*X2[i])-58.98)):
                    cnt_2 +=1
print(cnt_1, cnt_2)



figure, axis = plt.subplots()

plt.plot(X1, Y1, 'bo', marker = ".", label ='Chekhov')
plt.plot(X2, Y2, 'ro', marker = '.', label ='Tolstoy')
x = np.linspace(5,7)
plt.plot(x, (x*12.73)-58.98, '-r', label = 'Прямая распределния')
plt.ylim([3, 24])
plt.legend()

plt.xlabel('Средняя длинна слова в символах')
plt.ylabel('Средняя длинна предложения в словах')


plt.show()
