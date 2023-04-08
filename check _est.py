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



def line_coeff(X1: list, Y1: list, X2: list, Y2: list):
    best_k = 0
    best_b = 0
    min_cnt = 0
    cnt_1 = 0
    cnt_2 = 0
    cnt = 0
 
    
    range_of_coeff = [x / 100 for x in range(-5000, 5000+1)]
    for k in range_of_coeff:
        for b in range_of_coeff:
            for i in range(len(X1)):
                 
                if (Y1[i] < ((k*X1[i])+b)):
                    cnt_1 +=1
                
                if (Y2[i] > ((k*X2[i])+b)):
                    cnt_2 +=1
                cnt = abs(cnt_1-cnt_2)
                if (cnt <= min_cnt ):
                    min_cnt= min(min_cnt, cnt)
                    best_b = b
                    best_k = k
           
                
            cnt_1 = 0
            cnt_2 = 0
            cnt = 0


    return best_k, best_b
k, b = line_coeff(X1, Y1, X2, Y2)
print('end')
print(k,b)
