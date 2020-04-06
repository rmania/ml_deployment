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

### ML_system and architecture

**Key principles**
	- **Reproducibility**: Have the ability to replicate a given ML prediction (eact training data that was used, the, features, configuration, any third party libraries and infrastructure)
	- **Automation**: Retrain, update and deploy models as part of an automated pipeline (automate everything if possible)
	- **Extensibility**: Have the ability to easily add and update models.
	- **Modularity**: Preprocessing/feature engineering code used in training should be organized into clear pipelines
	- **Scalability**: Ability to serve model predictions to large numbers of customers (within time constraints)
	- **Testing**: Test variation between model versions
	
The architecture of a production machine learning system needs to take into account business requirements, as well as the unique challenges at the intersection of data science, software engineering and devops.

General ML Architectures

 - Train by batch, predict on the fly, serve via REST API (*)
 - Train by batch, predict by batch, serve through a shared database
 - Train, predict by streaming
 - Train by batch, predict on mobile (or other client)
 
 ![ml_architecture](/home/dmeijerink/pathe/ml_deployment/images/ml_architecture_comparison.png  "ml_architecture")
 
(*) Diagram of a possible architecture

![batch_predict_rest_api](/home/dmeijerink/pathe/ml_deployment/images/ml_architecture_batch_predict_rest_api.png  "batch_predict_rest_api")

Complexity arises when there is more than one environment:

![multiple_ml_envs](/home/dmeijerink/pathe/ml_deployment/images/multiple_ml_envs.png  "multiple_ml_envs")

![deployment_integration](/home/dmeijerink/pathe/ml_deployment/images/deployment_integration.png  "deployment_integration")

Reads on Building Reproducible Pipelines:
 - https://www.trainindata.com/post/building-and-deploying-reproducible-machine-learning-pipelines
 - https://arxiv.org/ftp/arxiv/papers/1810/1810.04570.pdf
 - https://petewarden.com/2018/03/19/the-machine-learning-reproducibility-crisis/
  - scaling ML_as_a_service: http://proceedings.mlr.press/v67/li17a/li17a.pdf
  - https://engineering.fb.com/ml-applications/introducing-fblearner-flow-facebook-s-ai-backbone/
  
 
 MLaaS - UITWERKEN !!!!
 
Again reproducacility in ML is hard because most machine learning methods rely on some sort of pseudorandomness for things like:
 - Weight initialization
 - Dropout
 - Subsetting/shuffling for mini-batches
 - Training/testing/validation split

More advanced topics: streaming approach (pattern 3 from the
lecture), Apache Kafka:
https://www.confluent.io/blog/using-apache-kafka-drive-cutting-edge-machine-learning
Code examples: https://github.com/kaiwaehner/kafka-streams-machine-learning-examples
Tutorial working with Apache Spark for large scale data processing:
https://towardsdatascience.com/deep-learning-with-apache-spark-part-1-6d397c16abd

Advanced architecture discussions from larger companies:
Netflix on architecture for recommendation systems:
https://medium.com/netflix-techblog/system-architectures-for-personalization-and-recommendation-e081aa94b5d8
Google’s TFX Paper: https://ai.google/research/pubs/pub46484
Uber’s (very complex!) Michelangelo System: https://eng.uber.com/michelangelo/
Testing Machine Learning Systems: https://ai.google/research/pubs/pub45742

### ML Pipeline: writing Production code

 - Procedurial Prgramming --> procedures, also known as routines, subroutines or functions, are carried out as a series of computational steps. (yaml, config, .py scripts etc instead of code in notebooks and lab envs)
 - Object Oriented Programming - OOP. we write code in the form of “objects”. This “objects” can store data, and can also store instructions or procedures to modify that data.
 - Pipelines --> set of data processing steps connected in series, where typically, the
output of one element is the input of the next one.
 - Skearn API (Predictors, Transformers, Pipeline)