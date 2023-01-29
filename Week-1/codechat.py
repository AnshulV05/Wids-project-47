def Codechat(string):
    codewords={'meet':'cooks','love':'plays','you':'tom','i':'jerry'}
    words=string.split()
    final_string=''
    for x in words:
        if x in codewords.keys():
            final_string+=codewords[x]
        else:
            x=x[::-1]
            final_string+=x
    return final_string
