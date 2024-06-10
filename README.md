# RAG Chatbot for PDF Interaction

Welcome to the RAG Chatbot project! This chatbot leverages Generative AI to provide an interactive platform for engaging with PDF documents. Users can upload PDFs and explore their content through conversational interactions, making complex information more accessible and understandable.

## Features

- **Interactive Dialogue**: Engage in dynamic conversations with the chatbot to delve into the content of uploaded PDFs.
- **Content Retrieval**: Quickly access specific information, quotes, or sections from PDFs based on your queries.
- **Contextual Insights**: Receive contextually relevant insights and explanations to enhance understanding of the document's content.

## Built With

- **LLaMA-2**: Powers the understanding and generation of natural language responses.
- **Pinecone**: A vector database that facilitates efficient retrieval of document-specific information.
- **LangChain**: Orchestrates the integration between generative AI and the vector database for seamless interaction.
- **Flask**: Used for deploying the chatbot as a web application.

## Getting Started

### How to Run?

#### Clone the Repository

```bash
git clone https://github.com/your-repository-url
cd your-repository-directory

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n chat python=3.12.2 -y
```

```bash
conda activate chat
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


### Create a `.env` file in the root directory and add your Pinecone credentials as follows:

```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
PINECONE_API_ENV = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```


### Download the quantize model from the link provided in model folder & keep the model in the model directory:

```ini
## Download the Llama 2 Model:

llama-2-7b-chat.ggmlv3.q4_0.bin


## From the following link:
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
```

```bash
# run the following command
python store_index.py
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up localhost:
```

### Techstack Used:

- Python
- LangChain
- Flask
- Meta Llama2
- Pinecone


