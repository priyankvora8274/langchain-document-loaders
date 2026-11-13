from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv


load_dotenv()

text_loader = TextLoader("/Users/patel/MyDrive/Study/Langchain_Learning/Code/langchain-document-loaders/TextLoader/kubernetes_pod_troubleshooting_logs.txt")

log_file = text_loader.load()

# The Textloader load() will return the list of Document type objects
print(type(log_file))

# the length is one
print(len(log_file))

# we will need to get the first element of list, that will be langchain document type object
print(type(log_file[0]))

# any Langchain Document Type object, contains 2 fields page_content -> Actual content of the souce doc and metadata -> metadata about that source doc
# print(log_file[0].page_content)

model = ChatOpenAI(model='gpt-5.2')
prompt = PromptTemplate(
    template="Troubleshoot the issue based on the given log file {logs}. Answer the reason and solution in short",
    input_variables= ["logs"]
)
parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({"logs":log_file[0].page_content})

print(result)