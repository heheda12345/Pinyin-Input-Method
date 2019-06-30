import json
import sys
from copy import deepcopy


binary = ternary = dict_to_hz_nozero = py_count = word_count = main_py = None


def load_json(path):
    f = open(path+'.json', 'r', encoding = 'utf-8')
    j = json.load(f)
    f.close()
    return j


def dp_ternary(st, alpha = 0.1, beta = 1e-6, top = 100):
    binary_dyz = binary
    ternary_dyz = ternary
    if st == []:
        return ""
    alpha *= beta
    if (len(st) == 1):
        ans = -1
        ret = ""
        for x in dict_to_hz_nozero[st[0]]:
            if word_count[x] > ans:
                ans = word_count[x]
                ret = x
        return ret
    f = [{} for x in st]
    g = [{} for x in st]
    l = len(st)
    # forward
    py0 = st[0]
    py1 = st[1]
    # first two words: uses the best binary model
    for zi0 in dict_to_hz_nozero[st[0]]:
        for zi1 in dict_to_hz_nozero[st[1]]:
            f[1][zi0+zi1] = -1
            g[1][zi0+zi1] = ""
            prob= 0
            if main_py[zi1] == py1:
                prob += alpha * word_count[zi1] / py_count[py1]
            py_binary = binary_dyz[py0 + ' ' + py1] if py0 + ' ' + py1 in binary_dyz else None 
            if py_binary and zi0 + zi1 in py_binary:
                prob += beta * py_binary[zi0 + zi1] # / zi_nextPy_count[zi0][py1]
            if prob > f[1][zi0+zi1]:
                f[1][zi0+zi1] = prob
                g[1][zi0+zi1] = zi0
    # dp
    for i in range(2, l):
        py0 = st[i-2]
        py1 = st[i-1]
        py2 = st[i]
        py_binary = binary_dyz[py1 + ' ' + py2] if py1 + ' ' + py2 in binary_dyz else None 
        py_binary_pre = binary_dyz[py0 + ' ' + py1] if py0 + ' ' + py1 in binary_dyz else None
        py_ternary = ternary_dyz[py0 + ' ' + py1 + ' ' + py2] if py0 + ' ' + py1 + ' ' + py2 in ternary_dyz else None
        sorted_prob = [(zi, f[i-1][zi]) for zi in f[i-1]]
        sorted_prob = sorted(sorted_prob, key=lambda x: x[1], reverse = True) # sorted() sorts from small to large
        for zizi in sorted_prob[:min(len(sorted_prob), top)]:
            zi0 = zizi[0][0]
            zi1 = zizi[0][1]
            pre = zi0+zi1
            for zi2 in dict_to_hz_nozero[st[i]]:
                cur = zi1+zi2
                if cur not in f[i]:
                    f[i][cur] = -1
                    g[i][cur] = ""
                prob = 0
                if main_py[zi2] == py2:
                    prob += alpha * word_count[zi2] / py_count[py2]
                if py_binary and zi1 + zi2 in py_binary:
                    prob += beta * py_binary[zi1 + zi2]
                if py_ternary and zi0 + zi1 + zi2 in py_ternary :
                    prob += py_ternary[zi0 + zi1 + zi2]**1.5
                if prob*f[i-1][pre] > f[i][cur]:
                    f[i][cur] = prob * f[i-1][pre]
                    g[i][cur] = pre

    # backward
    mx = -1
    zi_cur = ""
    for zi in f[l-1]:
        if f[l-1][zi] > mx:
            mx = f[l-1][zi]
            zi_cur = zi
    ret = zi_cur[1]
    for i in range(l-1, 1, -1):
        zi_cur = g[i][zi_cur]
        ret = zi_cur[1] + ret
    ret = zi_cur[0] + ret
    return ret


def solve(st):
    inp = []
    for s in st.split(" "):
        if s != "":
            inp.append(s)
    
    l = len(inp)
    if l == 0:
        return []
    for x in inp:
        if x not in dict_to_hz_nozero:
            return []
    
    ret = []
    if len(inp) > 3:
        ret.append(dp_ternary(inp))
    elif len(inp) == 3:
        py3 = " ".join(inp)
        if py3 not in ternary:
            ret.append(dp_ternary(inp))
        else:
            lst = [(ci, ternary[py3][ci]) for ci in ternary[py3]]
            lst = sorted(lst, key=lambda x: x[1], reverse = True)
            for i in range(0, min(len(lst), 3)):
                ret.append(lst[i][0])
    elif len(inp) == 2:
        py2 = " ".join(inp)
        if py2 not in ternary:
            ret.append(dp_ternary(inp))
        else:
            lst = [(ci, binary[py2][ci]) for ci in binary[py2]]
            lst = sorted(lst, key=lambda x: x[1], reverse = True)
            for i in range(0, min(len(lst), 5)):
                ret.append(lst[i][0])
    elif len(inp) == 1:
        py1 = inp[0]
        for x in dict_to_hz_nozero[py1]:
            ret.append(x)
    return ret


def init():
    global binary, ternary, dict_to_hz_nozero, py_count, word_count, main_py
    binary = load_json('pyData/binary')
    ternary = load_json('pyData/ternary')
    dict_to_hz_nozero = load_json('pyData/dict_to_hz_nozero')
    py_count = load_json('pyData/py_count')
    word_count = load_json('pyData/word_count')
    main_py = load_json('pyData/main_py')
