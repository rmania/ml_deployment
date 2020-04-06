# ====   PATHS ===================

TRAINING_DATA_FILE = "titanic.csv"
PIPELINE_NAME = 'logistic_regression.pkl'


# ======= FEATURE GROUPS =============

TARGET = 'survived'

FEATURES = ['pclass', 'age', 'sibsp', 'parch', 'fare','age_NA', 'fare_NA',
       'sex_male', 'cabin_Missing', 'cabin_Rare', 'embarked_Q',
       'embarked_Rare', 'embarked_S', 'title_Mr', 'title_Mrs', 'title_Rare']


CATEGORICAL_VARS = ['sex', 'cabin', 'embarked', 'title']

NUMERICAL_VARS = ['pclass', 'age', 'sibsp', 'parch', 'fare']


DUMMY_VARIABLES = ['sex_male', 'cabin_Missing', 'cabin_Rare', 'embarked_Q',
                   'embarked_Rare', 'embarked_S', 'title_Mr', 'title_Mrs',
                   'title_Rare']
CABIN = 'cabin'