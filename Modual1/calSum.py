def cal(operation,number_1,number_2):
    
    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == 'x':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('You have not typed a valid operator, please run the program again.')


with open("test.txt",'r') as f:
    filelines = f.read().splitlines()
    for line in filelines: 
        lineparts = line.split()
        operation = lineparts[1]
        number_1 = int(lineparts[2])
        number_2 = int(lineparts[3])
        
        answer=cal(operation,number_1,number_2)

print(f'Total sum = {total}')