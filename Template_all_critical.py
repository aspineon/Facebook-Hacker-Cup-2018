# Written by Gerrit Schoettler, 2018

f = open("all_critical_sample_input.txt", 'r')
output = open("all_critical_sample_outputTEST.txt", 'w')
input = f.readline
ans = 1
for cnum in range(1, int(input()) + 1):
    p = input().strip().split()
    p = list(map(float, p))
    print(p)

    print("Case #%d: %d" % (cnum, ans), file=output)

f.close()
output.close()
print('Input file closed:', f.closed)
print('Output file closed:', output.closed)
