from langchain_community.vectorstores import Chroma

from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_text_splitters import CharacterTextSplitter

def create_vector_db():


    with open(
        "data/products.txt",
        "r"
    ) as f:


        text=f.read()



    splitter=CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )


    docs=splitter.create_documents(
        [text]
    )


    embeddings=HuggingFaceEmbeddings(
        model_name=
        "sentence-transformers/all-MiniLM-L6-v2"
    )


    db=Chroma.from_documents(
        docs,
        embeddings,
        persist_directory="vector_db"
    )


    return db



def search_products(question):


    embeddings=HuggingFaceEmbeddings(
        model_name=
        "sentence-transformers/all-MiniLM-L6-v2"
    )


    db=Chroma(
        persist_directory="vector_db",
        embedding_function=embeddings
    )


    result=db.similarity_search(
        question,
        k=2
    )


    return result