single_fruit = ['apple', 'banana', 'watermelon', 'grape']
multi_fruit = []
multi_fruit.append(single_fruit[0] + 's')
multi_fruit.append(single_fruit[1] + 's')
multi_fruit.append(single_fruit[2] + 's')
multi_fruit.append(single_fruit[3] + 's')
print(multi_fruit)

for i in range(10):
    multi_fruit.append(1)


#Warm up, part two

list_of_numbers = [3, 5, 10, 23]
for num in list_of_numbers:
    print('num is' + str(num)) 