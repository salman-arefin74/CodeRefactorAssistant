complex_code_thresholds = {
        "long_method": {
            "line_count": 30,
            "cyclomatic_complexity": 10
            }
        }

def get_complex_code_thresholds(complexity_type):
    return complex_code_thresholds.get(complexity_type)