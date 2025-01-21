# LangChain LLM Tutorial

Welcome to the LangChain LLM tutorial! This guide is designed to help you learn LangChain step by step, at a slow and deliberate pace. Rushing often leads to mistakes, and we want to ensure you have a solid understanding at every stage.

## About This Tutorial
LangChain is a powerful framework for building applications using large language models (LLMs). However, due to its complexity, it’s easy to become overwhelmed if you try to move too quickly. This tutorial is intentionally structured to:

- Emphasize gradual learning.
- Break down complex topics into manageable steps.
- Provide clear examples and exercises.

By the end of this tutorial, you’ll have the confidence and knowledge to create robust LangChain-based applications.

---

## Structure of the Tutorial

1. **Introduction to LLMs**
   - Understand the basics of large language models.
   - Learn how LangChain leverages LLMs for application development.

2. **Building Blocks of LangChain**
   - Learn about key concepts such as chains, prompts, and agents.

3. **Implementing Your First LangChain Application**
   - Step-by-step guidance to set up your environment and run your first LangChain program.

4. **Advanced Topics**
   - Dive into embeddings, vector stores, and classification.
   - Experiment with extraction and more complex workflows.

5. **Deployment and Scaling**
   - Learn how to deploy your LangChain applications using Docker and Docker Compose.

---

## Prerequisites
To follow this tutorial, ensure you have the following installed:

- Python 3.8 or later
- Docker and Docker Compose
- A GPU-enabled machine for optimal performance

Additionally, install the required Python packages:

```
asyncio
fastapi
groq
gunicorn
haystack-ai
ollama-haystack
langchain
langchain-groq
langchain-ollama
langchain-openai
langchain-community
langchain-qdrant
pypdf
```

These dependencies are also listed in the `requirements.txt` file.

---

## Getting Started

### Step 1: Set Up the Environment
1. Clone this repository.
2. Build the Docker containers using the provided `docker-compose.yaml` file:

   ```bash
   docker-compose up -d
   ```

3. Confirm that the services are running:
   - LangChain: Accessible on port 8888
   - Qdrant: Accessible on port 6333

### Step 2: Run the Notebooks
This tutorial includes a series of Jupyter Notebooks to guide you through the concepts:

- `01.llm_template.ipynb`: Start with LangChain templates.
- `02.embeddings_vectors.ipynb`: Explore embeddings and vectorization.
- `03.classify.ipynb`: Learn how to classify text.
- `04.extraction.ipynb`: Understand data extraction techniques.

Run these notebooks in sequence to follow the structured learning path.

---

## Tips for Success
- **Take Your Time**: Resist the urge to skip steps or rush through sections.
- **Experiment**: Modify the examples and test your ideas.
- **Ask Questions**: Engage with the LangChain community if you encounter issues.

---

## Contribution
This is a community-driven effort, and your feedback is valuable. If you find errors or have suggestions for improvement, please submit an issue or pull request.

Happy Learning!