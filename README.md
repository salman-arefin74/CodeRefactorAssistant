# CodeRefactorAssistant
A code refactor assistant, which will detect code smells and help refactor the code using machine learning algorithms.

`pip install pandas numpy scikit-learn nltk astroid radon matplotlib flask`

To train the classifiers:
* Update config.py to change the thresholds for code smell detection.
* Keep your code files in the data folder to detect code smells.
* Run python src/code_smell_label_script.py to generate a CSV file filled with information such as line count, complexity, whether code smell is detected, etc.
* Run python src/random_forest_classifier.py to run the Random Forest classification algorithm on the generated data.
* Run python src/knn_classifier.py to run the K-Nearest Neighbor classification algorithm on the generated data.
* Run python src/naive_bayes_classifier.py on the generated data to run the Naive Bayes classification algorithm.
* Run python src/support_vector_machine_classifier.py to run the Support Vector Machine classification algorithm on the generated data.
* Run `python src/main.py [classifier name]` to generate a `CSV` file filled with information like line count, complexity, code smell detected, type of code smell, refactoring suggestions, etc.

For example, to run the Random Forest Classifier, run:
`python src/main.py random_forest_classifier.pkl`

To run the UI:
Run `python src/ap.py`, and the UI will run in http://127.0.0.1:5000/
