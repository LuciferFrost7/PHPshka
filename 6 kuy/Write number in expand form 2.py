def expanded_form(num: float):
    num1, num2 = str(num).split('.')
    l = []; ll = []
    ppp = [k for k in [str(l[j] * 10**(len(l)-1-j)) for j in range(len([l.append(int(i)) for i in str(num1)]))] if k!= '0']
    ppp.extend([k for k in [str(ll[j]) + f'/' + str(10 ** (j+1)) for j in range(len([ll.append(int(i)) for i in str(num2)]))] if k[:2] != '0/'])
    return ' + '.join(ppp)