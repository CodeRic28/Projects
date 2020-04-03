
def brac(exp):
    if "(" in exp:
        par_pos1 = exp.find('(')
        par_pos2 = exp.find(')', par_pos1)
        par_exp = exp[par_pos1 + 1:par_pos2]
        exp = exp[:par_pos1] + str(evaluate(par_exp)) + exp[par_pos2 + 1:]
        return evaluate(exp)

def evaluate(exp):
    if "+" in exp:
        pos_op = exp.find("+")
        left = exp.split("+")[0]
        right = exp[pos_op + 1:]
        return evaluate(left) + evaluate(right)
    elif "-" in exp:
        pos_op = exp.find("-")
        left = exp.split("-")[0]
        if left == '':
            left = '0'
        right = exp[pos_op + 1:]
        return evaluate(left) - evaluate(right)
    elif "/" in exp:
        pos_op = exp.find("/")
        left = exp.split("/")[0]
        right = exp[pos_op + 1:]
        return evaluate(left) / evaluate(right)
    elif "*" in exp:
        pos_op = exp.find("*")
        left = exp.split("*")[0]
        right = exp[pos_op + 1:]
        return evaluate(left) * evaluate(right)
    elif "^" in exp:
        pos_op = exp.find("^")
        left = exp.split("^")[0]
        right = exp[pos_op + 1:]
        return evaluate(left) ** evaluate(right)
    else:
        # Base Case
        #print("Execution completed")
        return int(exp)


inp = input("Enter an expression: ")
if "(" in inp:
    print(brac(inp))
else:
    print(evaluate(inp))
