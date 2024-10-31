Almma Health LLM Testing Suite
This project evaluates different Large Language Models (LLMs) for integration into Almma Health’s digital platform, aiming to enhance holistic health support by ensuring relevance, accuracy, and user satisfaction.

Project Overview
Almma Health’s mission is to empower personal health journeys through reliable, AI-supported guidance. This project tests the suitability of multiple LLMs to provide effective, personalized health advice, assessing metrics like response accuracy, contextual relevance, and user satisfaction.

Technologies Used
LLMs Tested: OpenAI, Gemini, Mistral, Claude
Frameworks: LangChain, Bubble (for frontend)
Languages: Python (for backend and testing scripts)
Installation & Setup
Clone the Repository:

bash
Copy code
git clone https://github.com/almma-health/llm-testing-suite.git
cd llm-testing-suite
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Configure API Keys: Add API keys for each LLM in the .env file:

OPENAI_API_KEY=your_openai_key
GEMINI_API_KEY=your_gemini_key
CLAUDE_API_KEY=your_claude_key
MISTRAL_API_KEY=your_mistral_key
Set Up Frontend (Optional): Deploy the frontend using Bubble if testing with a user interface.

Usage
Running Tests:

Run the main testing script to evaluate each LLM:
bash
Copy code
python test_llms.py
Results are saved in the results/ folder as .csv files.
Generating Reports:

Use the reporting tool to generate summaries and comparative insights:
bash
Copy code
python generate_report.py
LLM Testing Framework
Our testing framework evaluates models on:

Response Accuracy: Alignment of responses with expected health advice.
Context Relevance: Ability to maintain context across multi-turn interactions.
User Satisfaction: Based on simulated user experience.
Each LLM is tested in controlled environments to ensure consistency.

Testing Scenarios
Testing involves real-life health support scenarios, such as:

General Health Advice: Diet, exercise, and mental wellness.
Symptom Checker: Identifying potential health issues.
Holistic Lifestyle Tips: Recommendations for stress management, sleep, etc.
Preventive Health Measures: Tailored advice on preventive actions.

Example Scenario
For diet-related queries, models are prompted with:

"What are healthy snack options for someone looking to lose weight and gain muscle?"



