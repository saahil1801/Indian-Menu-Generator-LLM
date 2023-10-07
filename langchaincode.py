from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from secret import openapi_key

import os       
os.environ['OPENAI_API_KEY'] = openapi_key

llm = OpenAI(temperature=0.7)

def generate_restaurant_name_and_items(indianfood):
    llm = OpenAI(temperature=0.7)
    prompt_template_name=PromptTemplate(
    input_variables =['indianfood'],
    template = "I want to open a  for {indianfood} food. Suggest a fancy name for this."
    )
    name_chain =LLMChain(llm=llm, prompt=prompt_template_name,output_key="restaurant_name")
    llm = OpenAI(temperature=0.7)
    prompt_template_items = PromptTemplate(
    input_variables = ['restaurant_name'],
    template="Suggest some menu items for {restaurant_name}."
    )

    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items,output_key="menu_items")
    chain = SequentialChain(
    chains = [name_chain, food_items_chain],
    input_variables = ['indianfood'],
    output_variables = ['restaurant_name', "menu_items"]
    )
    response = chain({'indianfood': indianfood})

    return response

if __name__ == "__main__":
    print(generate_restaurant_name_and_items("Samosa"))