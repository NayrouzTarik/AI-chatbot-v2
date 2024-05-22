import streamlit as st

st.set_page_config(
    page_title="EU AI GUARDIAN",
    page_icon=":robot_face:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    .main-title {
        font-size: 50px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 0;
    }
    .subtitle {
        font-size: 30px;
        text-align: center;
        color: #8b8b8b;
        margin-top: 0;
    }
    .center-text {
        text-align: center;
    }
    .query-input {
        width: 60%;
        margin: 0 auto;
        display: block;
    }
    .buttons-container {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 10px;
        margin-top: 20px;
    }
    .button {
        background-color: #333;
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<h1 class="main-title">EU AI GUARDIAN</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="subtitle">EU AI Act Compliant Chatbot</h2>', unsafe_allow_html=True)

st.markdown('<div class="center-text">Dive into EU AI Act Knowledge. What’s your inquisition?</div>', unsafe_allow_html=True)

query = st.text_input('', key='query', placeholder='Type your question here...', label_visibility="collapsed")

if st.button("Send"):
    if query:
        response = f"Response to: {query}"
        st.markdown('<div class="center-text"><b>User:</b> ' + query + '</div>', unsafe_allow_html=True)
        st.markdown('<div class="center-text"><b>Bot:</b> ' + response + '</div>', unsafe_allow_html=True)
    else:
        st.warning("Please enter a query.")

st.markdown("<div class='button-row'>", unsafe_allow_html=True)
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("What is the EU AI Act?"):
        st.write("The EU AI Act is a proposed regulation by the European Commission to regulate artificial intelligence.")

with col2:
    if st.button("What organizations will the EU AI Act apply to?"):
        st.write("The EU AI Act will apply to providers and users of AI systems within the EU, as well as those outside the EU if the AI system affects people within the EU.")

with col3:
    if st.button("What are the EU AI Act's main objectives?"):
        st.write("The main objectives of the EU AI Act are to ensure the safety and fundamental rights of people and businesses, and to strengthen AI uptake, investment, and innovation across the EU.")

with col4:
    if st.button("What are the EU AI Act's 4 Risk Levels?"):
        st.write("The EU AI Act categorizes AI systems into four risk levels: Unacceptable Risk, High Risk, Limited Risk, and Minimal Risk.")

with col5:
    if st.button("What are the sanctions for non-compliance with the EU AI Law?"):
        st.write("Sanctions for non-compliance can include fines up to €20 million or 4% of the total worldwide annual turnover, whichever is higher.")

st.markdown("</div>", unsafe_allow_html=True)
