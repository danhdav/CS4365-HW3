def resolve_clauses(clause1, clause2):
    """
    Perform resolution on two clauses.
    :param clause1: A set of literals (e.g., {'~p', 'q', 'z'})
    :param clause2: A set of literals (e.g., {'~z', 'y'})
    :return: A new clause (set of literals) after resolution, or None if no resolution is possible.
    """
    for literal in clause1:
        # Check for complementary literal in clause2
        if literal.startswith('~') and literal[1:] in clause2:
            # Remove complementary literals and combine the remaining literals
            return (clause1 - {literal}) | (clause2 - {literal[1:]})
        elif not literal.startswith('~') and f'~{literal}' in clause2:
            # Remove complementary literals and combine the remaining literals
            return (clause1 - {literal}) | (clause2 - {f'~{literal}'})
    return None  # No resolution possible


def resolution_algorithm(clauses):
    """
    Perform resolution on a set of clauses and track the steps with a counter.
    :param clauses: A dictionary where keys are clause numbers and values are sets of literals.
    :return: A dictionary of resolved clauses with their step numbers.
    """
    resolved_clauses = {}
    step_counter = len(clauses) + 1  # Start counter after the initial clauses

    # Iterate over pairs of clauses for resolution
    for i, (key1, clause1) in enumerate(clauses.items()):
        for key2, clause2 in list(clauses.items())[i + 1:]:
            resolved_clause = resolve_clauses(clause1, clause2)
            if resolved_clause:
                # Add the resolved clause to the dictionary with its step number
                resolved_clauses[step_counter] = {
                    "clause": resolved_clause,
                    "parents": {key1, key2}
                }
                print(f"Step {step_counter}: Resolved {resolved_clause} from clauses {key1} and {key2}")
                step_counter += 1

    return resolved_clauses


# Example clauses from the file
clauses = {
    1: {'~p', 'q'},
    2: {'~z', 'y'},
    3: {'p', '~q'},
    4: {'~p', 'q', 'z'},
    5: {'~p', 'q', '~z'},
    6: {'z'},
    7: {'~y'},
    8: {'p'}
}

# Perform resolution and track steps
resolved_clauses = resolution_algorithm(clauses)

# Print the resolved clauses
print("\nResolved Clauses:")
for step, data in resolved_clauses.items():
    print(f"{step}. {data['clause']} {data['parents']}")