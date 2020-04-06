import preprocessing_functions as pf
import config

# ================================================
# TRAINING STEP - IMPORTANT TO PERPETUATE THE MODEL

# Load data
data = pf.load_data(config.PATH_TO_DATASET)

# divide data set
X_train, X_test, y_train, y_test = pf.divide_train_test(data, config.TARGET)

# get first letter from cabin variable
X_train['cabin'] = pf.extract_cabin_letter(df=X_train, var='cabin')
X_test['cabin'] = pf.extract_cabin_letter(df=X_test, var='cabin')

# impute categorical variables
for var in config.CATEGORICAL_VARS:
    X_train[var] = pf.impute_na(X_train, var, replacement='Missing')
    X_test[var] = pf.impute_na(X_test, var, replacement='Missing')

# impute numerical variable
for var in config.NUMERICAL_TO_IMPUTE:
    X_train[var] = pf.add_missing_indicator(df=X_train, var=var)
    X_test[var] = pf.add_missing_indicator(df=X_test, var=var)

# Group rare labels
for var in config.CATEGORICAL_VARS:
    X_train[var] = pf.remove_rare_labels(X_train, var, config.FREQUENT_LABELS[var])
    X_test[var] = pf.remove_rare_labels(X_test, var, config.FREQUENT_LABELS[var])

# encode categorical variables
X_train = pf.encode_categorical(df=X_train, var=config.CATEGORICAL_VARS)
X_test = pf.encode_categorical(df=X_test, var=config.CATEGORICAL_VARS)

# check all dummies were added
X_train = pf.check_dummy_variables(X_train, config.DUMMY_VARIABLES)
X_test = pf.check_dummy_variables(df=X_test, dummy_list=config.DUMMY_VARIABLES)

# train scaler and save
scaler = pf.train_scaler(X_train[config.FEATURES],
                         config.OUTPUT_SCALER_PATH)

# scale train set
X_train = scaler.transform(X_train[config.FEATURES])
X_test = scaler.transform(X_test[config.FEATURES])

# train model and save
pf.train_model(X_train,
               y_train,
               config.OUTPUT_MODEL_PATH)

print('Finished training')