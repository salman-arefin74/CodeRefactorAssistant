complex_code_thresholds = {
        "long_method": {
            "line_count": 15,
            "cyclomatic_complexity": 5
            }
        }

refactor_approaches = {
        "long_method": ["divide_into_chunks"]
        }

def get_complex_code_thresholds(complexity_type):
    return complex_code_thresholds.get(complexity_type)

def get_refactor_approaches(complexity_type):
    return refactor_approaches.get(complexity_type)