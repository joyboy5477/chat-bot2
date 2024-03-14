# Bhagavad Gita Chatbot using-Llama2

Welcome to the Bhagavad Gita Chatbot project! This innovative chatbot aims to bring the timeless wisdom of the Bhagavad Gita closer to people through the power of Generative AI. By combining advanced AI technologies with an intuitive user interface, we offer an interactive platform where users can explore the teachings of the Bhagavad Gita in a conversational manner.

## Features

- **Interactive Dialogue**: Engage in conversations with the chatbot to explore the teachings of the Bhagavad Gita.
- **Verse Retrieval**: Access verses and interpretations directly related to your questions or topics of interest.
- **Contextual Insights**: Gain deeper understanding through contextually relevant insights and explanations.

## Built With

- **Llama-2** - For understanding and generating natural language responses.
- **Pinecone** - A vector database that enables efficient retrieval of relevant information.
- **Langchain** - Orchestrates the integration between the generative AI and the vector database.
- **Flask** - The web framework used for deploying the chatbot as a web application.

## Getting Started

# How to run?
### STEPS:

Clone the repository

```bash
Project repo: https://github.com/
```

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


