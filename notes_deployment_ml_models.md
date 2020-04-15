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

 - Procedurial Programming --> procedures, also known as routines, subroutines or functions, are carried out as a series of computational steps. (yaml, config, .py scripts etc instead of code in notebooks and lab envs)
 - Object Oriented Programming - OOP. we write code in the form of “objects”. This “objects” can store data, and can also store instructions or procedures to modify that data.
 - Pipelines --> set of data processing steps connected in series, where typically, the
output of one element is the input of the next one.
 - Skearn API (Predictors, Transformers, Pipeline) leverages power of acknowledged api's
 
 Some useful modules:
  - https://github.com/solegalli/feature_engine and https://feature-engine.readthedocs.io/en/latest/
  
  Resources to Improve as a Python Developer
   - https://gist.github.com/sloria/7001839
    - https://realpython.com/tutorials/best-practices/
  learn IDE (integrated development environments) like pycharm:
   - https://www.tutorialspoint.com/pycharm/index.htm
   - https://www.fullstackpython.com/pycharm.html
   
 (A few) Software Engineering Good Practices:
  - Version control
  - Test: Unit, Integration, acceptance ...
  - Trunk based development and peer reviews
  - understand system dependencies
  - CI/CI pipelines
  - Python --> Style (PEP 8), Type Hint, Literal String Interpolation (f"{}") Forcing Key Word Arguments (kwargs)   
   
  - **pytest** is the defacto standard. Killer feature here is : https://docs.pytest.org/en/latest/fixture.html#fixture They provide a fixed baseline so that tests execute reliably and produce consistent, repeatable, results.
  - **tox** aims to automate and standardize testing in Python. https://tox.readthedocs.io/en/latest/
  
  - package your model for reproducability with effective use of versioning (including data)
  - clearly organize preprocessing and feature engineering steps
  - persist your predictions (logs or databases)
  - abstract model details in congif
  - validate your data
  
### model serving via an REST API
  
An **API** is an application programming interface. It is a set of rules that allow programs to talk to each other. The developer creates the API on the server and allows the client to talk to it.
**REST** determines how the API looks like. It stands for Representational State Transfer”. It is a set of rules that developers follow when they create their API. 

https://www.smashingmagazine.com/2018/01/understanding-using-rest-api/

