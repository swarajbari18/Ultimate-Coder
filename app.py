
import streamlit as st
from components import (
    get_solution
)



def main():

    st.set_page_config(page_title= "The Ultimate Coder",
                    page_icon= '🤖',
                    layout= 'centered',
                    )
    
    st.header("Welcome to the palace of Ultimate Coder 🤖")

    question= st.text_input("Just ask your question here and have your solution right away!")


    col1,col2= st.columns([5,5])

    with col1:
        language= st.selectbox('Favourite Coding Language to use',
                                ('Python', 'Java', 'C', 'C++', 'R', 'Ruby'),index=0)
    with col2:
        code_style= st.selectbox('Explaination level of generated code',
                                ('None', 'brief', 'detailed', 'funny'),index=0)
        
    submit=st.button("Generate")

    if submit:
        st.write(get_solution(language= language, code_style= code_style, question= question))



if __name__ == '__main__':
    main()