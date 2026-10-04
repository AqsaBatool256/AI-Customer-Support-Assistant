import requests
import streamlit as st


API_URL = "http://127.0.0.1:8000/support/ask"


st.set_page_config(
    page_title="NovaTech Customer Support",
    page_icon="🤖",
    layout="centered",
)


st.title("🤖 NovaTech Customer Support")
st.caption("AI-powered support assistant for NovaTech products and policies.")

st.divider()

question = st.text_input(
    "How can we help you?",
    placeholder="Ask about pricing, refunds, cancellations, or products...",
)

st.caption("Try an example:")
st.write("💰 Pricing  •  💳 Refunds  •  ❌ Cancellation  •  🔐 Data Security")

if st.button("Ask Support", type="primary"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Searching the knowledge base..."):
            try:
                response = requests.get(
                    API_URL,
                    params={"question": question},
                    timeout=120,
                )

                response.raise_for_status()
                data = response.json()

                st.subheader("💬 Answer")
                st.write(data["answer"])

                if data["sources"]:
                    st.subheader("📚 Sources")

                    for source in data["sources"]:
                        st.info(source)

            except requests.exceptions.RequestException as error:
                st.error(f"Unable to connect to the support service: {error}")

st.divider()

st.caption("NovaTech Customer Support Assistant • Powered by RAG + Local AI")
