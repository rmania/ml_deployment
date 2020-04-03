# Deployment of Machine Learning models


First some usefull links for extra info on:
	- best resources to learn ML: https://www.trainindata.com/post/best-resources-to-learn-machine-learning
	- Feature Engineering: https://www.trainindata.com/post/data-processing
 
Typical ML model Pipeline steps

![ml_steps](/home/dmeijerink/pathe/ml_deployment/images/ml_pipeline_steps.png  "ml_steps")

these are the steps we perform before getting to the model deployment: puuting the model in the cloud or any other system where it can be accessed by our other systems in the business in other to get its predictions. 

 - **Feature Engineering**
 
	- Imputing/ remove missing data
 	 - outlier detection
  	- labels in categorical variables (high cardinality, infrequent labels, strings)
 	- categorical variable encoding 
 	-  check assumptions about distributions
 	- features magnitudes - scale (ml models sensitive to feature scale: Linear and Logistic regression, NN, SVM, KNN, KM, LDA and PCA)
 	
Some take-aways of steps I tend to miss

 - missing values in numerical variables: 1) add a binary missing value indicator variable before replacing missing values in the original variable with the mode 2) analyse rare labels (low cardinality) 

Some tools helful for FE purposes:
	- FeatureTools https://www.featuretools.com/
	- MLExtend http://rasbt.github.io/mlxtend/
	- good additional resources: https://www.trainindata.com/post/best-resources-to-learn-feature-engineering
	- https://www.trainindata.com/post/feature-engineering-comprehensive-overview

 	
  - **Feature Selection** --> process (filter, wrapper and embedded methods - the latter co-occurs with actually training the ml algorithm like Lasso-regression) to identify the most predictive features. There are important reasons to apply thorough and robust feature selection methods.
  
  	• Simple models are easier to interpret
	• Shorter training times
	• Enhanced generalisation by reducing overfitting
	• Easier to implement by software developers (Model production)
	• Reduced risk of data errors during model use
	• Data redundancy
	• Smaller json messages sent over to the model (Json messages contain only the necessary variables / inputs)
	• Less lines of code for error handling
	• Error handlers need to be written for each variable / input
	• Less information to log
	• Less feature engineering code
	
**Reproducibility** in machine learning modeling is an important problem faced by data scientists and organisations seeking to put machine learning models into production. Reproducibility means that given the same inputs, we should obtain exactly the same outputs. In other words, our research models -in the research environment-, and our deployed models -in the production environment-, should produce the same score for the same input data. the costs of non-reproducible ML are high:

 - Financial costs
 - Time costs (lost time)
 - Reputational costs
 - Compliance costs
 - Regulatory costs
 
The problems with reproducibility can arise in any and all of the machine learning pipeline steps: Data gathering, Feature extraction and engineering, Feature selection, Model building and Data scoring. This is because all these steps involve elements of randomness. For example, if gathering data with SQL, there is an element of randomness when retrieving the rows from the database. During feature engineering, if we replace missing information by a random extraction of non-missing observations, we are introducing another layer of randomness. Machine learning models and feature selection algorithms involve randomness during model fitting. Think for example Random Forests; there is an element of randomness to select the features at each split, as well as to bootstrap a sample of the dataset to fit each tree. For neural networks there is an element of randomness to initialise the network weights.