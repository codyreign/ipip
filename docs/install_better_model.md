# Install Better Model for ipip

Run these commands in Windows where Ollama is installed:

```cmd
# Install a text-focused model (recommended)
ollama pull llama3.2

# Or install Mistral (smaller, faster)
ollama pull mistral

# Verify installation
ollama list
```

Then test ipip again:
```cmd
ipip --verbose "build a chatbot" --dry-run
```

Expected output with llama3.2:
```
Using Ollama model: llama3.2
LLM confidence: 0.9
Reasoning: For building a chatbot, you need NLP libraries...
Resolved packages: ['transformers', 'torch', 'flask', 'openai']
```
EOF < /dev/null
