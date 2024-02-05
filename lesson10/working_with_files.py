file1 = open('a.txt', 'r')
lines_to_read = file1.readlines()
print(lines_to_read)
file1.close() #zavjdy zakrivate, bo bude visity vidkritym i ne bude dostupu

file2 = open('a.txt', 'w')
file2.write('hello i m first entity here\n')
file2.writelines(['first line\n', 'second line\n'])
file2.close()

file3 = open('a.txt', 'a')
file3.write('this is a new line, new hope\n')
file3.close()

permanent_lines = []
with open('a.txt', 'r') as a:
    temp_lines = a.readlines()
    permanent_lines.append(temp_lines)
    print(permanent_lines)

with open('b.txt', 'w') as b:
    for line in permanent_lines:
        if len(line) > 20:
            permanent_lines[permanent_lines.index(line)] = 'sorry this line was too long\n'
    b.writelines(str(permanent_lines))


