import streamlit as st

from app.services.rag_service import generate_response


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
                response = generate_response(question)

                st.subheader("💬 Answer")
                st.write(response["answer"])

                if response["sources"]:
                    st.subheader("📚 Sources")

                    for source in response["sources"]:
                        st.info(source)

            except Exception as error:
                st.error(f"Unable to generate a response: {error}")

st.divider()

st.caption("NovaTech Customer Support Assistant • Powered by RAG + Gemini")
