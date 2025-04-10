# Brain Tumor Classification Project

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

## How to Use
1. Run the Streamlit application using the command:
2. Upload an MRI image through the web interface.
3. The model will predict the type of brain tumor and display the confidence level of the prediction.

## Conclusion
This project aims to enhance the diagnostic process for brain tumors by leveraging the power of deep learning and providing an accessible tool for healthcare professionals. The implementation of the model and web application demonstrates the potential of AI in the medical field.
