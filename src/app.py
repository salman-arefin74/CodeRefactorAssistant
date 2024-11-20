from flask import Flask, render_template, request, jsonify
import pandas as pd
from joblib import load
import ast
from radon.complexity import cc_visit
from config import get_complex_code_thresholds
import os

LONG_METHOD_THRESHOLD = get_complex_code_thresholds("long_method")
LINE_THRESHOLD = LONG_METHOD_THRESHOLD["line_count"]
COMPLEXITY_THRESHOLD = LONG_METHOD_THRESHOLD["cyclomatic_complexity"]

CLASSIFIERS = {
    "RandomForest": "random_forest_classifier.pkl",
    "KNN": "knn_classifier.pkl",
    "SupportVectorMachine": "support_vector_machine_classifier.pkl",
    "NaiveBayes": "naive_bayes_classifier.pkl"
}
models = {name: load(path) for name, path in CLASSIFIERS.items()}

def analyze_method(method):
    line_count = method.end_lineno - method.lineno + 1
    cyclomatic_complexity = sum([block.complexity for block in cc_visit(ast.unparse(method))])

    return {
        "method_name": method.name,
        "line_count": line_count,
        "complexity": cyclomatic_complexity
    }

def classify_function(model, line_count, complexity):
    input_data = pd.DataFrame([[line_count, complexity]], columns=['line_count', 'complexity'])
    prediction = model.predict(input_data)
    return bool(prediction[0])

def detect_smell_type(line_count):
    if line_count > LINE_THRESHOLD:
        return "Long Method"
    else:
        return "High Cyclomatic Complexity"

def generate_refactoring_suggestion(code_smell, method_name):
    suggestions = {
        "Long Method": f"Refactor '{method_name}' by splitting it into smaller functions.",
        "High Cyclomatic Complexity": f"Reduce complexity in '{method_name}' by simplifying logic or extracting helper methods."
    }
    return suggestions.get(code_smell, "No suggestion available.")

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '../templates'))

@app.route('/')
def index():
    return render_template('index.html', classifiers=list(CLASSIFIERS.keys()))

@app.route('/analyze', methods=['POST'])
def analyze():
    code = request.form['code']
    selected_classifier = request.form['classifier']
    if not code:
        return jsonify({'error': 'No code provided.'}), 400
    if not selected_classifier:
        return jsonify({'error': 'No classifier provided.'}), 400
    
    classifier = models[selected_classifier]

    tree = ast.parse(code)
    functions = []
    results = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            analysis = analyze_method(node)
            functions.append(analysis)

    for func in functions:                
        is_smelly = classify_function(classifier, func['line_count'], func['complexity'])
        func['is_smelly'] = is_smelly
        
        if is_smelly:
            func['smell_type'] = detect_smell_type(func['line_count'])
            func['refactoring_suggestion'] = generate_refactoring_suggestion(func['smell_type'], func['method_name'])
            results.append(func)
    
    return jsonify(results)
    
if __name__ == '__main__':
    app.run(debug=True)