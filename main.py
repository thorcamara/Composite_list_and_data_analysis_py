temporary = []
main = []
biggest = lowest = 0
while True:
    temporary.append(str(input('Name: ')))
    temporary.append(float(input('Weight: ')))
    if len(main) == 0:
        biggest = lowest = temporary[1]
    else:
        if temporary[1] > biggest:
            biggest = temporary[1]
        if temporary[1] < lowest:
            lowest = temporary[1]
    main.append(temporary[:])
    temporary.clear()
    answer = str(input('Do you want to continue? [\033[4;32mY\033[m/\033[4;31mN\033[m] '))
    if answer in 'Nn':
        break
print('-=' * 30)
print(f'In all, you registered \033[4;33m{len(main)}\033[m people.')
print(f'The biggest weight was of \033[4;32m{biggest}\033[mKg. Weight of ', end='')
for w in main:
    if w[1] == biggest:
        print(f'[\033[4;34m{w[0]}\033[m] ', end='')
print()
print(f'The lowest weight was of \033[4;31m{lowest}\033[mKg. Weight of ', end='')
for w in main:
    if w[1] == lowest:
        print(f'[\033[4;35m{w[0]}\033[m] ', end='')
print()
