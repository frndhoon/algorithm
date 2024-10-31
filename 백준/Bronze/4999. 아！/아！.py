jh = input()
doctor = input()

result = jh.replace(doctor, '')
print('no' if 'h' in result else 'go')
