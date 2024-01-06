import os
import google.generativeai as genai
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_solution(question, language, code_style):


    model = genai.GenerativeModel("gemini-pro")


    template="""
        Write a computer program code in {language} programming language to solve the question given below.
        Also provide {code_style} explaination of the code generated.
        if the answer is not correct just say, "answer is not available in the context", don't provide the wrong answer\n\n
        
        Question: \n{question}\n

        Answer:
            """
    
    prompt=PromptTemplate(input_variables=["language","code_style",'question'],
                          template=template)
    

    response=model(prompt.format(language= language, code_style= code_style, question= question))

    return response.txt