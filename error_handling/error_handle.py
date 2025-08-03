file = open('youtube.txt','w')

try:
    file.write('chai aur code')
finally:
    file.close()

with open('youtue.txt','w') as file:
    file.write('chai aur code')