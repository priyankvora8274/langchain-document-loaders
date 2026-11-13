from langchain_community.document_loaders import CSVLoader

loader = CSVLoader("/Users/patel/MyDrive/Study/Langchain_Learning/Code/langchain-document-loaders/csv_loader/sample_ecommerce_orders.csv")

data = loader.load()

# CSV Loader will convert each row of the CSV file into one document, and return the list of that documents.
# So the length of returned Document type object list woulg be same as number of rows
print(len(data))

print(data[2])