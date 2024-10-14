import pandas as pd
import chromadb
import uuid

class Portfolio:
    def __init__(self, file_path="app/resources/myportfolio.csv"):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        self.chroma_client = chromadb.PersistentClient('vectorstore')
        self.collection = self.chroma_client.get_or_create_collection(name="portolio")


    def load_portfolio(self):
        if not collection.count():
            for _, row in df.iterrows():
                collection.add(documents=row["Techstack"],
                       metadatas={"links": row["Links"]},
                       ids=[str(uuid.uuid4())])


    def query_links(self, skills):
        return self.collection.query(query_texts=skills, n_results=2).get("metadatas", [])