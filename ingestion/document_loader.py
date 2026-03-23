import os
import fitz
import pandas as pd
from langchain_core.documents import Document


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "asthma_docs")


def load_documents():
    """
    Load PDF and CSV files from the asthma knowledge base
    and convert them into LangChain Document objects.
    """

    documents = []

    print("Reading files from:", DATA_PATH)

    if not os.path.exists(DATA_PATH):
        print("ERROR: data folder not found")
        return documents

    files = os.listdir(DATA_PATH)

    print("Files found:", files)

    for file in files:

        file_path = os.path.join(DATA_PATH, file)

        # -------- Load PDFs --------
        if file.lower().endswith(".pdf"):

            try:
                pdf = fitz.open(file_path)

                for page_num, page in enumerate(pdf):

                    text = page.get_text()

                    if text.strip():

                        documents.append(
                            Document(
                                page_content=text,
                                metadata={
                                    "source": file,
                                    "page": page_num
                                }
                            )
                        )

            except Exception as e:
                print("Error reading PDF:", file, e)

        # -------- Load CSV --------
        elif file.lower().endswith(".csv"):

            try:
                df = pd.read_csv(file_path)

                # Optional: create a dataset summary for statistics queries
                summary_text = f"""
Asthma dataset statistics:
Total records: {len(df)}
Columns: {', '.join(df.columns)}
"""

                documents.append(
                    Document(
                        page_content=summary_text.strip(),
                        metadata={"source": file, "type": "dataset_summary"}
                    )
                )

                for index, row in df.iterrows():

                    # Convert each row into readable text using column names
                    row_text_parts = []

                    for col in df.columns:
                        value = row[col]
                        row_text_parts.append(f"{col} is {value}")

                    text = " | ".join(row_text_parts)

                    documents.append(
                        Document(
                            page_content=text,
                            metadata={
                                "source": file,
                                "row": index
                            }
                        )
                    )

            except Exception as e:
                print("Error reading CSV:", file, e)

    print(f"\nLoaded {len(documents)} document sections")

    return documents