from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv()

# Remove hard-coded API key and load from environment variable
API_KEY = os.getenv("GROQ_API_KEY")
from groq import Groq

client = Groq(api_key=API_KEY)

def get_bot_response(query, df, low_threshold, excess_threshold):
    """
    Generate a chatbot response based solely on the inventory data analytics.
    The function builds a context prompt with the inventory summary and threshold info,
    then calls the Groq API to get a recommendation or answer.
    """
    # Create a summary of inventory data (title and quantity only)
    if not df.empty:
        inventory_summary = "\n".join([f"{row['title']}: {row['quantity']}" for index, row in df.iterrows()])
    else:
        inventory_summary = "No inventory data available."

    # Build messages for the Groq API
    messages = [
        {
            "role": "system",
            "content": (
                f"You are an inventory analytics assistant. Your responses must be based only on "
                f"the provided inventory data and threshold information. The low stock threshold is {low_threshold} "
                f"and the excess stock threshold is {excess_threshold}. Here is the current inventory data:\n"
                f"{inventory_summary}\n"
                "If the query asks about low stock, advise on reordering or restocking items below the threshold. "
                "If the query asks about excess stock, suggest discount or promotional strategies. "
                "Answer only based on this data."
            )
        },
        {
            "role": "user",
            "content": query
        }
    ]

    # Call Groq's chat completions API using streaming
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    response = ""
    for chunk in completion:
        # Append each chunk's response. The API might return None for empty chunks.
        response += chunk.choices[0].delta.content or ""
    return response
