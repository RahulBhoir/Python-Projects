print('/'*15, 'Love Calculator', '/'*15)
your_name = input('What is your name? ').lower()
crush_name = input('What is your crush name? ').lower()

t_count = your_name.count('t') + crush_name.count('t')
r_count = your_name.count('r') + crush_name.count('r')
u_count = your_name.count('u') + crush_name.count('u')
e_count = your_name.count('e') + crush_name.count('e')
l_count = your_name.count('l') + crush_name.count('l')
o_count = your_name.count('o') + crush_name.count('o')
v_count = your_name.count('v') + crush_name.count('v')

true_count = t_count + e_count + u_count + r_count
love_count = l_count + o_count + v_count + e_count

love = int(str(true_count) + str(love_count))

print('\nCalculating your love score...')
if love < 10 or love > 90:
    print(f'Your score is {love}, you go together like coke and mentos.')
elif love > 40 and love < 50:
    print(f'Your score is {love}, you are alright together.')
else:
    print(f'Your score is {love}.')
