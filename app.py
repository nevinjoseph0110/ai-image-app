import streamlit as st
import openai
from langchain.chains import LLMChain
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate

openai.api_key = st.secrets["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"]

st.set_page_config(page_title="AI Image Generator", layout="centered")
st.title("🎨 AI Image Generator")
st.write("Type your idea and get an image created by AI!")

scene = st.text_input("Enter your scene idea:")

if scene:
    st.info("🧠 Improving your prompt...")
    
    template = PromptTemplate(
        input_variables=["image_desc"],
        template="Generate a detailed prompt to generate an image based on the following description: {image_desc}"
    )
    llm = OpenAI(temperature=0.8)
    chain = LLMChain(llm=llm, prompt=template)
    better_prompt = chain.run(scene)

    st.success("✅ Prompt created!")
    st.write(better_prompt)

    st.info("🎨 Generating image...")
    response = openai.images.generate(
        model="dall-e-3",
        prompt=better_prompt,
        n=1,
        size="1024x1024"
    )

    image_url = response.data[0].url
    st.image(image_url, caption="Your AI Image")
    st.markdown(f"[🔗 Open Full Image]({image_url})")
