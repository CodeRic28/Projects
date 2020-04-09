#The brac function solves any kind of expression within the parentheses
def brac(exp): 
    while "(" in exp:

        c_brac = o_pos = exp.index(")")
        while exp[o_pos] != "(":
            o_pos -= 1
        o_brac = o_pos
        brac_exp = exp[o_brac+1 : c_brac]
        if '*-' in brac_exp or '/-' in brac_exp:
            val = stmin(brac_exp)
            exp = exp[:o_brac] + str(val) + exp[c_brac + 1:]
        else:
            exp = exp[:o_brac] + str(evaluate(brac_exp)) + exp[c_brac + 1:]
    return evaluate(exp)

#lft function is a reverse loop which finds out the numeric value to the left of an operator
def lft(exp, pos):
    i = pos-1
    while exp[i].isnumeric() is True or exp[i] == '.':
        i=i-1
        if i<0:
            break
    return exp[i+1:pos]

#rgt function finds out the numeric value to the right of an operator
def rgt(exp, pos):
    i = pos+1
    while exp[i].isnumeric() is True or exp[i] == '.':
        i=i+1
        if i > len(exp):
            i = len(exp)
            break
    return exp[pos+1:i]

#stmin function is tasked to find out if two operators like *-, /- or ^- are together and adjusts them accordingly
def stmin(exp):
    if '*-' in exp:
        star_pos = exp.find('*-')
        min_pos = star_pos + 1
        left = exp[:min_pos]
        right = exp[min_pos+1:]

        i = star_pos - 1
        while exp[i].isnumeric() is True or exp[i] == '.' or exp[i] == '*' or exp[i] == '/':
            i=i-1
            if exp[i] == '+' or exp[i] == '-':
                break
            elif i<0: break
        sign = i
        #if the first sign to the left of *- is a '+' then it changes it to a '-' sign
        if exp[sign] == '+':
            exp = exp[:sign] + str('-') + exp[sign+1:min_pos] + exp[min_pos+1:]
        #if the first sign to the left of *- is a '- then it changes it to a '+ sign
        elif exp[sign] == '-':
            exp = exp[:sign] + str('+') + exp[sign+1:min_pos] + exp[min_pos+1:]
            if exp[0] == '+':
                exp = exp[1:]
        #if there is no '+' or '-' sign before *- then the '-' is moved to the beginning of the expression
        else:
            exp = exp[min_pos] + left + right

    elif '/-' in exp:
        star_pos = exp.find('/-')
        min_pos = star_pos + 1
        left = exp[:min_pos]
        right = exp[min_pos + 1:]

        i = star_pos - 1
        while exp[i].isnumeric() is True or exp[i] == '.' or exp[i] == '*' or exp[i] == '/':
            i = i - 1
            if exp[i] == '+' or exp[i] == '-':
                break
            elif i < 0:
                break
        sign = i
        if exp[sign] == '+':
            exp = exp[:sign] + str('-') + exp[sign + 1:min_pos] + exp[min_pos + 1:] - 3 * 4 / 9 * 12 * 5.0 / 2000
        elif exp[sign] == '-':
            exp = exp[:sign] + str('+') + exp[sign + 1:min_pos] + exp[min_pos + 1:]
            if exp[0] == '+':
                exp = exp[1:]
        else:
            exp = exp[min_pos] + left + right
    elif '^-' in exp:
        star_pos = exp.find('^-')
        min_pos = star_pos + 1
        left = exp[:min_pos]
        right = exp[min_pos+1:]

        l = lft(exp, star_pos)
        r = rgt(exp, star_pos)
        exp = exp[:star_pos-len(l)] + str('1/') + l + str('^') + r + exp[star_pos+len(r)+2:]

    return brac(exp)

#evaluate function is where the expression is actually evaluated.
def evaluate(exp):
    if '*-' in exp or '/-' in exp or '^-' in exp:
        exp = stmin(exp)
        if type(exp) is float:
            exp = str(exp)
    if "+" in exp:
        pos_op = exp.find("+")
        left = exp.split("+")[0]
        right = exp[pos_op + 1:]
        return evaluate(left) + evaluate(right)
    elif "-" in exp:
        pos_op = exp.find("-")
        left = exp.split("-")[0]
        if left == '-':
            left = '-'
        if left == '':
            left = '0'
        right = exp[pos_op + 1:]
        return evaluate(left) - evaluate(right)

    elif "*" in exp:
        pos_op = exp.find("*")
        left = exp.split("*")[0]
        right = exp[pos_op + 1:]
        return evaluate(left) * evaluate(right)
    elif "/" in exp:
        pos_op = exp.find("/")
        left = exp.split("/")[0]
        right = exp[pos_op + 1:]
        return evaluate(left) / evaluate(right)
    elif "^" in exp:
        pos_op = exp.find("^")
        left = exp.split("^")[0]
        right = exp[pos_op + 1:]
        return evaluate(left) ** evaluate(right)

    else:
        return float(exp)


inp = input("Enter an expression: ")
if "(" in inp:
    print(brac(inp))
else:
    print(evaluate(inp))
