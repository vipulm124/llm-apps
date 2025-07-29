import streamlit as st
from selenium_handler import SeleniumHandler
from typing import List
import random
import datetime
from LLMProcessor import LLMProcessor
from llmhandlers import LLMPROVIDERS

def main():
    # Initialize LLMProcessor in session state if not exists
    if 'llmprocessor' not in st.session_state:
        st.session_state.llmprocessor = LLMProcessor(LLMPROVIDERS.OPENAI)
    
    llmprocessor = st.session_state.llmprocessor
    selenium_handler = SeleniumHandler()
    image_paths = ['screenshots/screenshot_1.png', 'screenshots/screenshot_2.png']

    if 'history' not in st.session_state:
        st.session_state.history = llmprocessor.conversation_history
    else:
        # Keep history in sync with the processor
        llmprocessor.conversation_history = st.session_state.history


    st.title("🛒 Smart Cart Analyzer")
    
    st.session_state.cart_url = st.text_input("Enter cart URL", placeholder="https://example.com/cart")
    col_left, col_right = st.columns(2)

    with col_left:
        if st.button("Get Cart Screenshots"):
            with st.spinner("Getting screenshots from url"):
                selenium_handler.open_new_tab_take_screenshots(st.session_state.cart_url)
                st.rerun()
    
    with col_right:
        if st.button("Process screenshots"):
            with st.spinner("Reading screenshots for data"):
                llmprocessor.read_screenshots(screenshot_paths=image_paths)
                print(f"llmprocessor.image_context: {llmprocessor.image_context}")


    with st.container(height=400):
        for hist in st.session_state.history:
            st.write(hist)
    
    col1, col2 = st.columns([12, 1], vertical_alignment="center")
    
    question = col1.text_area("Questions?")

    if col2.button("➤", type="primary"):
        with st.spinner("Talking to model....."):
            print(llmprocessor.image_context)
            llmprocessor.initiate_chat(question)
            st.session_state.history = llmprocessor.conversation_history
            st.rerun()



if __name__ == "__main__":
    st.set_page_config(page_title="Cart Analyzer", page_icon=":shopping_cart:")
    main()