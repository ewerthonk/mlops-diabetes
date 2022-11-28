# Machine Learning Operations - Diabetes
<div align="center">
<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
<img src="https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white">
<img src="https://img.shields.io/badge/Joblib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black">
<img src="https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white">
<img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white">
<img src="https://img.shields.io/badge/serverless-%2314162c?style=for-the-badge&logo=rescript&logoColor=e34c4c">
</div>

## 🧾 Table of Contents
  - [👨🏻‍🏫 Introduction](#-introduction)
  - [🗺 Project](#-project)
  - [🗄 Reproducibility: Make and Folder Structure](#-reproducibility-make-and-folder-structure)
  - [📚 Learnings](#-learnings)
  - [🛣 Roadmap](#-roadmap)

## 👨🏻‍🏫 Introduction
The focus of this project is on the productionizing/operation of a serverless Machine Learning on AWS.

I chose a simple dataset from the US National Institute of Diabetes, Digestive and Kidney Diseases: Pima Indian Diabetes. The dataset presents diagnostic measurements from female patients of at least 21 years old of Pima heritage as variables and indicates if the patient has or has not diabetes as an outcome.

A quick process of ML is developed in the notebook of the project. Data is ingested from AWS S3, the model - that predicts if a patient has diabetes or not based on 8 medical exam features - is created locally and deployed using serverless framework to AWS Lambda. Then, AWS API Gateway makes it available for the public.

The features are the following:
- pregnancies: number of pregnancies the patient had.
- glucose: plasma glucose concentration a 2 hours in an oral glucose tolerance test.
- blood_pressure: Diastolic blood pressure (mm Hg).
- skin_thickness: Triceps skin fold thickness (mm).
- insulin: 2-Hour serum insulin exam (mu U/ml).
- bmi: Body mass index (weight in kg/(height in m)^2).
- diabetes_pedigree_function: genetic predisposition to diabetes (from 0 to 1)
- age: patient age.

The model achieved an accuracy of 72% and an ROC-AUC of 71%.

You can get an example prediction for a 55 years-old patient, who had 3 pregnancies, with a glucose of 200,a blood-pressure of 100, an insulin of 200, triceps skin thickness of 50 an a diabetes genetic function of 0.5 in the following link:

https://q6l78vh36a.execute-api.sa-east-1.amazonaws.com/development/lambda-prediction?pregnancies=3&glucose=200&blood_pressure=100&skin_thickness=50&insulin=200&bmi=40&diabetes_pedigree_function=0.5&age=55

You may change the parameters directly on the URL to get different predictions 😁

## 🗺 Project
![Project](/references/mlops-diabetes.png)

## 🗄 Reproducibility: Make and Folder Structure
#### To reproduce the project

```git clone https://github.com/ewerthonk/mlops-diabetes.git``` 

To locally clone the project. Then, run the following commands in the project folder:

```make create_environment``` 

To create the project environment with all modules from requirements.txt.

```make upload_data_to_s3``` 

To upload the diabetes.csv from /data folder to your AWS S3.

```make download_data_from_s3``` 

To download the diabetes.csv from your AWS S3 to /data folder.

```make deploy_model``` 

To deploy the model to your AWS Lambda using serverless-framework. Requires Docker, NodeJS and serverless-framework.

#### Folder Structure

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make deploy_model`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │
    ├── models             <- Trained and serialized models.
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-ejk-creating-the-model`.
    │
    ├── deployment         <- All files dockerized and deployed to AWS Lambda, like "handler.py".
    │
    ├── references         <- Explanatory materials.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip list --format=freeze > requirements.txt`

## 📚 Learnings
- This project idea was initially conceived during [Ada's Data Science Degree](https://ada.tech/sou-aluno). I also used two Udemy courses to learn more about serverless deployment of machine learning models: [Deploy Serverless Machine Learning Models to AWS Lambda](https://www.udemy.com/course/deploy-serverless-machine-learning-models-to-aws-lambda/) and [Deploy Machine Learning Models on GCP + AWS Lambda (Docker)](https://www.udemy.com/course/deploy-machine-learning-model/).
- Deploying the model was really troublesome. It took many iterations (package and plugin instalation, serverless.yml editing, reducing function size, etc). This guide helped a lot - it is the best I found on the internet about this subject: [How to Handle your Python packaging in Lambda with Serverless plugins](https://www.serverless.com/blog/serverless-python-packaging/).

## 🛣 Roadmap
- Create a frontend for this API - I think a streamlit on an AWS EC2 instance would be really great for this.
- Deepen the machine learning process: EDA, Model Selection and Model Tunning.
- Implement more functionalities for CI/CD process, like direct Dockerizing and Github Actions. I am already learning more about it in this course: [Deployment of Machine Learning Models](https://www.udemy.com/course/deployment-of-machine-learning-models/).
- Deploy the serverless model on more Cloud Services.
