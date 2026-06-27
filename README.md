# 🤖 AI Multi-Domain Chatbot

A powerful multi-domain AI chatbot built with Python, Flask, and OpenAI API. This chatbot can assist users in multiple domains:

- 📚 **Education** - Study helper and concept explainer
- 🏥 **Health & Fitness** - Health tips and wellness advice
- 💼 **Career** - Job guidance and resume help
- 🍕 **Food & Recipes** - Recipe suggestions and nutrition info
- 🏠 **Real Estate** - Property advice and investment guidance
- 📱 **Tech Support** - Coding help and troubleshooting

## Features

✨ **Multi-Domain Support** - Switch between different domains seamlessly
🎨 **Beautiful UI** - Modern, responsive web interface
🚀 **Fast & Reliable** - Built on Flask and OpenAI API
🌍 **Hindi/English Support** - Bilingual responses
💬 **Real-time Chat** - Instant AI responses

## Prerequisites

- Python 3.8+
- OpenAI API Key (Get it from: https://platform.openai.com/api-keys)
- pip (Python package manager)

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/s24911720/ai-multi-domain-chatbot.git
cd ai-multi-domain-chatbot
```

### 2. Create a virtual environment
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup environment variables
```bash
# Create .env file (copy from .env.example)
cp .env.example .env

# Edit .env and add your OpenAI API key:
# OPENAI_API_KEY=your_api_key_here
```

## Usage

### Run the application
```bash
python app.py
```

### Access the chatbot
Open your browser and go to:
```
http://localhost:5000
```

### How to use:
1. Select a domain from the buttons at the top
2. Type your question or message
3. Press Enter or click Send
4. Get instant AI-powered responses!

## Project Structure
```
ai-multi-domain-chatbot/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── README.md             # This file
└── templates/
    └── index.html        # Frontend HTML/CSS/JS
```

## API Endpoints

### GET `/`
Returns the main chatbot interface

### POST `/api/chat`
Send a message to the chatbot
```json
{
  "message": "Your question here",
  "domain": "education"
}
```

### GET `/api/domains`
Get list of available domains

## Domains & Use Cases

### 📚 Education
- Explain complex concepts
- Study tips and learning strategies
- Subject guidance
- Assignment help

### 🏥 Health & Fitness
- Health tips and wellness advice
- Fitness recommendations
- Nutrition guidance
- Lifestyle improvements

### 💼 Career
- Career planning
- Resume and cover letter help
- Job search strategies
- Interview preparation

### 🍕 Food & Recipes
- Recipe suggestions
- Nutritional information
- Cooking tips
- Dietary recommendations

### 🏠 Real Estate
- Property advice
- Investment guidance
- Neighborhood information
- Home buying/selling tips

### 📱 Tech Support
- Coding help
- Programming concepts
- Troubleshooting
- Tech tips and solutions

## Customization

### Add more domains:
1. Add domain-specific prompt in `DOMAIN_PROMPTS` in `app.py`
2. Add domain button in `templates/index.html`
3. Update `/api/domains` endpoint

### Modify system prompts:
Edit the `DOMAIN_PROMPTS` dictionary in `app.py` to customize chatbot behavior for each domain.

## Troubleshooting

### "API key not found"
- Make sure you've created `.env` file
- Check that `OPENAI_API_KEY` is properly set
- Verify your API key is valid

### "Connection refused"
- Make sure Flask app is running: `python app.py`
- Check if port 5000 is available
- Try a different port: `app.run(port=5001)`

### "Rate limit exceeded"
- You've made too many API calls
- Wait a few minutes before trying again
- Consider upgrading your OpenAI plan

## Future Enhancements

- [ ] Chat history saving
- [ ] User authentication
- [ ] More domains
- [ ] Voice input/output
- [ ] Mobile app version
- [ ] Multi-language support
- [ ] Database integration
- [ ] Rate limiting

## License

This project is open source and available under the MIT License.

## Support

For issues and questions:
1. Check the troubleshooting section
2. Review OpenAI API documentation
3. Create an issue on GitHub

## Author

Created with ❤️ by s24911720

---

**Happy Chatting! 🤖✨**
