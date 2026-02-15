# Model Card

## Model Details
Name - Census Income Classifier
Version - V1.0
Date Trained - 2/14/26
Author - Aubrie Smith
Algorithm - RandomForestClassifier
Encoders - OneHotEncoder for categorical features, LabelBinarizer for labels

## Intended Use
Model uses census data to predict whether an individual earns more than $50K per year.  The predictions can be used for research or demographic analysis.  It's intended use is for demographic insights and income predictions.  

## Training Data
The model was trained on the U.S. Census data (census.csv) with 32,560 files and 15 features including: age, workclass, education, marital status, race, sex, native-country, salary and other income information.

## Evaluation Data
Evaluation was conducted on 20% of the original dataset that was reserved as a test set.  Model predictions were compared to the true labels for both overall performance and on slices of categorical features.

## Metrics
This model reports precision, recall, F1, and accuracy metrics if desired on quantitative perfomance, both overall and slice-based.
Overall test set performance:
Precision: 0.7419 | Recall: 0.6384 | F1: 0.6863

Slice-based performance examples:
workclass: Private, Count: 4,578
Precision: 0.7376 | Recall: 0.6404 | F1: 0.6856

education: Bachelors, Count: 1,053
Precision: 0.7523 | Recall: 0.7289 | F1: 0.7404

## Ethical Considerations
This model uses many demographic features such as race, sex, education, etc, which may lead to potential bias or fairness concerns, especially among overly or under represented populations.  It should be recognized that the model's performance may differ across groups.

## Caveats and Recommendations
Because this model was trained only on a subset of census data, it may not generalize to all populations well.  Additionally, some categories have few samples, which may lead to lower performance.  Predictions are for research and educational purposes only and should not be used for weighty decisions like loan approval or hiring.  Future retraining on more representative datasets could lead to better modeling.