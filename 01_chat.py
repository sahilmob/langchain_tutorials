from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, SystemMessage


load_dotenv()

system_template = "Translate the following into {language}:"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)


model = ChatOpenAI(model="gpt-4")


parser = StrOutputParser()

chain = prompt_template | model | parser


print(chain.invoke({"language": "italian", "text": "hi"}))
