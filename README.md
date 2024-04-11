## 🫀  Heart Disease Prediction

Heart disease remains a leading cause of death globally. The aim of this project is t apply machine learning methods to predict heart disease in patients.

**Features**
The predictions were made based on several features such as chest pain type, Resting electrocardiographic results, serum cholesterol, etc. as described in the [data description file](data_description.md)

**Source**
This dataset was gottenfrom [kaggle](https://www.kaggle.com/datasets/yasserh/heart-disease-dataset)

**Steps:**
* **Exploratory Data Analysis (EDA):** Various exploratory analysis were performed in order to get insights about the dataset, uncovering its structure, identifying potential issues, and visualizing relationships between various features.

* **Data Cleaning and Preprocessing:**
  Various cleaning and preprocessing were performed to ensure quality and buiding reliable models, some of them include: 
  + Drop duplicate rows
  + Ensureing consistency of input
  + Standard Scaling
  + One hot encoding

* **Model Building and Evaluation:**
  - The model is built using various models such as logistic regression, randomforest and catboost
  - Hyperparameter tuning was also performed to optimize model performance and generalization.
  - The datset is relatively balanced so we focused on accuracy various evaluation metrics, such as precision, recall, and F1-score, were used to assess model performance.

**Tools and Technologies:**
* Programming language: Python
* Libraries : Pandas, NumPy, scikit-learn, CatBoost, XGBoost
* IDE/Notebook: Jupyter lab

**Note!**
This README will evolve as the project progresses. You may check back for updates on findings and challenges encountered.  
A deployment pipeline will be added in the future