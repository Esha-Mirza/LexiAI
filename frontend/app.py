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

    st.header("📚 Analysis History")
    if st.button("🔄 Refresh History"):
        st.session_state["show_history"] = True

    if st.session_state.get("show_history"):
        try:
            history = requests.get("http://localhost:8000/history/", timeout=10).json()
            if not history:
                st.caption("No past analyses yet.")
            else:
                for item in history[:10]:  # show last 10
                    label = item["timestamp"]
                    with st.expander(f"🕒 {label}"):
                        preview = item["input_text"][:150]
                        st.caption(f"Input: {preview}...")
                        result = item.get("result", {})
                        st.write(f"**Summary:** {result.get('summary', result.get('result', 'N/A'))}")
                        if st.button("↩️ Load this document", key=f"load_{item['id']}"):
                            st.session_state["sample_text"] = item["input_text"]
                            st.rerun()
                        if st.button("🗑️ Delete", key=f"del_{item['id']}"):
                            requests.delete(f"http://localhost:8000/history/{item['id']}", timeout=10)
                            st.rerun()

                if st.button("🗑️ Clear All History"):
                    requests.delete("http://localhost:8000/history/", timeout=10)
                    st.rerun()
        except Exception as e:
            st.error(f"Could not load history: {e}")

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
                    timeout=120
                )

                if response.status_code == 200:
                    data = response.json()

                    st.subheader("📄 Summary")
                    st.info(data.get("summary", data.get("result", "N/A")))

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