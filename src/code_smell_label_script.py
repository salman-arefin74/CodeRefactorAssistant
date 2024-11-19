import os
import ast
import csv
from radon.complexity import cc_visit
from config import get_complex_code_thresholds

LONG_METHOD_THRESHOLD = get_complex_code_thresholds("long_method")
LINE_THRESHOLD = LONG_METHOD_THRESHOLD["line_count"]
COMPLEXITY_THRESHOLD = LONG_METHOD_THRESHOLD["cyclomatic_complexity"]

def analyze_method(method_node, filename):
    """Analyzes a function/method for line count and cyclomatic complexity."""

    line_count = method_node.end_lineno - method_node.lineno + 1
    cyclomatic_complexity = sum([block.complexity for block in cc_visit(ast.unparse(method_node))])
    code_smell_detected = line_count > LINE_THRESHOLD or cyclomatic_complexity > COMPLEXITY_THRESHOLD
    code_smell = "No Smell detected"
    if code_smell_detected:
        if line_count > LINE_THRESHOLD:
            code_smell = "Long Method"
        else:
            code_smell = "High Cyclomatic Complexity"

    return {
        "file_name": filename,
        "method_name": method_node.name,
        "line_count": line_count,
        "complexity": cyclomatic_complexity,
        "code_smell_detected": code_smell_detected,
        "code_smell": code_smell
    }

def analyze_file(filepath, filename):
    """Analyzes each function in the file for code smells and returns results."""
    
    with open(filepath, "r") as file:
        tree = ast.parse(file.read())

    results = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            analysis = analyze_method(node, filename)
            results.append(analysis)
    
    return results

def save_results_to_csv(results, output_file="code_smells.csv"):
    """Saves the analyzed results to a CSV file."""
    
    with open(output_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["file_name", "method_name", "line_count", "complexity", "code_smell_detected", "code_smell"])

        for result in results:
            writer.writerow([
                result["file_name"],
                result["method_name"],
                result["line_count"],
                result["complexity"],
                result["code_smell_detected"],
                result["code_smell"],
            ])
    print(f"Results saved to {output_file}")

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "..", "data")

    all_results = []

    for filename in os.listdir(data_dir):
        if filename.endswith(".py"):
            file_path = os.path.join(data_dir, filename)
            results = analyze_file(file_path, filename)

            for result in results:
                result["file_name"] = filename
            all_results.extend(results)

    save_results_to_csv(all_results)

if __name__ == "__main__":
    main()