# CodeRefactorAssistant
A code refactor assistant, which will detect code smells and help refactor the code using machine learning algorithms.

`pip install pandas numpy scikit-learn nltk astroid radon matplotlib flask`

* Update `config.py` to change the thresholds for code smell detection.
* Keep your code files in the `data` folder to detect code smells.
* Run `python src/main.py [classifier name]` to generate a `csv` file filled with information like line count, complexity, is code smell detected, type of code smell, and refactoring suggestions etc.

For example, to run the Random Forest Classifier, run:
`python src/main.py random_forest_classifier.pkl`

To run the UI:
Run `python src/ap.py` and the UI will run in http://127.0.0.1:5000/