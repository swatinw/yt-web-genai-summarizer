
import validators
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader, WebBaseLoader

# Streamlit app setup
st.set_page_config(page_title="LangChain: Summarize Text From YT or Website", page_icon="🦜")
st.title("🦜 LangChain: Summarize Text From YT or Website")
st.subheader("Summarize URL")

# Sidebar: API key input
groq_api_key = st.secrets.get("groq_api_key", "")

with st.sidebar:
    if not groq_api_key:
        groq_api_key = st.text_input("Groq API Key", value="", type="password")

# Input: URL
generic_url = st.text_input("Enter a YouTube or Website URL")

# Prompt template
prompt_template = """
Provide a summary of the following content in 300 words:
Content: {text}
"""
prompt = PromptTemplate(template=prompt_template, input_variables=["text"])

# Summarize button logic
if st.button("Summarize the Content From YT or Website"):
    if not groq_api_key.strip() or not generic_url.strip():
        st.error("❌ Please provide both the API key and the URL.")
    elif not validators.url(generic_url):
        st.error("❌ Please enter a valid URL.")
    else:
        try:
            with st.spinner("⏳ Extracting and summarizing content..."):
                docs = []
                if "youtube.com" in generic_url:
                    try:
                        loader = YoutubeLoader.from_youtube_url(generic_url, add_video_info=True)
                        docs = loader.load()
                        if not docs or not docs[0].page_content.strip():
                            raise ValueError("Transcript not found.")
                    except Exception:
                        st.warning("⚠️ Could not load from YouTube. Trying as a generic website...")
                        loader = WebBaseLoader(generic_url)
                        docs = loader.load()
                else:
                    try:
                        loader = UnstructuredURLLoader(
                            urls=[generic_url],
                            ssl_verify=False,
                            headers={
                                "User-Agent": "Mozilla/5.0"
                            }
                        )
                        docs = loader.load()
                        if not docs or not docs[0].page_content.strip():
                            raise ValueError("No content found.")
                    except Exception:
                        loader = WebBaseLoader(generic_url)
                        docs = loader.load()

                if not docs or not docs[0].page_content.strip():
                    st.warning("⚠️ No content found at the provided URL. Try another one.")
                    st.stop()

                # Initialize LLM
                llm = ChatGroq(model="llama3-8b-8192", groq_api_key=groq_api_key)

                # Summarization chain
                chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
                output_summary = chain.run(docs)

                st.success("✅ Summary Generated:")
                st.write(output_summary)

        except Exception as e:
            st.exception(e)
