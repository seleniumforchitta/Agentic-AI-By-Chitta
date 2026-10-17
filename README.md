# Agentic AI by Chitta 🤖

A hands-on journey into Agentic AI using Python, local Large Language Models (LLMs), and modern development tools. This project explores how to build AI-powered applications that interact with language models programmatically — starting with a simple command-line AI assistant.

The goal is to learn the fundamentals of AI application development while keeping experimentation local and avoiding paid API usage.

## 🚀 Project Overview

The current application is a command-line AI assistant that:

- Accepts questions directly from the terminal.
- Sends prompts to a locally running LLM using Ollama.
- Displays AI-generated responses.
- Measures response execution time.
- Supports interactive conversations until the user chooses to exit.
- Uses Python and `uv` for dependency and project management.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| uv | Python package and project management |
| Ollama | Running LLMs locally |
| Qwen 3.5 | Local language model |
| OpenAI Python SDK | Communicating with Ollama's OpenAI-compatible API |
| Requests | Alternative direct communication with Ollama's native API |
| Git & GitHub | Version control and project sharing |

## 🏗️ Architecture

```text
User
  |
  v
Terminal / Command Line
  |
  v
Python Application (main.py)
  |
  v
Ollama Local API
  |
  v
Qwen 3.5 Model
  |
  v
Generated Response
  |
  v
Terminal Output
```

The model runs locally through Ollama. Prompts and responses are processed by the local application rather than requiring an OpenAI-hosted model API.

## 📋 Prerequisites

Before running the project, make sure you have:

- Python installed.
- `uv` installed.
- Ollama installed and running.
- A supported local language model downloaded.
- Git installed (optional, for version control).

The project is currently being developed on macOS using an Apple Silicon MacBook Air.

## ⚙️ Setup and Installation

### 1. Install uv

If `uv` is not already installed:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Refresh your shell environment if required:

```bash
source "$HOME/.local/bin/env"
```

Verify the installation:

```bash
uv --version
```

### 2. Install Ollama

Download and install Ollama from:

https://ollama.com/download

Open the Ollama application and verify that its local API is available:

```bash
curl http://localhost:11434/api/tags
```

### 3. Download a local language model

The project has experimented with these Qwen 3.5 models:

```bash
ollama pull qwen3.5:0.8b
```

A larger model can also be used:

```bash
ollama pull qwen3.5:4b
```

The smaller model may respond faster but can produce lower-quality answers. The larger model may provide better responses at the cost of additional processing time and memory.

To check downloaded models:

```bash
ollama list
```

### 4. Set up the project

Navigate to the project directory:

```bash
cd Agentic-AI-By-Chitta
```

If the project already has a `pyproject.toml` file, install its dependencies:

```bash
uv sync
```

If you are starting from scratch, initialize the project and add the required dependency:

```bash
uv init
uv add openai
```

If your current implementation uses the `requests` library instead, install it with:

```bash
uv add requests
```

Use the dependency that matches the implementation in `main.py`.

## ▶️ Run the Application

Start the application with:

```bash
uv run main.py
```

Enter a question when prompted:

```text
Ask your question: Is Cuttack a district?

AI Response: Yes, Cuttack is a district in Odisha, India.

Execution time: <measured time in seconds>
```

The response above is an illustrative example; the actual output depends on the model.

To stop the application, enter:

```text
exit
```

You can also use `quit` or `q` if supported by the current implementation.

## 🔌 How It Works

The application follows a simple request-response workflow:

1. Read the user's question from the terminal.
2. Send the prompt to the locally running Ollama model.
3. Wait for the model to generate a response.
4. Print the response to the terminal.
5. Measure and display the execution time.
6. Continue accepting questions until the user exits.

Ollama also provides an OpenAI-compatible API, allowing applications to use the OpenAI Python SDK with a local endpoint.

Example connection pattern:

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)
```

Here, `ollama` is a placeholder credential used by the local endpoint; it is not a paid OpenAI API key.

## ⚡ Performance and Troubleshooting

### Ollama is not responding

Check whether the local API is available:

```bash
curl http://localhost:11434/api/tags
```

Open the Ollama application if the service is not running.

### Responses are slow

Check which model is loaded:

```bash
ollama ps
```

For faster experimentation, try a smaller model. For better response quality, try a larger model that fits your system.

### The model returns an empty response

Some thinking-capable models may spend their output-token budget on internal reasoning without returning visible text in the response's `content` field.

When using Ollama's native chat API, test whether the selected model supports disabling thinking with `"think": false`. You can also inspect the returned JSON, including `message.content`, `message.thinking`, and `done_reason`, to understand what happened.

### Dependency errors

Synchronize the project dependencies:

```bash
uv sync
```

If a required package is missing, add it using `uv add <package-name>`.

## 💰 Cost

The current local-model workflow is designed to avoid per-request OpenAI API charges.

- Ollama: Runs supported models locally.
- Qwen: Uses the downloaded model on your machine.
- `uv`: Manages the Python environment and dependencies.
- OpenAI API: Not required for the local Ollama endpoint.

Local inference still uses your computer's memory, processor, and electricity.

## 🗺️ Learning Roadmap

This project can grow incrementally from a basic LLM client into a more capable Agentic AI application.

- [x] Set up Python and `uv`.
- [x] Install Ollama and download a local model.
- [x] Connect a Python application to a local LLM.
- [x] Build an interactive terminal-based AI assistant.
- [x] Measure response execution time.
- [ ] Improve response quality and error handling.
- [ ] Maintain conversation history across multiple prompts.
- [ ] Add structured outputs and prompt templates.
- [ ] Explore tool calling and function execution.
- [ ] Build an AI agent that can choose and execute tools.
- [ ] Explore retrieval-augmented generation (RAG).
- [ ] Experiment with multi-agent workflows.
- [ ] Build and deploy a practical AI-powered application.

## 📁 Project Structure

The project structure may evolve as new capabilities are added.

```text
Agentic-AI-By-Chitta/
├── main.py
├── pyproject.toml
├── uv.lock
├── README.md
└── .gitignore
```

- `main.py` — Entry point for the command-line AI assistant.
- `pyproject.toml` — Project metadata and dependency definitions.
- `uv.lock` — Locked dependency versions managed by `uv`.
- `README.md` — Project documentation.
- `.gitignore` — Files and local configuration that Git should ignore.

## 🔐 Security

- Do not commit API keys, passwords, or other secrets.
- Keep `.env` files out of version control if you introduce environment variables.
- Never commit virtual environments or large downloaded model files to the repository.
- Review any tools or scripts before allowing an AI agent to execute commands or modify files.

## 🎯 Project Goal

Build practical AI engineering skills by progressing from local LLM integration to tool-using agents, automation, and real-world Agentic AI applications.

**Learn by building. Experiment locally. Improve one capability at a time.**

---

**Author:** Chitta  
**Project:** Agentic-AI-By-Chitta  
**Focus:** Python | Local LLMs | Ollama | Agentic AI
