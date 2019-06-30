import json
import sys

def load_json(path):
    f = open(path+'.json', 'r', encoding = 'utf-8')
    j = json.load(f)
    f.close()
    return j

def dp_ternary(st, alpha = 0.1, beta = 1e-6, top = 100):
    binary_dyz = binary
    ternary_dyz = ternary
    if st == "":
        return ""
    alpha *= beta
    st = st.split(' ')
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


def run(input_dir, output_dir):
    fin = open(input_dir)
    fout = open(output_dir, 'w', encoding = 'utf-8')
    for st in fin.readlines():
        st_py = st[:-1].lower().rstrip()
        st_hz = dp_ternary(st_py)
        fout.write(st_hz + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("command: python3 pinyin.py input.txt output.txt")
    input_dir, output_dir = sys.argv[1:]
    binary = load_json('binary')
    ternary = load_json('ternary')
    dict_to_hz_nozero = load_json('dict_to_hz_nozero')
    py_count = load_json('py_count')
    word_count = load_json('word_count')
    main_py = load_json('main_py')
    print('load success!')
    run(input_dir, output_dir)
