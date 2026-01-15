🧬 DNA Mutation Detector (Python)
📌 Project Description

The DNA Mutation Detector is a simple Python program that compares a normal DNA sequence with a mutated DNA sequence and identifies possible mutations.

This project detects:

Substitution mutations

Insertion mutations

Deletion mutations

🎯 Objective

To develop a Python-based tool that:

Takes two DNA sequences as input

Compares them base by base

Reports mutation type and position in a human-readable format

🧪 Mutation Types Detected

| Mutation Type | Description                               |
| ------------- | ----------------------------------------- |
| Substitution  | One nucleotide is replaced by another     |
| Insertion     | Extra nucleotide(s) appear in mutated DNA |
| Deletion      | Missing nucleotide(s) from normal DNA     

🛠️ Technologies Used

Python 3

Core programming concepts:

     Functions

     Loops

     Conditional statements

     String indexing

▶️ How to Run the Program

Clone the repository:

git clone https://github.com/Krittika0620/DNA-Mutation-Detector.git


Navigate to the project directory:

cd DNA-Mutation-Detector

Run the program:

mutation_detector.py

🧾 Sample Input

Enter normal DNA sequence: ATGCCA

Enter mutated DNA sequence: ATGCAA

📤 Sample Output

Mutations detected:

- Substitution at position 5: C → A

🧠 Logic Explanation (Simple)

Compare both DNA sequences character by character

If bases differ → Substitution

If mutated DNA is longer → Insertion

If normal DNA is longer → Deletion

Positions are shown using 1-based indexing (biological standard)
