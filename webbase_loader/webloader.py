from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

url = "https://www.amazon.com/Meta-Quest-512GB-Virtual-Reality/dp/B0CD1JTBSC/ref=sr_1_3?adgrpid=1340307272258905&dib=eyJ2IjoiMSJ9.CGm71Wko96ZDTz4KEsP_rsdMQr6ELsxHmXpaj2DJcZrnV8n5B7JiWBo80rvpoEZcO981egnOUODlTyQq_n6nzemUiB68aOt0mCpX-ZbGxuYFLIFr5Oc6foB_-8MeQDOIJWa95D-J5KVUSfz9X9VYNeQ7YAm9GKEBgZVdaMWalhhMnhhnVUcn4Vb8XnCdtBcdS72s3gyHyVhIwV8CrlJUi2ebdeMgr-XnpPfi1ZeqlLE.8T49c6bIKlGixH8RDLulLSULCPbARZFGxCI-jNyIs3E&dib_tag=se&gb=2&hvadid=83769497895713&hvbmt=be&hvdev=c&hvexpln=0&hvlocphy=162683&hvnetw=o&hvocijid=8996551055860409982--&hvqmt=e&hvtargid=kwd-83770493594825%3Aloc-190&hydadcr=18886_13351312_9005&keywords=apple%2Bvision%2Bpro&mcid=ebb9e18c5cd83102b44b8a22aaf0e2b2&qid=1794594608&sr=8-3&th=1"
loader = WebBaseLoader(url)
doc = loader.load()

# print(len(doc))
# print(doc[0].page_content)


model = ChatOpenAI(model='gpt-5.2')
prompt = PromptTemplate(
    template="Give the answer for the following question {question} based on the text {text}",
    input_variables= ["question","text"]
)
parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({"question": "What is this product and what is the price?", "text":doc[0].page_content})
print(result)