import sys

'''
Daniel Hori Davila
Patrick D'Souza
CS4365.004
Professor Vlad Birsan
'''

def negate(line):
    # if ~ in line, replace with ''
    if '~' in line:
        return ' '.join(['~' + part if '~' not in part else part.replace('~', '') for part in line.split()])
    # else if ~ not in line, replace with ~ before each element in line separated by space
    else:
        return ' '.join(['~' + part for part in line.split()])


def delete_complements(l1, l2):
    if l1 == ('~' + l2) or l2 == ('~' + l1):
        return True
    else:
        return False


def resolve_clauses(clause1, clause2, all_clauses):

    # Split clauses into lists of literals
    literals1 = clause1.split()
    literals2 = clause2.split()

    # Combine literals from both clauses
    combined_literals = set(literals1 + literals2)
    resolved_literals = list(combined_literals)
    original_literals = list(combined_literals)

    # Iterate through literals to find and remove complementary pairs
    for literal1 in literals1:
        for literal2 in literals2:
            if delete_complements(literal1, literal2):
                resolved_literals.remove(literal1)
                resolved_literals.remove(literal2)
                # If all literals are removed, return False (contradiction)
                if len(resolved_literals) == 0:
                    return False
                else:
                    # Check for tautology
                    if any(delete_complements(lit1, lit2) for lit1 in resolved_literals for lit2 in resolved_literals):
                        return True

                    # Check if the resolved clause already exists
                    for existing_clause in all_clauses:
                        existing_literals = existing_clause.split()
                        difference = [
                            lit for lit in resolved_literals + existing_literals
                            if lit not in resolved_literals or lit not in existing_literals
                        ]
                        if not difference:
                            return True

                    return resolved_literals

    # Return true if no changes were made
    if resolved_literals == original_literals:
        return True


def find_two_clauses(clauses):
    # Print the original clauses and the negated last line
    for clause in clauses:
        formatted_clause = f"{clauses.index(clause) + 1}. {clause} {{ }}"
        print(formatted_clause)

    # Store the total number of clauses
    total_clauses = len(clauses) + 1

    # Take the clauses from current_clause_index and comparison_clause_index and attempt to resolve them
    current_clause_index = 1
    while current_clause_index < total_clauses - 1:
        comparison_clause_index = 0
        while comparison_clause_index < current_clause_index:
            resolved_clause = resolve_clauses(clauses[current_clause_index], clauses[comparison_clause_index], clauses)
            
            if resolved_clause is False:
                print(f"{total_clauses}. Contradiction {{ {current_clause_index + 1}, {comparison_clause_index + 1} }}")
                total_clauses += 1
                print("Valid")
                sys.exit(0)
            elif resolved_clause is True:
                comparison_clause_index += 1
                continue
            else:
                print(f"{total_clauses}. {' '.join(resolved_clause)} {{ {current_clause_index + 1}, {comparison_clause_index + 1} }}")
                total_clauses += 1
                clauses.append(' '.join(resolved_clause))
            comparison_clause_index += 1
        current_clause_index += 1


# Read in text file
with open(sys.argv[1], 'r') as file:
    lines = [line.rstrip('\n') for line in file.readlines()]

toProve = negate(lines[-1])  # Negate the last line

toProveList = []  # Initialize an empty list for toProve
# if toProve is more than 1 element, split elements into a list
if len(toProve.split()) > 1:
    toProve = toProve.split()
    # add each element to a list
    toProveList = [toProve[i] for i in range(len(toProve))]
else:
    toProveList.append(toProve)

# print("toProve", toProve)
lines = lines[:-1]  # Remove the last line from the list
clauseList = lines + toProveList  # Combine the lines and the negated last line
solution = find_two_clauses(clauseList)