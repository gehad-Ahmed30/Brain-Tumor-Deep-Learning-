# Brain Tumor Classification Project 
![Photo](Screenshot(210).png )

![Photo](Screenshot(211).png)

![Photo](Screenshot(212).png)

## Project Overview
The Brain Tumor Classification project is designed to develop a deep learning model that can accurately classify MRI images of the brain into four categories: Glioma, Meningioma, No Tumor, and Pituitary. The primary goal of this project is to assist medical professionals in diagnosing brain tumors by providing an automated and reliable tool for image analysis.

## Objectives
- **Develop a Convolutional Neural Network (CNN)**: Utilize the EfficientNetB3 architecture to build a model that can learn from a dataset of MRI images.
- **Image Preprocessing**: Implement preprocessing techniques such as resizing and normalization to prepare the images for input into the model.
- **Model Training**: Train the model using a labeled dataset and evaluate its performance on validation and test datasets.
- **Deployment**: Create a user-friendly web application using Streamlit that allows users to upload MRI images and receive predictions regarding the type of brain tumor present.

## Dataset
The dataset consists of a collection of MRI images classified into four categories:
- **Glioma**
- **Meningioma**
- **No Tumor**
- **Pituitary**

The model is trained on a balanced dataset to ensure robust performance across all classes.

## Technologies Used
- **TensorFlow**: For building and training the deep learning model.
- **Streamlit**: For creating the web application interface.
- **Pandas and NumPy**: For data manipulation and processing.
- **Matplotlib**: For visualizing training results and data samples.

## Model Performance
The model achieved the following performance metrics on the test dataset:

- **Accuracy**: 98%
- **Precision, Recall, F1-Score**:

| Class        | Precision | Recall | F1-Score | Support |
|--------------|-----------|--------|----------|---------|
| Glioma       | 0.99      | 0.90   | 0.94     | 149     |
| Meningioma   | 0.94      | 0.97   | 0.95     | 143     |
| No Tumor     | 1.00      | 0.99   | 1.00     | 200     |
| Pituitary    | 0.93      | 0.99   | 0.96     | 164     |
| **Accuracy** |           |        | **0.98** | 656     |
| Macro Avg    | 0.97      | 0.96   | 0.96     | 656     |
| Weighted Avg | 0.98      | 0.98   | 0.9     | 656     |

## How to Use
1. Run the Streamlit application using the command:  
   ```bash
   streamlit run app.py

2. Upload an MRI image through the web interface.
3. The model will predict the type of brain tumor and display the confidence level of the prediction.

## Conclusion
This project aims to enhance the diagnostic process for brain tumors by leveraging the power of deep learning and providing an accessible tool for healthcare professionals. The implementation of the model and web application demonstrates the potential of AI in the medical field.
