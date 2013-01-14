def sql_str(x):
    return "'" + str(x) + "'"

def sql_and(x,  y):
    if x == '':
        return y
    elif y == '':
        return x
    else:
        return x + " AND " + y
