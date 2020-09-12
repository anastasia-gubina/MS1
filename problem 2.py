a = [int(i) for i in input().split()]
print(sorted(a))
xmin = min(a)
xmax = max(a)
print(xmin, xmax, 'R =', (xmax-xmin))
print(len(a))
ai = float(input())
bi = float(input())
for i in a:
    if ai < i < bi:
        print(i)
x = [float(j) for j in input().split()]
mi = [7, 2, 2, 7, 20, 9, 2, 1]
xmi = [x[j] * mi[j] for j in range(len(mi))]
print(xmi)
average = ((sum(xmi))/len(a))
print('average is', average)
m2 = [(x[j]-average)**2 * mi[j] for j in range(len(mi))]
m3 = [(x[j]-average)**3 * mi[j] for j in range(len(mi))]
m4 = [(x[j]-average)**4 * mi[j] for j in range(len(mi))]
print(m2, '\n', m3, '\n', m4)
dispersion = sum(m2)/len(a)
mu3 = sum(m3)/len(a)
mu4 = sum(m4)/len(a)
print('dispersion is', dispersion, '\n', mu3, '\n', mu4)
s = dispersion ** 0.5
print('Asymmetry is', mu3/s**3)
print('Kurtosis is', mu4/s**4 - 3)