a Praised Python Flask tutorial : https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

 - Make your api a thin layer (minimizes the chance of having code logic for your models spread across 2 different applications which increases the chances of forgetting to update one)
 -  validate inputs carefully (consider using a schema -python marshmallow module: https://marshmallow.readthedocs.io/en/stable/quickstart.html#declaring-schemas) 
 - log all key inputs and errors for reproducability and debugging
 - test the api
 
### CI CD
 
 Testing and deploying our applications according to the CI/CD method means:
 - The system in an “always releasable” state
 - Faster, regular release cycles
 - Building and testing is automated
 - Delivery and deployments are automated (at least to some extent)
 - Visibility across the company (and audit log)

### Differential tests

A type of test that compares the differences in execution from one system version to the next when the inputs are the same.
 - Sometimes called “back-to-back” testing
 - Very useful for detecting machine learning system errors that do not raise exceptions.
 - Tuning them is a balancing act (depends on business requirements).
 - Can prevent very painful mistakes that are not detected for long periods of time.
 
 good practice to put a `differential_tests` folder with 

### Docker

create, deploy, and run applications by using containers. Containers allow a developer to package up an application with all of the parts it needs, such as libraries and other dependencies, and deploy it as one package. 
installation on Ubuntu: https://docs.docker.com/engine/install/ubuntu/

### AWS ECS

Amazon Elastic Container Service (Amazon ECS) is a highly scalable, fast, container management service that makes it easy to run, stop, and manage Docker containers on a cluster.
Two main launch types: Fargate and EC2. 

Course stipulates: task definition so Amazon ECS knows which Docker image to use for containers, how many containers to use in the task, and the resource allocation for each container. 

Containerization has transformed how we deploy software
 - options: Kubernetes, ECS, Docker Swarm
 - Kubernetes is the container orchestration engine of choice......But has the most complex setup and management
 - Self-Managed (Kubernetes) vs. Fully managed service (ECS)
 - Kubernetes is a good choice in many scenarios (but not all)
 - New Player: Amazon Elastic Container Service for Kubernetes (EKS) = managed Kubernetes
 
 Steps in course: 
 
  - make an AWS account
  - set up IAM
  	- create a new group (collection of permissions) 
  	- attach permissions (AmazonEC@ContainerServiceFullAccess +  AmazonEC@ContainerRegisttryFullAccess + IAMReadOnlyAccess)
  - add user (ecs-admin) --> programmatic access
  - permissions for user (we attach a group we just created)
  - (skip add key)
  - create user (get he access key id and the secret access key that is only shown here and one should store in a fault)
  
  - install AWS CLI (https://docs.amazonaws.cn/en_us/cli/latest/userguide/install-linux.html
  - AW CLI config steps
  	- `aws configure` --> AWS access key and the secret key 
  	- `aws iam list-users` for overview
  - ECR --> get started, create name for repo, get the URI that we need
  - via AWS CLI we can the Docker Images and put them in ECR --> build locally and push to ECR.
  	- go to project root
  	- activate venv
  	- get the ENV VARIABLES ready to use (test with echo %NAME_ENV_VARIABLE)
  	- `docker build --build-arg
PIP_EXTRA_INDEX_URL=${PIP_EXTRA_INDEX_URL} -t
YOUR_APP_NAME:latest .`
	- `docker tag YOUR_APP_NAME:latest ${AWS_ACCOUNT_ID}.dkr.ecr.us-
east-1.amazonaws.com/YOUR_APP_NAME:latest`
	- before we can push we need to login to the ECR: `aws ecr get-login --no-include-email --region us-east-1` 
	- this will spit out the DOCKER LOGIN. Copy and paste :
	- `docker login -u AWS -p DOCKER LOGIN
	- `docker push ${AWS_ACCOUNT_ID}.dkr.ecr.us-east-
1.amazonaws.com/YOUR_APP_NAME:latest`
	- check on AWS ECR if image URI and tag have been successfully created
	
**creating ECS cluster with FARGATE method**
	- go to ECR service, copy latest IMAGE URI
	- go to ECS --> clusters --> get started --> click on "custom container definition" 
	- in image paste the  IMAGE URI, port-mapping: 5000, advanced settings: environment variables: PIP_EXTRA_INDEX_URL (the Gemfury url) . create , define your service: no load balancer, give it the cluster name (ml-api-cluster f.i.)
	- after creation go to view service: task (tab) you will see "pending" will take some minutes. Wait until finished
	- got task tab and copy the public IP. past in browser with port 5000/ health you should see ok
	
**updating cluster containers**
 
 - f.i. update the API VERSION number
 - build the updated Docker Image locally, tagged it and pushed it to the AWS registry where the updated IMAGE URI should be available.
 - udpate the ECS task in `aws ecs update-service --cluster YOUR_CLUSTER_NAME --service
YOUR_SERVICE_NAME --task-definition YOUR_TASK_DEFINITION --
force-new-deployment`
 - check if successful: on AWS ECS cluster -- task tab where we should see an additional task being provisioned. When complete there should be a new Network Public IP address (in details). To get a consistent IP adress or a range of IP addresses we need to use Load Blancer.
 -  check new public IP adress and endpoint to see that the new image is being used. 
 
**tear down ECS cluster**
`https://docs.aws.amazon.com/AmazonECS/latest/developerguide/delete_cluster.htm

**adding deployment to ECS to the CI_CD pipeline**
 - add new job (commands) to the `circle/congif.yml` 
 - add new ENV VARIABLES to circle CI: AWS ACCESS KEY, AWS ACCOUNT ID, AWS_DEFAULT_REGION, AWS_SECRET_ACESS_KEY
 - change MAKEFILE : new commands: build-ml-api-aws with the docker steps build, push and tag 
	

  
  
  
  
  
  
 
 
 
