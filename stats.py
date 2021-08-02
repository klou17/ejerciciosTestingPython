def stats(lst):
    min = None
    max = None
    freq = {}
    for i in lst:
        if min is None or i < min:
            min = i
        if max is None or i > max:
            max = i
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    lst_sorted = sorted(lst)
    if len(lst_sorted)%2 == 0:
        middle = len(lst_sorted)/2
        median = (lst_sorted[middle] + lst_sorted[middle-1]) / 2
    else:
        median = lst_sorted[len(lst_sorted)/2]
    mode_times = None
    for i in freq.values():
        if mode_times is None or i > mode_times:
            mode_times = i
    mode = []
    for (num, count) in freq.items():
        if count == mode_times:
            mode.append (num)
    print ("list = " + str(lst))
    print ("min = " + str(min))
    print ("max = " + str(max))
    print ("median = " + str(median))
    print ("mode(s) = " + str(mode))

def test1():
    l = [31, 30, 1, 2, 20]
    stats(l)
    l = [31, 23, 1, 2]
    stats(l)

def test2():
    l = [-31, -2]
    stats(l)

test1()
test2()
