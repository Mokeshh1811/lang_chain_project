# LangChain Projects Repository

This repository is a collection of LangChain-based projects demonstrating various concepts such as types of memories, agents, tools, and other advanced features. Each project includes executable code and examples to help you understand and implement LangChain effectively in your own applications.

---

## Table of Contents

1. [About the Repository](#about-the-repository)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Projects Included](#projects-included)
6. [Contributing](#contributing)
7. [License](#license)

---

## About the Repository

This repository serves as a comprehensive guide to LangChain, showcasing how to:

- Utilize different memory types (e.g., BufferMemory, ConversationMemory, etc.).
- Create and use various agents (e.g., Zero-Shot Agents, Tool-using Agents).
- Integrate tools into LangChain workflows.
- Implement prompts and chains for complex reasoning tasks.

Whether you are a beginner or an advanced user, this repository provides practical examples and code snippets to help you harness the power of LangChain.

---

## Features

- **Executable Examples**: Each project includes code that you can execute directly.
- **Memory Types**: Demonstrates the use of multiple memory implementations.
- **Agent Types**: Covers a variety of agent configurations and use cases.
- **Tool Integration**: Examples of creating and integrating tools into LangChain agents.
- **Detailed Explanations**: Comments and explanations are included to make the code easy to understand.

---

## Installation

To run the projects in this repository, ensure you have Python 3.8 or higher installed.

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/langchain-projects.git
   cd langchain-projects
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up any required API keys or environment variables for services like OpenAI, Google Generative AI, etc.
   ```bash
   export OPENAI_API_KEY='your_openai_key_here'
   ```

---

## Usage

Navigate to the desired project folder and run the corresponding script:

```bash
cd agents
python zero_shot_agent.py
```

Each project folder contains a `README.md` file explaining the specific example and its usage.

---

## Projects Included

### 1. **Memory Types**
   - **BufferMemory**: Retains all messages in a conversation.
   - **ConversationMemory**: Tracks context over time.
   - **SummaryMemory**: Summarizes context to save memory.

### 2. **Agents**
   - **Zero-Shot Agents**: Solve problems with no prior examples.
   - **Tool-Using Agents**: Integrate tools for enhanced functionality.

### 3. **Tool Integration**
   - Examples of creating and using custom tools with LangChain.
   - Tools for calculations, string processing, etc.

### 4. **Prompts and Chains**
   - Custom prompt creation.
   - Multi-step reasoning with chains.

### 5. **Miscellaneous**
   - Integration with third-party APIs (e.g., OpenAI, Google Generative AI).
   - Complex workflows and task automation.

---

## Contributing

Contributions are welcome! If you have new ideas or improvements, please feel free to submit a pull request or open an issue.

### Steps to Contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add feature-name"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

---

