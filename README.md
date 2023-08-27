# USD-HackAThon-2023-Fall

Hack-a-thon USD MS-AAI Submission for August 25-26.

This template was used from:
https://github.com/readytensor/usd-hackathon-fars-template-jupyter-notebook/

See the above link for information on docker and folder structure. 

# Model Details

The model used is an sklearn StackingClassifier which uses 3 base classifiers:
- sklearn RandomForestClassifier 
- sklearn GradientBoostingClassifier
- XGBoost XGBClassifier

Class imbalance has been addressed by using a sample_weight during the model fitting. 

The missing values are imputed using sklearn SimpleImputer.

## Process to come up with the model

1. I ran most of the common sklearn models and picked the model with the highest accuracy. This ended up being the GradientBoostingClassifier.
2. From there, I started trying to tune the model by running GridSearchCV and RandomizedSearchCV. GridSearchCV ended up being too time consuming for my schedule so I used RandomizedSearchCV. 
3. After tuning and seeing good results from GradientBoostingClassifier I decided to go back and see if I could tune any of the other sklean models to get better results. I found the results RandomForestClassifier performed well and decided to try the StackingClassifier to see if both models would perform even better when ran together. This slightly improved the score. Finally, I read about optimized Gradient Boosting and decided to try out XGBoost. 
4. I tried improving the value imputation and feature selection but did not see very much improvement in the model. 
