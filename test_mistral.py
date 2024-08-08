 # test different LLMs: Mistral
# Embedding pair: GloveEmbeddings
from langchain import Mistral, LLMChain
from langchain.embeddings import GloveEmbeddings
import os
import logging
import time

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Mistral API Key placeholder ('MISTRAL_API_KEY')
api_key = os.getenv('PlaceHolder')
if not api_key:
    raise ValueError("API key not found. Please set the MISTRAL_API_KEY environment variable.")

# Initialize the GloVe embeddings
embedding_model = GloveEmbeddings()

# Setup the LLMChain with the embedding model
llm_chain = LLMChain(llm=Mistral(api_key=api_key), embedding_model=embedding_model)

def get_menu_from_restaurant_mistral(name, address):
    try:
        start_time = time.time()  # Record the start time
        query = f"Get the menu for {name} located at {address}"
        result = llm_chain(query)
        end_time = time.time()  # Record the end time
        time_taken = end_time - start_time  # Calculate the elapsed time
        logger.info(f"Time taken to retrieve menu for {name} at {address}: {time_taken:.2f} seconds")
        return result, time_taken  # Return the result and the time taken
    except Exception as e:
        logger.error(f"Error retrieving menu for {name} at {address}: {e}")
        return [], 0

def find_vegetarian_options(menu):
    vegetarian_keywords = ['vegetarian', 'vegan', 'plant-based', 'meat-free']
    vegetarian_options = [item for item in menu if any(keyword in item.lower() for keyword in vegetarian_keywords)]
    return vegetarian_options

def generate_summary(menu, vegetarian_options):
    prompt = f"The menu includes the following items: {menu}. The vegetarian options are: {vegetarian_options}. Please provide a summary."
    try:
        start_time = time.time()  # Record the start time
        summary = llm_chain(prompt)
        end_time = time.time()  # Record the end time
        time_taken = end_time - start_time  # Calculate the elapsed time
        logger.info(f"Time taken to generate summary: {time_taken:.2f} seconds")
        return summary, time_taken  # Return the summary and the time taken
    except Exception as e:
        logger.error(f"Error generating summary: {e}")
        return "Error in generating summary.", 0

def workflow(name, address):
    menu, menu_time = get_menu_from_restaurant_mistral(name, address)
    vegetarian_options = find_vegetarian_options(menu)
    summary, summary_time = generate_summary(menu, vegetarian_options)
    
    return {
        "restaurant": name,
        "address": address,
        "menu": menu,
        "vegetarian_options": vegetarian_options,
        "summary": summary,
        "time_taken": {
            "menu_retrieval": menu_time,
            "summary_generation": summary_time
        }
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
            print("Time Taken:", result['time_taken'])
            print("-" * 40)
        except Exception as e:
            logger.error(f"Error processing {name} at {address}: {e}")

if __name__ == "__main__":
    test_workflow()
