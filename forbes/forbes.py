"""
Functions to help out parsing Forbes information
"""

def parse_top(filename_in="./forbes/top.txt", filename_out="./forbes/lines.csv"):
    """
    Parses copy pasted info into a csv file capable of being handled by pandas
    """
    f = open(filename_in, "r")
    i=0
    a = []
    
    for x in f:
        if ((i%8 != 0) & (i != 0)):
            a.append(x.replace('\n', '|'))
        elif (i%8 == 0):
            a.append('\n')
            a.append(x.replace('\n', '|'))
        i = i + 1
        
    a[0] = ''

    q = ''.join(a)

    w = open(filename_out, "w")
    w.write(q)
    w.close()   