def bubble_sort(N):
    n = 1
    while n < len(sorted_list):
        for i in range(len(sorted_list)-n):
            if sorted_list[i] > sorted_list[i+1]:
                sorted_list[i],sorted_list[i+1] = sorted_list[i+1],sorted_list[i]
        n += 1

def python_sort(N):
    sorted_list.sort()

if __name__ == '__main__':
    import datetime
    import random
    N = [100, 1000,3000,10000,20000,30000]
    f = open('results.xls', 'w+')
    a = []
    b = []
    for n in N:
        for i in range(5):
            sorted_list = range(n)
            random.shuffle(sorted_list)
            start = datetime.datetime.now()
            bubble_sort(n)
            finish = datetime.datetime.now()
            c = str(finish-start)
            c = c.split(':')
            if c[2][0] == '0':
                a.append(float(c[2][1:]))
            else:
                a.append(float(c[2]))
            sorted_list = range(n)
            random.shuffle(sorted_list)
            start2 = datetime.datetime.now()
            python_sort(n)
            finish2 = datetime.datetime.now()
            d = str(finish2-start2)
            d = d.split(':')
            if d[2][0] == '0':
                b.append(float(d[2][1:]))
            else:
                b.append(float(d[2]))
    a.sort()
    b.sort()
    sorted_a = a[1:4]+a[6:9]+a[11:14]+a[16:19]+a[21:24]+a[26:29]
    sorted_b = b[1:4]+b[6:9]+b[11:14]+b[16:19]+b[21:24]+b[26:29]
    f.writelines("%s\n" % n for n in N)
    f.writelines("%s\n" % j for j in sorted_a)
    f.writelines("%s\n" % k for k in sorted_b)
    f.close()