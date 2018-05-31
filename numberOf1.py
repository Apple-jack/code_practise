n = 5

def NumberOf1(n):
    bi = []
    n_abs = abs(n)
    continue_0_num = 0
    continue_end = False
    other_0_num = 0
    while n_abs > 1:
        bi.append(n_abs % 2)
        n_abs = int(n_abs / 2)
    bi.append(n_abs)
    while len(bi) < 32:
        bi.append(0)
    print(bi)
    if n < 0:
        for i in range(len(bi)):
            if bi[i] == 0 and not continue_end:
                continue_0_num += 1
            elif bi[i] == 0 and continue_end:
                other_0_num += 1
            else:
                continue_end = True
        return other_0_num + 1
    else:
        return sum(bi)


print(NumberOf1(-5))