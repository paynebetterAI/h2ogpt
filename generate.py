import os
import sys

if os.path.dirname(os.path.abspath(__file__)) not in sys.path:
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.gen import main
from src.utils import H2O_Fire
os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_VERSION"] = "2023-05-15"
os.environ["OPENAI_API_BASE"] = "https://aiga-gpt-000.openai.azure.com/"
os.environ["OPENAI_API_KEY"] = ""

def entrypoint_main():
    H2O_Fire(main)


if __name__ == "__main__":
    entrypoint_main()
