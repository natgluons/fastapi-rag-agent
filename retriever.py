import os
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class Retriever:
    def __init__(self, data_dir="data", embedding_model_name="all-MiniLM-L6-v2"):
        self.data_dir = data_dir
        self.model = SentenceTransformer(embedding_model_name)
        self.docs = []
        self.doc_ids = []
        self.embeddings = None
        self.index = None
        self._load_and_embed_docs()

    def _load_and_embed_docs(self):
        files = sorted(os.listdir(self.data_dir))
        texts = []
        for i, f in enumerate(files):
            path = os.path.join(self.data_dir, f)
            with open(path, 'r', encoding='utf-8') as file:
                text = file.read()
                self.docs.append(text)
                self.doc_ids.append(f)
                texts.append(text)

        self.embeddings = self.model.encode(texts, convert_to_numpy=True)
        dim = self.embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(self.embeddings)

    def retrieve(self, query, top_k=3):
        query_emb = self.model.encode([query], convert_to_numpy=True)
        distances, indices = self.index.search(query_emb, top_k)
        results = []
        for idx in indices[0]:
            results.append((self.doc_ids[idx], self.docs[idx]))
        return results
