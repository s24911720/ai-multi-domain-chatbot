from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

# Domain-specific system prompts
DOMAIN_PROMPTS = {
    'education': """You are an expert education assistant and concept explainer. 
    - Explain complex concepts in simple terms
    - Use examples and analogies
    - Break down topics step by step
    - Provide study tips and learning strategies
    - Ask clarifying questions if needed
    - Language: Hindi/English mix""",
    
    'health': """You are a health and fitness advisor. 
    - Provide general health tips and wellness advice
    - Give fitness and exercise recommendations
    - Offer nutrition and diet guidance
    - Suggest healthy lifestyle habits
    - IMPORTANT: Always mention to consult a doctor for serious conditions
    - Language: Hindi/English mix""",
    
    'career': """You are a career counselor and job guidance expert. 
    - Help with career planning and guidance
    - Provide resume and cover letter tips
    - Discuss job search strategies
    - Offer interview preparation advice
    - Suggest career paths based on interests
    - Language: Hindi/English mix""",
    
    'food': """You are a food and nutrition expert. 
    - Suggest recipes based on ingredients
    - Provide nutritional information
    - Give cooking tips and techniques
    - Offer dietary recommendations
    - Suggest healthy alternatives
    - Language: Hindi/English mix""",
    
    'realestate': """You are a real estate advisor. 
    - Help with property advice and guidance
    - Explain real estate concepts
    - Provide investment tips
    - Discuss neighborhood information
    - Offer home buying and selling guidance
    - Language: Hindi/English mix""",
    
    'techsupport': """You are a technical support expert and coding helper. 
    - Help with coding problems and debugging
    - Explain programming concepts
    - Provide troubleshooting guidance
    - Offer tech tips and solutions
    - Help with software and hardware issues
    - Language: Hindi/English mix"""
}

def get_chatbot_response(message, domain='education'):
    """Get response from OpenAI based on domain"""
    try:
        system_prompt = DOMAIN_PROMPTS.get(domain, DOMAIN_PROMPTS['education'])
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": message}
            ],
            temperature=0.7,
            max_tokens=500
        )
        
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    domain = data.get('domain', 'education')
    
    if not user_message:
        return jsonify({'error': 'Message is required'}), 400
    
    # Get AI response
    ai_response = get_chatbot_response(user_message, domain)
    
    return jsonify({
        'user_message': user_message,
        'ai_response': ai_response,
        'domain': domain
    })

@app.route('/api/domains', methods=['GET'])
def get_domains():
    domains = {
        'education': '📚 Education - Study Helper',
        'health': '🏥 Health & Fitness',
        'career': '💼 Career Guidance',
        'food': '🍕 Food & Recipes',
        'realestate': '🏠 Real Estate',
        'techsupport': '📱 Tech Support'
    }
    return jsonify(domains)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
