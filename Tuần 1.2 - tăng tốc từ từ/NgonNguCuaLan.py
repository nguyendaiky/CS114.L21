def function(s):
    if len(s) == 1 and ('lios' in s[0] or 'etra' in s[0] or 'inites' in s[0] or 'liala' in s[0] or 'etr' in s[0] or 'initis' in s[0]):
        return 'YES'
    Am = []
    Vm = []
    Nm = []
    Aw = []
    Vw = []
    Nw = []
    i = 0
    for si in s:
        if 'etra' in si:
            Nw.append([i,si])
        elif 'inites' in si:
            Vw.append([i,si])
        elif 'liala' in si:
            Aw.append([i,si])
        elif 'etr' in si:
            Nm.append([i,si])
        elif 'initis' in si:
            Vm.append([i,si])
        elif 'lios' in si:
            Am.append([i,si])
        else:
            return 'NO'
        i += 1
    if len(Nm) == 1 and len(Vm) >= 0 and len(Am) >= 0 and len(Nw) == 0 and len(Vw) == 0 and len(Aw) == 0:
        gt = 1
    elif len(Nm) == 0 and len(Vm) == 0 and len(Am) == 0 and len(Nw) == 1 and len(Vw) >= 0 and len(Aw) >= 0:
        gt = 0
    else:
        return 'NO'
    if gt == 1:
        for i in range(len(Am)):
            if Am[i][0] > Nm[0][0]:
                return 'NO'
        for i in range(len(Vm)):
            if Vm[i][0] < Nm[0][0]:
                return 'NO'
        return 'YES'
    elif gt == 0:
        for i in range(len(Aw)):
            if Aw[i][0] > Nw[0][0]:
                return 'NO'
        for i in range(len(Vm)):
            if Vw[i][0] < Nw[0][0]:
                return 'NO'
        return 'YES'
s = list(input().split())
print(function(s))
