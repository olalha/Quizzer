def show_alert(st):
    """
    Display a Streamlit alert from session state and clear it.

    Args:
        st (streamlit): The Streamlit module.
    """
    # Display alert if present in session state
    if st.session_state.alert:
        alert_type = st.session_state.alert['type']
        message = st.session_state.alert['message']
        getattr(st, alert_type)(message)
    
    # Clear the alert
    st.session_state.alert = None
