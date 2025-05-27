lines = ['Welcome to file handling, Roshini!!']
with open('data.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')

more_lines = ['there are different operations in it','let us discuss one by one','we have read,readline,readlines,write,writelines,append etc.,']
with open('data.txt', 'a+') as f:
    f.write('\n'.join(more_lines)+'\n')
    f.seek(0)
    data=f.read()
    print(data)