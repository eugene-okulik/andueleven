results = ['результат операции: 42',
           'результат операции: 514',
           'результат работы программы: 9',
           'результат: 2']


def process_results(results_list):
    total_sum = 0
    for result_str in results_list:
        colon_index = result_str.index(':')
        number_str = result_str[colon_index + 2:]
        total_sum += int(number_str) + 10
    return total_sum


final_result = process_results(results)

print(final_result)
