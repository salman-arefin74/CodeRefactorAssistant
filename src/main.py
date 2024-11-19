import os
import pandas as pd
from code_smell_label_script import analyze_file
from code_smell_label_script import detect_smell_type
from code_refactor_suggestions_generator import generate_refactoring_suggestion
from joblib import load
import argparse

def classify_function(model, line_count, complexity):
    input_data = pd.DataFrame([[line_count, complexity]], columns=['line_count', 'complexity'])
    prediction = model.predict(input_data)
    return bool(prediction[0])


def process_codes(file_path, model, output_path):
    results = []
    
    for root, _, files in os.walk(file_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                functions = analyze_file(file_path, file)
                
                for func in functions:
                    
                    is_smelly = classify_function(model, func['line_count'], func['complexity'])
                    func['is_smelly'] = is_smelly
                    
                    if is_smelly:
                        func['smell_type'] = detect_smell_type(func['line_count'])
                        func['refactoring_suggestion'] = generate_refactoring_suggestion(func['smell_type'], func['method_name'])
                        results.append(func)
    
    df = pd.DataFrame(results)
    df.to_csv(output_path, index=False)
    print(f"Analysis complete. Results saved to {output_path}")

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "..", "data")

    parser = argparse.ArgumentParser(description="Process codes with a specified model.")
    parser.add_argument(
        "model_name",
        type=str,
        help="Name of the model file [extension: .pkl]",
    )
    args = parser.parse_args()
    
    model = load(args.model_name)
    process_codes(data_dir, model, "results.csv")