# create first agent that is search agent
from langchain.agents import create_agent   ## before we used create_react_agent but here we are using different
# because  of old version of langchain that why we used create_react_agent (reasoning and action) and in version they
# replace same with create_agent
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser  # LCEL : langchain expression language
from src.tools.tools import search_web, scrape_url
from dotenv import load_dotenv

# thought, action and observation ----> ReAct to use react characterisctics we use agent_executor
# when we were using create_react_agent but in create_agent we dont use executor

load_dotenv()

# setup the model or model initialization
# llm=ChatOpenAI(
#         model="gpt-4o-mini",
#         temperature =0
# )

llm=ChatGroq(
        model="openai/gpt-oss-120b",
        temperature =0
)

# create agent function ----> 1st agent

def build_search_agent():
        return create_agent(
                model = llm,
                tools =[search_web],
                # here manual prompting is not required as it is returning the url only
        )


# create agent function ----> 2nd agent
def build_reader_agent():
        return create_agent(
                model = llm,
                tools =[scrape_url],
                # here manual prompting is not required as it is returning the url only
        )

# writer chain  topic ---> getting from user and research ---> getting from 2nd agent

writer_prompt = ChatPromptTemplate.from_messages([
        ("system", "Yor are expert research wirter. Write clear, structured and insightful reports"),
        ("human", """ Write a detailed research report on the topic below

         Topic :{topic}

         Research Gathered : {research}

         Structure the report as :
         - Introduction
         - Key Finding (minimum 3 well-explained points)
         - Conclucion
         - Source (list all URLs found in th research)

         Be detailed, factual and professional. """),
])

writer_chain = writer_prompt | llm | StrOutputParser()  # this is LCEL

# critic chain

critic_prompt = ChatPromptTemplate.from_messages([
        ("system", "You ara sharp and constructive research critics. Be honest and specific."),
        ("human", """Review the research report below and evaluate it strictly.

         Report :{report}

         Respond in this exact format :

         Score: X/10

         Strengths:
         - ...
         - ...

         Areas to Improv :
         - ...
         - ...

         One line verdict:
         ...
"""),
])

critic_chain = critic_prompt | llm | StrOutputParser()
