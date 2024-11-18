# CodeRefactorAssistant
A code refactor assistant, which will detect code smells and help refactor the code using machine learning algorithms.

`pip install pandas numpy scikit-learn nltk astroid radon matplotlib`

* Update `config.py` to change the thresholds for code smell detection.
* Keep your code files in the `data` folder to detect code smells.
* Run `python src/code_smell_label_script.py` to generate a `csv` file filled with information like line count, complexity, is code smell detected etc.
* Run `python src/random_forest_classifier.py` to run the Random Forest classification algorithm on the generated data.
