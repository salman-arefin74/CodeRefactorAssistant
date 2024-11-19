import csv
import os
import pandas

def generate_refactoring_suggestion(code_smell, method_name):
    suggestions = {
        "Long Method": f"Refactor '{method_name}' by splitting it into smaller functions.",
        "High Cyclomatic Complexity": f"Reduce complexity in '{method_name}' by simplifying logic or extracting helper methods."
    }
    return suggestions.get(code_smell, "No suggestion available.")

current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "..")
file_name = "code_smells.csv"
file_path = os.path.join(data_dir, file_name)

dataset = pandas.read_csv(file_path)
dataset = dataset.drop(['file_name', 'line_count', 'complexity', 'code_smell_detected'], axis=1)
detected_smells = dataset.to_dict(orient='records')

refactoring_suggestions = []

for smell in detected_smells:
    if smell["code_smell"] != "No Smell detected":
        suggestion = generate_refactoring_suggestion(smell["code_smell"], smell["method_name"])
        refactoring_suggestions.append([smell["method_name"], smell["code_smell"], suggestion])

csv_file = "refactoring_suggestions.csv"

with open(csv_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Method Name", "Code Smell", "Refactoring Suggestion"])  # Write header

    for suggestion in refactoring_suggestions:
        writer.writerow(suggestion)

print(f"Refactoring suggestions have been written to '{csv_file}'.")