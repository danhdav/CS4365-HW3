import sys

def negate(line):
    # if ~ in line, replace with ''
    # else if ~ not in line, replace with ~ before each element in line separated by space
    if '~' in line:
        return ' '.join(['~' + part if '~' not in part else part.replace('~', '') for part in line.split()])
    else:
        return ' '.join(['~' + part for part in line.split()])
    
def resolve(line1, line2):
    # Split the lines into lists of literals
    line1 = line1.split()
    line2 = line2.split()

    # Find the resolvent by removing the complementary literals
    resolvent = [lit for lit in line1 if f"~{lit}" not in line2 and lit not in line2] + \
                [lit for lit in line2 if f"~{lit}" not in line1 and lit not in line1]
    
    # Return the resolvent as a string
    return ' '.join(resolvent)

# Read in a text file taken as argument
with open(sys.argv[1], 'r') as file:
    lines = [line.rstrip('\n') for line in file.readlines()]
    toProve = negate(lines[-1])  # Negate the last line
    
    toProveList = []  # Initialize an empty list for toProve
    # if toProve is more than 1 element, split elements into a list
    if len(toProve.split()) > 1:
        toProve = toProve.split()
        # add each element to a list
        toProveList = [toProve[i] for i in range(len(toProve))]

    lines = lines[:-1]  # Remove the last line from the list
    clauseList = lines + toProveList  # Combine the lines and the negated last line

    # get the max length of how many elements in the line
    maxLength = max(len(line.split()) for line in clauseList)
    print(maxLength)

# Open an output file to write the modified lines
with open('output.txt', 'w') as output_file:
    for line in clauseList:
        # Add {} to the end of each line, and append line number at the start
        modified_line = str(clauseList.index(line) + 1) + '. ' + line + ' { }'
        output_file.write(modified_line + '\n')