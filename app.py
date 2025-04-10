import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("Brain Tumors.h5")
    return model

model = load_model()


class_labels = ['glioma', 'meningioma', 'notumor', 'pituitary']

st.title("🧠 Brain Tumor Classifier")
st.write("Upload an MRI image to predict the type of brain tumor.")

uploaded_file = st.file_uploader("Choose an MRI image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption='Uploaded MRI.', use_column_width=True)

    # Preprocessing
    img = image.resize((224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    # Prediction
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    predicted_class = class_labels[tf.argmax(score)]

    st.markdown("---")
    st.success(f"✅ **Predicted Class:** `{predicted_class}`")





