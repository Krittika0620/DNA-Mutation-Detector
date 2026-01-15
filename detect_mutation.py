def detect_mutation(normal_dna, mutated_dna):
    mutations = []

    min_len = min(len(normal_dna), len(mutated_dna))

    # Check for substitutions
    for i in range(min_len):
        if normal_dna[i] != mutated_dna[i]:
            mutations.append(
                f"Substitution at position {i+1}: {normal_dna[i]} → {mutated_dna[i]}"
            )

    # Check for insertion
    if len(mutated_dna) > len(normal_dna):
        extra = mutated_dna[min_len:]
        mutations.append(
            f"Insertion at position {min_len+1}: {extra}"
        )

    # Check for deletion
    elif len(normal_dna) > len(mutated_dna):
        missing = normal_dna[min_len:]
        mutations.append(
            f"Deletion at position {min_len+1}: {missing}"
        )

    return mutations


# -------- MAIN PROGRAM --------
normal = input("Enter normal DNA sequence: ").upper()
mutated = input("Enter mutated DNA sequence: ").upper()

result = detect_mutation(normal, mutated)

if result:
    print("\nMutations detected:")
    for m in result:
        print("-", m)
else:
    print("\nNo mutation detected.")
