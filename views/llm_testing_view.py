import streamlit as st
from utils.alert import show_alert
from _config import settings
from text_processing import prompt_lib, prompt_builder

from utils.api_request import prompt_llm

if st.session_state.alert:
    show_alert()

st.title("Prompt Builder")

selected_model = st.selectbox("Select a model", options=list(settings.MODELS.keys()))

template_options = list(prompt_lib.user_prompt_templates.keys())
selected_template = st.selectbox("Select a prompt template", options=template_options)

if selected_template:
    template_info = prompt_lib.user_prompt_templates[selected_template]
    
    st.subheader("Fill out the context")
    context = {}
    for var in template_info['context']:
        context[var] = st.text_input(f"{var.capitalize()}")

    if st.button("Generate response"):
        
        try:
            # Render prompt with context
            rendered_prompt = prompt_builder.render_prompt(template_info['file_name'], context)
            
            st.subheader("Prompt")
            st.write(rendered_prompt)
            
           # Get response from LLM
            messages = [
                {"role": "user", "content": rendered_prompt},
            ]
            response = prompt_llm(settings.MODELS[selected_model], messages)
            
            st.subheader("Response")
            st.write(response)
            
        except Exception as e:
            st.error(f"{str(e)}")
            