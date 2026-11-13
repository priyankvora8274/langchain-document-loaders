from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

# glob : we can define what files we want to load from directory. we can define patterns, so file that follow pattern will load.
#loader_cls: based on what type of file we are loading, we need to choose class

#Dire
loader = DirectoryLoader(
    "/Users/patel/MyDrive/Study/Langchain_Learning/Code/langchain-document-loaders/Directory_Loader/ML_Courses",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

pdf_docs = loader.load() # OR lazy_load()

for doc in pdf_docs:
    print(doc.metadata)

# print(len(pdf_docs))
# print(pdf_docs[523].page_content)
# print(pdf_docs[523].metadata)