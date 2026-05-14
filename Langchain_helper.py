import os 
from dotenv import load_dotenv
from langchain_groq import ChatGroq 
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough

# Load environment variables
load_dotenv()
groq_key = os.getenv("GROQ_API_KEY")

# Initialize the LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=groq_key # Fixed parameter name: api_key, not api
)

def generate_restaurent_name_and_items(cuisine):
    # 1. First Chain: Name Suggestion
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'], # Fixed parameter: input_variables
        template="I want to open a restaurant for {cuisine}, suggest only one name"
    )
    name_chain = prompt_template_name | llm

    # 2. Second Chain: Menu Suggestion
    prompt_template_menu = PromptTemplate(
        input_variables=['restaurent_name'],
        template="Suggest me menu for {restaurent_name}, suggest top 5 with comma separated"
    )
    food_menu_name = prompt_template_menu | llm

    # 3. Create the Full Chain
    # We use .assign so the final dictionary contains both the name and the menu
    full_chain = (
        {"restaurent_name": name_chain} 
        | RunnablePassthrough.assign(menu=food_menu_name)
    )

    # 4. Invoke and Return
    result = full_chain.invoke({"cuisine": cuisine})
    return result

if __name__ == "__main__":
    data = generate_restaurent_name_and_items("Italian")
    