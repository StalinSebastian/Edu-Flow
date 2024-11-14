import os
import warnings

# Suppress SyntaxWarnings
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

from langtrace_python_sdk import langtrace

# Load the API key from the .env file
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Initialize Langtrace with the API key
langtrace_api_key = os.getenv("LANGTRACE_API_KEY")
langtrace_client = langtrace.init(api_key=langtrace_api_key)

# You can now use langtrace_client throughout your application
