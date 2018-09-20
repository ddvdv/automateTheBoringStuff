#! python3

# Mad libs, a classic..

print('####### WELCOME IN MAD LIB FEVER ########')
adjective = input('Enter an adjective: ')
noun1 = input('Enter a noun: ')
verb = input('Enter a verb: ')
noun2 = input('Enter a noun: ')

result = f"The {adjective} panda walked to the {noun1} and then {verb}. A nearby {noun2} was unaffected by these events."

print(result)

file = open('madLibResult.txt', 'a')
file.write(result + '\n')
file.close()
