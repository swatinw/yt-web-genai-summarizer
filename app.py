import validators
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_core.documents import Document
from youtube_transcript_api import YouTubeTranscriptApi
from langchain_community.document_loaders import UnstructuredURLLoader, WebBaseLoader

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
prompt_template = "Provide a summary of the following content in 300 words:\nContent: {text}"
prompt = PromptTemplate(template=prompt_template, input_variables=["text"])

# Function to fetch YouTube transcript
def get_youtube_transcript(video_url):
    try:
        video_id = video_url.split("v=")[-1]
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        full_text = " ".join([t['text'] for t in transcript_list])
        return full_text
    except Exception as e:
        st.error("❌ Could not fetch transcript. Video may not have captions or is restricted.")
        st.stop()

# Summarize button logic
if st.button("Summarize the Content From YT or Website"):
    if not groq_api_key.strip() or not generic_url.strip():
        st.error("❌ Please provide both the API key and the URL.")
    elif not validators.url(generic_url):
        st.error("❌ Please enter a valid URL (must start with http or https).")
    else:
        try:
            with st.spinner("⏳ Extracting and summarizing content..."):
                if "youtube.com" in generic_url:
                    text = get_youtube_transcript(generic_url)
                    docs = [Document(page_content=text)]
                else:
                    try:
                        loader = UnstructuredURLLoader(
                            urls=[generic_url],
                            ssl_verify=False,
                            headers={
                                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.3 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
                            }
                        )
                        docs = loader.load()
                        if not docs or not docs[0].page_content.strip():
                            raise ValueError("Unstructured loader returned empty content.")
                    except Exception:
                        loader = WebBaseLoader(generic_url)
                        docs = loader.load()

                if not docs or not docs[0].page_content.strip():
                    st.warning("⚠️ No content found at the provided URL. Try another one.")
                    st.stop()

                llm = ChatGroq(model="llama3-8b-8192", groq_api_key=groq_api_key)
                chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
                output_summary = chain.run(docs)

                st.success("✅ Summary Generated:")
                st.write(output_summary)

        except Exception as e:
            st.exception(e)
