import streamlit as st
from PIL import Image
import io
import base64
from logic import get_emotions_from_image_async
import json
import asyncio


async def main():
    st.title("Face Emotion Detection")
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    # Create a unique identifier for the current file to track changes.
    current_file_id = None
    if uploaded_file is not None:
        current_file_id = f"{uploaded_file.name}-{uploaded_file.size}"

    # If the file is removed or a new file is uploaded, clear old results.
    if st.session_state.get('current_file_id') != current_file_id:
        st.session_state.current_file_id = current_file_id
        if 'emotion_response' in st.session_state:
            del st.session_state['emotion_response']

    if uploaded_file is not None:
        file_bytes = uploaded_file.read()
        if file_bytes:
            image = Image.open(io.BytesIO(file_bytes))
            st.image(image, caption="Uploaded Image", use_container_width=True)
            encoded_string = base64.b64encode(file_bytes).decode("utf-8")
            if st.button("Get Emotions"):
                with st.spinner("Processing image and detecting emotions..."):
                    response = await get_emotions_from_image_async(encoded_string=encoded_string)
                    st.session_state["emotion_response"] = response.content
                    st.rerun()

    # Display results if available
    if "emotion_response" in st.session_state:
        st.markdown("### Results")
        all_faces = json.loads(st.session_state["emotion_response"])
        if all_faces is not None:
            number_of_faces = all_faces.get("number_of_faces", 0)
            if number_of_faces > 0:
                faces = all_faces.get("faces")
                for i in range(number_of_faces):
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        st.text_input(label="Position_From_Left", key=f"position_from_left_{i}", value=faces[i].get("position_from_left", -1))
                    with col2:
                        st.text_area(label="Emotion", key=f"emotion_{i}", value=faces[i].get("emotion", None), height="content")
                    with col3:
                        st.text_area(label="Boundry", key=f"boundry_{i}", value=faces[i].get("bounding_box", None), height="content")
                    with col4:
                        st.text_area(label="Additional_Notes", key=f"notes_{i}", value=faces[i].get("additional_info", None), height="content")
            else:
                st.error("There are no faces in this image")
        else:
            st.error("There are no faces in this image")

# Streamlit async entrypoint
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())