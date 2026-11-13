from langchain_community.document_loaders import PyPDFLoader

pdf_loader = PyPDFLoader("/Users/patel/MyDrive/Study/Langchain_Learning/Code/langchain-document-loaders/PDFLoader/sample_fake_resume.pdf")

pdf = pdf_loader.load()

# The list returned by pdf loader will have length as same as number of pages in PDF.
print(len(pdf))

# Each Document object in list will have that particular page content and metadata like num of pages, current page,creator, creation date,etc.
print(pdf[0].page_content)
print(pdf[0].metadata)