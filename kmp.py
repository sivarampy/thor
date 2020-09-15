def lps(pat):
    ans = [0 for i in range(len(pat))]
    i = 0
    j = 1
    while j < len(pat):
        if pat[j] == pat[i]:
            ans[j] = i + 1
            j += 1
            i += 1
        else:
            if i != 0:
                i = ans[i-1]
            else:
                ans[j] = 0
                j += 1
    return ans
text = input('enter the text: ')
pattern = input('Enter the pattern: ')
#print('The lps for the pattern is: ',lps(pattern))

def kmp(text,pat,lps):
    a = len(text)
    b = len(pat)

    ans = []
    m = 0
    n = 0

    while m < a: 
        if text[m] == pat[n]:
            m += 1
            n += 1
        else:
            if n != 0:
                n = lps[n-1]
            else:
                m += 1
        if n == b:
            ans.append(m-n)
            n = lps[n-1]
            
    return ans


print(kmp(text,pattern,lps(pattern)))