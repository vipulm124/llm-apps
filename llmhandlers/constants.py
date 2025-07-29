from enum import Enum
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="02-Cart Analyzer/.env")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


class LLMPROVIDERS(Enum):
    OPENAI=1
    GROK=2






PROMPT_PROCESS_SCREENSHOTS = """
Extract all unique products from the images. For each product, return a JSON with the following fields:
product_name: name of the product from the screenshot
price: price from the cart
protein_per_serving: search online and extract how many grams of protein are there per serving
serving_size: the weight of one serving in grams (not scoop count, actual grams)
product_specs: a short string describing protein per serving and scoop size, e.g., "30g protein in 2 scoops (80g)"

Format the final output as:
{
  "no_of_products": n,
  "products": [ ... ]
}
Do not give any other pre or post text, give just the above format json as output, this is very important.
Use only one record per unique product, and only include products visible in the screenshots I provided. All values must be based on verified product specifications from reliable online sources.
Search for only these products online to get more information
"""


PROMPT_CONVERSATION = """
Reply the below question. Make sure you answer only from the CONTEXT mentioned below and even if you have to search online, you only search for the products from the context and no other product. In case the information is already available in context, answer from there.
When answering about measurement, always consider all products at the same scale and unit of measurement and then respond.
Context : {0}
Give response in markdown format
"""
