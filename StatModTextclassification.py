

file_path = 'text_Tolstoy.txt'

with open(file_path, 'r', encoding='utf-8') as author_file:
    data = author_file.read()



BLOCK_COUNT = 100

result_data = ''
block_size = 12500
for i in range(BLOCK_COUNT):
    begin = i * block_size
    end = (i+1) * block_size

    amount_of_speach_const = 0
    sentences = 0
    word_count = 0
    other_chars = 0
    med_len_of_sentences = 0

    for j, char in enumerate(data[begin: end]):
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

    try:
        med_len_of_word = round(other_chars/word_count, 2)
        med_len_of_sentences = round(word_count/sentences, 3)
        
        result_data += f'{med_len_of_word} {med_len_of_sentences}\n'
    except ZeroDivisionError:
        break
        
with open(f'res_{file_path}', 'a') as output_file:
    output_file.write(result_data)
