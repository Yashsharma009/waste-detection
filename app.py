import streamlit as st
import base64
import firebase
import env
import os

# health check
def health_check():
    st.write('Running!')

# Performing image Recognition on Image, sent as bytes via POST payload
def detect():

    imgBytes = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    
    if imgBytes is not None:
        imgdata = imgBytes.read()
        
        with open("temp.png", 'wb') as f:
            f.write(imgdata)
            
        st.write("Successfully received image")
        
        # Pass image bytes to classifier
        result = classify.analyse("temp.png")
        
        # Return results as neat JSON object
        st.json(result)
        
        response_data = result
        
        db = firebase.Firebase()
        db.authenticate()
        db.push(response_data)
        
        st.write("Updated Firebase.")

# Instantiate Streamlit
def main():
    st.title("Image Recognition App")
    
    if st.sidebar.button("Health Check"):
        health_check()
    
    if st.button("Detect"):
        detect()

if __name__ == '__main__':
    main()
