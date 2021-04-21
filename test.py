from add2nums import add2nums

f = open("testcases.txt", mode='r', encoding='utf-8')
out = open("output.txt", mode='r+', encoding='utf-8')
cor = open("correct.txt", mode='r', encoding='utf-8')

x = f.read().split()

for i in range(0,len(x),2):
    a = int(x[i])
    b = int(x[i+1])
    out.write(str(add2nums(a,b))+'\n')

out.seek(0)
output = out.read().split()
correct = cor.read().split()

if (output == correct):
    print('Test Successful ! \n0 errors reported.')

out.close()
f.close()
