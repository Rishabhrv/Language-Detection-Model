# Language-Detection-Model

The Language Detection Model is a machine learning-based approach that accurately detects the language of a given text. It can identify 17 different languages, including English, Malayalam, Hindi, Tamil, Portuguese, French, Dutch, Spanish, Greek, Russian, Danish, Italian, Turkish, Swedish, Arabic, German, and Kannada. The model utilizes the MultinomialNB algorithm and achieves an impressive accuracy of 98%. Streamlit is used for user-friendly UI experience.

**Installation**
To run this project, please follow the steps below:

Clone the repository to your local machine.
Navigate to the project directory.

git clone <repository_url>
cd <project_directory>

**Usage**
Once you have installed the necessary dependencies, you can run the Language Detection Model with the following command:

streamlit run app.py

This command will launch the Streamlit application, providing a user-friendly UI for interacting with the Language Detection Model.

File Descriptions
This project includes the following files and folders:

**app.py:** This file contains the main code for the Language Detection Model. It utilizes the trained MultinomialNB algorithm to predict the language of the provided text. Streamlit is used to create an interactive and visually appealing user interface.

**Language_Detection.ipynb:** This Jupyter Notebook file provides the detailed implementation of the Language Detection Model. It includes the code, explanations, and steps involved in training the model and achieving an accuracy of 98%.

***.pkl files:** These are the pickle files that store the trained model and other necessary data used by the Language Detection Model. The specific names and purposes of these files may vary based on the implementation.

**data folder:** This folder contains the data used for training and evaluating the Language Detection Model. 

Feel free to explore and modify the code files, Jupyter Notebook, and data folder to suit your requirements.
