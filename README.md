# LangChain Project with Groq

This repository contains a LangChain implementation utilizing the Groq API for high-performance LLM inference.

##  Features
* Integration with LangChain frameworks.
* Powered by Groq LPU™ Inference Engine.
* Environment variable management for security.

##  Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/25955A0512/LangChain.git](https://github.com/25955A0512/LangChain.git)
   cd LangChain
   
2. Create a virtual environment:

Bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
Install dependencies:

Bash
pip install langchain langchain-groq python-dotenv
 Configuration
To run this project, you need to set up your environment variables:

Create a .env file in the root directory.
Add your Groq API Key:
Code snippet
GROQ_API_KEY=your_api_key_here
Note: The .env file is included in .gitignore to prevent your private API keys from being uploaded to GitHub.

 Usage
Run the main application script:

Bash
python main.py

---
