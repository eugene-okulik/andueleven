op_res1, op_res2, pro_res1 = ['результат операции: 42', 'результат операции: 514', 'результат работы программы: 9']

colon_index1 = op_res1.index(':')

colon_index2 = op_res2.index(':')

colon_index3 = pro_res1.index(':')

number_str1 = op_res1[colon_index1 + 2:]

number_str2 = op_res2[colon_index2 + 2:]

number_str3 = pro_res1[colon_index3 + 2:]

result1 = int(number_str1) + 10

result2 = int(number_str2) + 10

result3 = int(number_str3) + 10

print(result1 + result2 + result3)
