import os
import google.generativeai as genai

# open the key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# close the kwy
genai.configure(api_key=GEMINI_API_KEY)

# إmodle ao
model = genai.GenerativeModel("gemini-pro")

def generate_article(topic: str) -> str:
    prompt = f"""Write a detailed, well-structured blog article about: {topic}. It should be informative, engaging, and formatted well.
    Use:
- A friendly introduction
- Exclusive content, high value content.
- Clear subheadings, Write the sources under the blog only.  
- Natural tone and smooth flow  
- Short paragraphs, Dig into the information and make it influential. 
- A personal or reflective conclusion, Write creatively, discuss and compare like make tables. 
Avoid robotic language, repetition, or markdown. Output plain text only. Around 700-800 words.
"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print("🤔Error no article with Gemini:", e)
        return "This is a default article content due to an error in generating the article."
