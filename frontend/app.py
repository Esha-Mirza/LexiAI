import streamlit as st
import requests

st.set_page_config(
    page_title="Legal Document Analyzer",
    page_icon="⚖️",
    layout="wide"
)

st.title("⚖️ Legal Document Analyzer")
st.markdown("*AI-powered legal document analysis*")

with st.sidebar:
    st.header("ℹ️ About")
    st.write("""
    **What it extracts:**
    - 📄 Summary
    - 📌 Key Clauses (Termination, Liability, Jurisdiction)
    - 🔍 Parties, Dates, Locations
    """)
    
    st.header("📄 Sample Document")
    if st.button("📋 Load Sample"):
        st.session_state["sample_text"] = """This Agreement is entered into by Party A and Party B. Either party may terminate with 30 days notice. Liability is limited to direct damages. Governed by California law."""

text = st.text_area(
    "📄 Paste legal document here:",
    height=200,
    value=st.session_state.get("sample_text", "")
)

if st.button("🔍 Analyze", type="primary"):
    if text:
        with st.spinner("🧠 Analyzing..."):
            try:
                response = requests.post(
                    "http://localhost:8000/analyze/",
                    data={"text": text},
                    timeout=60
                )
                
                if response.status_code == 200:
                    data = response.json()
                    
                    st.subheader("📄 Summary")
                    st.info(data.get("summary", "N/A"))
                    
                    st.subheader("📌 Key Clauses")
                    st.info(data.get("clauses", "N/A"))
                    
                    st.subheader("🔍 Entities")
                    st.info(data.get("entities", "N/A"))
                else:
                    st.error(f"Error: {response.status_code}")
                    
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.warning("⚠️ Please paste a legal document")