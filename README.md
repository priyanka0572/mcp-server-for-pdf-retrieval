# MCP Server for PDF Retrieval

A Model Context Protocol (MCP) based chatbot that answers questions about a PDF resume using AI.

## Features

- 📄 **PDF Text Extraction** - Extracts and parses text from PDF documents
- 🤖 **AI-Powered Q&A** - Uses Cerebras LLM to answer questions about the PDF content
- 🔄 **MCP Protocol** - Client-server architecture using the Model Context Protocol
- ⚡ **Retry Logic** - Automatic retry on rate limiting

## Project Structure

```
├── mcp-client/
│   └── main.py          # MCP client with LLM integration
├── mcp-server/
│   └── main.py          # MCP server with PDF tool
├── Priyanka-resume.pdf  # Sample PDF document
├── requirements.txt     # Python dependencies
└── .env                 # Environment variables (API keys)
```

## Setup

1. **Create virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # Linux/Mac
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file with your API key:
   ```
   CEREBRAS_API_KEY=your_api_key_here
   ```

4. **Run the client**
   ```bash
   python mcp-client/main.py
   ```

## Usage

Once running, you can ask questions about the PDF:

```
Ask PDF (or exit): education
Bot: [Details about education from the resume]

Ask PDF (or exit): experience
Bot: [Details about work experience from the resume]

Ask PDF (or exit): exit
```

## Technologies Used

- **Python** - Core programming language
- **MCP (Model Context Protocol)** - Client-server communication
- **LangChain + Cerebras** - LLM integration
- **PyPDF** - PDF text extraction
- **FastMCP** - MCP server framework

## Author

Priyanka V - Computer Science Student at Sri Sairam Engineering College
