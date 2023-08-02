import os
from google.cloud import bigquery
from sqlalchemy import *
from sqlalchemy.engine import create_engine
from sqlalchemy.schema import *

from langchain.agents import create_sql_agent
from langchain.llms.openai import OpenAI
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import AgentExecutor, Tool, load_tools
import pandas as pd



import streamlit as st

service_account_file = "/Users/jayesh.patil/Workspace/hands-on/gen-ai/demos/bq_chat/dce-gcp-training-4f93809bda0c.json" # Change to where your service account key file is located
project = "dce-gcp-training"
dataset = "fhir_data_jvp"
table = "patient_flat"
sqlalchemy_url = f'bigquery://{project}/{dataset}?credentials_path={service_account_file}'

os.environ["OPENAI_API_KEY"] = "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"

db = SQLDatabase.from_uri(sqlalchemy_url)
llm = OpenAI(temperature=0, model="text-davinci-003")
toolkit = SQLDatabaseToolkit(db=db, llm=llm)
agent_executor = create_sql_agent(
llm=llm,
toolkit=toolkit,
verbose=True,
top_k=1000,
)

with st.echo():
    response = agent_executor.run("list all the patients in tabular format?")
    st.write(response)
with st.echo():
    response = agent_executor.run("How many male patients?")
    st.write(response)
with st.echo():
    response = agent_executor.run("List the details of all the male patients")
    st.write(response)
with st.echo():
    response = agent_executor.run("give me the sql to list the details of all the male patients")
    st.write(response)


