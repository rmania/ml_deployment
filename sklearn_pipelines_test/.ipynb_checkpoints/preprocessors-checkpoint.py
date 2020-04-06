import numpy as np
import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin
import config

# Add binary variable to indicate missing values
class MissingIndicator(BaseEstimator, TransformerMixin):

    def __init__(self, variables=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables


    def fit(self, X, y=None):
        # we need the fit statement to accomodate the sklearn pipeline
        return self


    def transform(self, X):

        X = X.copy()
        for feature in self.variables:
            X[feature + '_NA'] = np.where(df[var].isnull(), 1, 0)
            
        return X

    
    
# categorical missing value imputer
class CategoricalImputer(BaseEstimator, TransformerMixin):

    def __init__(self, variables=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y=None):
        # we need the fit statement to accomodate the sklearn pipeline
        return self

    def transform(self, X):
        X = X.copy()
        for feature in self.variables:
            X[feature] = X[feature].fillna('Missing')

        return X


# Numerical missing value imputer
class NumericalImputer(BaseEstimator, TransformerMixin):

    def __init__(self, variables=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y=None):
        # persist mode in a dictionary
        self.imputer_dict_ = {}
        
        for feature in self.variables:
            self.imputer_dict_[feature] = X[feature].median()
        return self

    def transform(self, X):

        X = X.copy()
        for feature in self.variables:
            X[feature].fillna(self.imputer_dict_[feature], inplace=True)
        return X


# Extract first letter from string variable
class ExtractFirstLetter(BaseEstimator, TransformerMixin):

    def __init__(self, variables=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y=None):
        # we need this step to fit the sklearn pipeline
        return self

    def transform(self, X):
        X = X.copy()
        for feature in self.variables:
            X[feature] = X[feature].str[0] 

        return X

# frequent label categorical encoder
class RareLabelCategoricalEncoder(BaseEstimator, TransformerMixin):

    def __init__(self, tol=0.05, variables=None):
        
        self.tol = tol
        
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y=None):

        # persist frequent labels in dictionary
        self.encoder_dict_ = {}

        for var in self.variables:
            # the encoder will learn the most frequent categories
            t = pd.Series(X[var].value_counts() / np.float(len(X)))
            # frequent labels:
            self.encoder_dict_[var] = list(t[t >= self.tol].index)

        return self

    def transform(self, X):
        X = X.copy()
        for feature in self.variables:
            X[feature] = np.where(X[feature].isin(self.encoder_dict_[
                    feature]), X[feature], 'Rare')

        return X

# string to numbers categorical encoder
class CategoricalEncoder(BaseEstimator, TransformerMixin):

    def __init__(self, variables=None):
        
        self.dummy_list = config.DUMMY_VARIABLES
        
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y=None):
        
        # HINT: persist the dummy variables found in train set
        # persist transforming dictionary
        self.dummy_dict_ = {}
        
        self.dummies = pd.get_dummies(X[self.variables], drop_first=True).columns
        for var in self.variables:
            self.dummy_dict_[var] = self.dummies
        
        return self

    def transform(self, X):
        # encode labels
        X = X.copy()
        # get dummies
        for feature in self.variables:
            X[feature] = X[feature].map(self.encoder_dict_[feature])
        # drop original variables
            X.drop(labels=[features], axis=1, inplace=True)
        # add missing dummies if any
            missing_vars = [var for var in self.dummy_list if var not in self.dummies]
    
            if len(missing_vars) == 0:
                print('All dummies were added')
            else:
                for var in missing_vars:
                    X[var] = 0
          
        return X
