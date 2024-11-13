import re
from collections import Counter

def find_consonance_per_line(file_path, output_path, threshold=0.1):
    # Define Persian consonants
    consonants = "بپتثجچحخدذرزسشصضطظعغفقکگلمنوه"
    
    with open(file_path, 'r', encoding='utf-8') as f, open(output_path, 'w', encoding='utf-8') as out_file:
        for line_num, line in enumerate(f, start=1):
            # Clean the line by removing non-consonant characters
            line_cleaned = ''.join([char for char in line if char in consonants])
            
            # Count the frequency of each consonant
            consonant_counts = Counter(line_cleaned)
            total_consonants = sum(consonant_counts.values())
            
            # Normalize the counts and find the most frequent consonant(s)
            normalized_counts = {c: count/total_consonants for c, count in consonant_counts.items()}
            frequent_consonants = {c: norm for c, norm in normalized_counts.items() if norm >= threshold}
            
            # Find words containing the frequent consonants
            words = line.split()
            alliterative_words = {}
            for consonant, norm_value in frequent_consonants.items():
                words_with_consonant = [word for word in words if consonant in word]
                if words_with_consonant:
                    alliterative_words[consonant] = words_with_consonant
            
            # Write the results to the output file
            if alliterative_words:
                out_file.write(f"Line {line_num}:\n")
                for consonant, words in alliterative_words.items():
                    out_file.write(f"Consonant: '{consonant}', Normalized Value: {normalized_counts[consonant]:.2f}\n")
                    out_file.write("Words containing this consonant: " + ", ".join(words) + "\n\n")
                out_file.write("-" * 40 + "\n\n")

# Set the input and output file paths
input_file_path = 'data.txt'
output_file_path = 'consonance_output.txt'

# Run the function
find_consonance_per_line(input_file_path, output_file_path, threshold=0.13)