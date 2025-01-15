# TTS Chat (Text-to-Speech Chat Interface)

A Python-based interactive chat interface that combines Groq LLM with Kokoro's text-to-speech synthesis to create a speaking AI assistant.

## Features

- Interactive chat interface with AI responses
- Text-to-speech conversion of AI responses
- Concise and conversational AI responses
- Voice customization options
- Conversation history management

## Prerequisites

- Python 3.x
- A Groq API key (or run llama.cpp for local inference)
- You also need [`kokoro-v0_19.onnx`](https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files/kokoro-v0_19.onnx) and [`voices.json`](https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files/voices.json)


## Installation

1. Clone the repository:

```bash
git clone https://github.com/os-dave/tts-chat.git
cd tts
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Set up your environment variables:
   Create a `.env` file in the project root and add your Groq API key:

```
GROQ_API_KEY=your_api_key_here
```

## Usage

Run the main script:

```bash
python main.py
```

- Type your message and press Enter to chat with the AI
- The AI will respond both in text and speech
- Type 'quit' to exit the program

## Dependencies

- requests==2.31.0
- python-dotenv==1.0.1
- sounddevice==0.4.6
- kokoro-onnx==0.2.6
- groq==0.3.0

## License

MIT License

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
