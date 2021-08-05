import sys

OPR = {
    '+', '-', '/', '*', '^'
}

NUM = {
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9','.'
}

LET = {
    'A', 'B', 'C', 'D', 'E', 'F'
}

BRC = {
    '(', ')'
}

def missing_operator(e):
    #empty vector
    if len(e) == 0:
        return True

    # operator without num/variables
    if e[0] in OPR or len(e) == 1:
        return True

    # Value Vector
    vvec = []
    # Operator Vector
    ovec = []

    # start and end
    i , j = (0, 0)
   
    while j < len(e):
        # Opening Bracket
        if e[j] == '(':
            # Opening Position
            j += 1
            i += j
            nbrackets = 0
            for k in range(j-1, len(e)):
                # Open one bracket
                if e[k] == '(':           
                    nbrackets += 1
                elif e[k] == ')':                 # Close bracket
                    if nbrackets == 0:
                        break                     # All brackets closed
                    nbrackets -= 1                # Close one bracket
            print(f"Remaining brackets: {nbrackets}")
            if nbrackets != 0:                    # Missing Closing Bracket
                return True
            else:
                print("Open and close brackets match")

        if e[j] in OPR:                           # Add Operator
            ovec.append(e[j])

        if e[j] in NUM:                           # Add Value
            i = j                                 # Start at position j
            while j < len(e) and e[j] not in OPR and e[j] not in BRC and e[j] not in LET:
                j += 1

            newvec = e[i:j]                         # Construct Value, Move Back
            vvec.append(newvec)
            j -= 1
        elif e[j] in LET:
            newvec = e[j]                         # Construct Value, Move Back
            vvec.append(newvec)
        j += 1

    # check for values with more than one decimal
    for val in vvec:
        count = 0
        for v in val:
            if "." == v:
                count += 1
        if count > 1:
            return True                            # Found Value with too many decimals (invalid)

    # Compare number of inputs to supplied operators found
    if len(vvec) != len(ovec) + 1:
        # print("Missing operator")
        return True
    return False

if __name__ == "__main__":

    if len(sys.argv) >= 2:
        expression = sys.argv[1]
        print(missing_operator(expression))
    else:
        print("Missing expression as input")
