# test different LLMs: Llama 3.0
# Embedding pair: Faiss

from langchain import Llama, LLMChain
from langchain.embeddings import FaissEmbeddings
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# LLaMA 3.0 API Key placeholder ('LLAMA_API_KEY')
api_key = os.getenv('LLAMA_API_KEY')
if not api_key:
    raise ValueError("API key not found. Please set the LLAMA_API_KEY environment variable.")

# Initialize the Faiss embeddings
embedding_model = FaissEmbeddings()

# Setup the LLMChain with the embedding model
llm_chain = LLMChain(llm=Llama(api_key=api_key), embedding_model=embedding_model)

def get_menu_from_restaurant_llama(name, address):
    try:
        query = f"Get the menu for {name} located at {address}"
        result = llm_chain(query)
        return result
    except Exception as e:
        logger.error(f"Error retrieving menu for {name} at {address}: {e}")
        return []

def find_vegetarian_options(menu):
    vegetarian_keywords = ['vegetarian', 'vegan', 'plant-based', 'meat-free']
    vegetarian_options = [item for item in menu if any(keyword in item.lower() for keyword in vegetarian_keywords)]
    return vegetarian_options

def generate_summary(menu, vegetarian_options):
    prompt = f"The menu includes the following items: {menu}. The vegetarian options are: {vegetarian_options}. Please provide a summary."
    try:
        summary = llm_chain(prompt)
        return summary
    except Exception as e:
        logger.error(f"Error generating summary: {e}")
        return "Error in generating summary."

def workflow(name, address):
    menu = get_menu_from_restaurant_llama(name, address)
    vegetarian_options = find_vegetarian_options(menu)
    summary = generate_summary(menu, vegetarian_options)
    
    return {
        "restaurant": name,
        "address": address,
        "menu": menu,
        "vegetarian_options": vegetarian_options,
        "summary": summary
    }

test_data = [
    {"name": "Joe's Diner", "address": "123 Main St, Springfield, IL"},
    {"name": "The Green Table", "address": "456 Elm St, Boulder, CO"},
    {"name": "Sunny Cafe", "address": "789 Pine St, Austin, TX"},
    {"name": "Veggie Delight", "address": "101 Maple Ave, Portland, OR"},
    {"name": "Healthy Eats", "address": "202 Oak St, Miami, FL"},
]

def test_workflow():
    for data in test_data:
        name = data["name"]
        address = data["address"]
        logger.info(f"Testing {name} at {address}")

        try:
            result = workflow(name, address)
            logger.info(f"Result: {result}")

            print(f"Restaurant: {result['restaurant']}")
            print("Menu:", result['menu'])
            print("Vegetarian Options:", result['vegetarian_options'])
            print("Summary:", result['summary'])
            print("-" * 40)
        except Exception as e:
            logger.error(f"Error processing {name} at {address}: {e}")

if __name__ == "__main__":
    test_workflow()
