# LangChain LLM Tutorial

Welcome to the LangChain LLM tutorial! This guide is designed to help you learn LangChain step by step, at a slow and deliberate pace. Rushing often leads to mistakes, and we want to ensure you have a solid understanding at every stage.

# About This Tutorial
LangChain is a powerful framework for building applications using large language models (LLMs). However, due to its complexity, it’s easy to become overwhelmed if you try to move too quickly. This tutorial is intentionally structured to:

- Emphasize gradual learning.
- Break down complex topics into manageable steps.
- Provide clear examples and exercises.

By the end of this tutorial, you’ll have the confidence and knowledge to create robust LangChain-based applications.

---

# Structure of the Tutorial

1. Talk to the LLM<br>
[01.llm_template.ipynb](01.llm_template.ipynb): Ask simple questions to a LLM

2. Vectors and embedding<br>
[02.embeddings_vectors.ipynb](02.embeddings_vectors.ipynb): How to use Embedding we can use for RAG's

3. Classification<br>
[03.classify.ipynb](03.classify.ipynb): Classify a message using pydantic object and ChatPromptTemplate

4. Extraction<br>
[04.extraction.ipynb](04.extraction.ipynb): Same but for structured data extraction

---

# Install 

To be independant and be able to practice anywhere, I'm using two Docker containers:
1) One for [**Ollama**](https://ollama.com/search)with a couple of models
2) **A development container** with Python 3.12 and the libraries I need
4) Using VSCode you [**"Attach Visual Studio Code"**](https://code.visualstudio.com/docs/devcontainers/containers) with Jupyter plugins 

... and you're the king of the world

- We'll use Ollama to avoid expenses associated with LLM like GPT. No need API keys nor Credit Card. 
- Results may be a bit less accurate than GPT but we wanna learn first.
- The version of LangChain installed should be 0.3+ (important)
- Ollama [is easy to install using Docker](https://github.com/ollama/ollama/blob/main/docs/docker.md). 
(Better to have a GPU, even a small one)
- I give an example of Dockerfile and docker-compose.yaml using Python 3.12
- You can then use an evironment variable OLLAMA_SERVER (ex. OLLAMA_SERVER='http://ollama:11434') from this container [running Jupyter](https://jupyterlab.readthedocs.io/en/4.1.x/getting_started/installation.html)
- Required Python packages from `requirements.txt` file should be build with the Dockerfile.

A simple `docker-compose up -d` should do the trick

# Run the Notebooks
This tutorial includes a series of Jupyter Notebooks you can run 


---

## Tips for Success
- **Take Your Time**: Resist the urge to skip steps or rush through sections.
- **Experiment**: Modify the examples and test your ideas.
- **Ask Questions**: Engage with the LangChain community if you encounter issues.

---

## Contribution
This is a community-driven effort, and your feedback is valuable. If you find errors or have suggestions for improvement, please submit an issue or pull request.

Happy Learning!