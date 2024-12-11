def filter_and_save(input_file, labels_to_filter, output_file):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    filtered_lines = [line for line in lines if any(f",{label}," in line for label in labels_to_filter)]
    
    with open(output_file, 'w') as outfile:
        outfile.writelines(filtered_lines)

    
    print(f"Αποθηκεύτηκαν {len(filtered_lines)} γραμμές στο αρχείο: {output_file}")

import re

# Είσοδος: Αρχείο εισόδου και labels που θέλεις να φιλτράρεις
input_file = "data_1600_gyro_watch.txt"  # Αντικατέστησέ το με το όνομα του αρχείου σου

match = re.search(r"_(\d+)_", input_file)
if match:
    prefix = match.group(1)  # Παίρνουμε τον αριθμό (π.χ. "1600")
else:
    raise ValueError("No numeric prefix found in the file name!")

labels_to_filter = ["A", "B", "E"]  # Τα labels που θέλεις να φιλτράρεις
output_file = f"{prefix}g_filtered_labels.csv"

# Εκτέλεση της συνάρτησης
filter_and_save(input_file, labels_to_filter, output_file)