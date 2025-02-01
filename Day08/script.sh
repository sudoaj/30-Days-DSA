#!/bin/bash
# Script to generate notebook files for each concept with the naming pattern:
# 005_specificconcept_majorconcept.ipynb

# Function to sanitize concept names:
# - Converts text to lowercase.
# - Removes commas, parentheses, and hyphens.
# - Replaces spaces with underscores.
sanitize() {
  echo "$1" | tr '[:upper:]' '[:lower:]' | sed 's/[(),-]//g' | tr -s ' ' '_'
}

counter=1

# --- Sorting Algorithms ---
sorting_major="sorting_algorithms"
sorting_concepts=(
  "Bubble Sort"
  "Selection Sort"
  "Insertion Sort"
  "Merge Sort"
  "Quick Sort"
  "Heap Sort"
  "Counting Sort"
  "Radix Sort"
  "Bucket Sort"
  "Tim Sort"
  "Intro Sort"
)

for concept in "${sorting_concepts[@]}"; do
  sanitized_concept=$(sanitize "$concept")
  padded=$(printf "%03d" "$counter")
  filename="${padded}_${sanitized_concept}_${sorting_major}.ipynb"
  touch "$filename"
  echo "Created file: $filename"
  ((counter++))
done

# --- Searching Algorithms ---
searching_major="searching_algorithms"
searching_concepts=(
  "Linear Search"
  "Binary Search"
  "Interpolation Search"
  "Exponential Search"
  "Fibonacci Search"
  "Depth-First Search (DFS)"
  "Breadth-First Search (BFS)"
)

for concept in "${searching_concepts[@]}"; do
  sanitized_concept=$(sanitize "$concept")
  padded=$(printf "%03d" "$counter")
  filename="${padded}_${sanitized_concept}_${searching_major}.ipynb"
  touch "$filename"
  echo "Created file: $filename"
  ((counter++))
done

# --- Recursion Basics ---
recursion_major="recursion_basics"
recursion_concepts=(
  "Understanding Recursion"
  "Recursion Trees and Visualization"
  "Factorial Calculation"
  "Fibonacci Sequence Computation"
  "Tower of Hanoi"         # Will become tower_of_hanoi
  "Recursive Sorting"
  "Recurrence Relations"
  "Solving Recurrences"
)

for concept in "${recursion_concepts[@]}"; do
  sanitized_concept=$(sanitize "$concept")
  padded=$(printf "%03d" "$counter")
  filename="${padded}_${sanitized_concept}_${recursion_major}.ipynb"
  touch "$filename"
  echo "Created file: $filename"
  ((counter++))
done

# --- Additional Related Concepts ---

## Complexity Analysis
complexity_major="complexity_analysis"
complexity_concepts=(
  "Big O, Big Theta, and Big Omega Notation"
  "Time Complexity"
  "Space Complexity"
  "Best-case, Worst-case, and Average-case Analysis"
)

for concept in "${complexity_concepts[@]}"; do
  sanitized_concept=$(sanitize "$concept")
  padded=$(printf "%03d" "$counter")
  filename="${padded}_${sanitized_concept}_${complexity_major}.ipynb"
  touch "$filename"
  echo "Created file: $filename"
  ((counter++))
done

## Algorithm Design Paradigms
design_major="algorithm_design_paradigms"
design_concepts=(
  "Divide and Conquer"
  "Dynamic Programming"
  "Greedy Algorithms"
  "Backtracking"
  "Branch and Bound"
)

for concept in "${design_concepts[@]}"; do
  sanitized_concept=$(sanitize "$concept")
  padded=$(printf "%03d" "$counter")
  filename="${padded}_${sanitized_concept}_${design_major}.ipynb"
  touch "$filename"
  echo "Created file: $filename"
  ((counter++))
done

## Data Structures Impacting Algorithms
datastruct_major="data_structures"
datastruct_concepts=(
  "Arrays and Linked Lists"
  "Stacks and Queues"
  "Trees and Graphs"
  "Hash Tables"
)

for concept in "${datastruct_concepts[@]}"; do
  sanitized_concept=$(sanitize "$concept")
  padded=$(printf "%03d" "$counter")
  filename="${padded}_${sanitized_concept}_${datastruct_major}.ipynb"
  touch "$filename"
  echo "Created file: $filename"
  ((counter++))
done

echo "Notebook file generation complete!"