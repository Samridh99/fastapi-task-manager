from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnablePassthrough, RunnableSequence
from langgraph.graph import Graph
import os
from dotenv import load_dotenv

load_dotenv()


gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("Missing Gemini API Key. Set GEMINI_API_KEY as an environment variable.")


llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=gemini_api_key)


prompt_template = PromptTemplate(
    input_variables=["description"],
    template="Categorize the following task description into one of these categories: 'Bug', 'Feature Request', 'Improvement'. Description: {description}",
)


llm_chain = RunnableSequence(
    RunnablePassthrough(),  # Pass the input directly to the prompt
    prompt_template,        # Apply the prompt template
    llm,                    # Pass the output to Gemini
)


def preprocess_description(state: dict) -> dict:
    """Pre-process the task description (e.g., clean text)."""
    return {"description": state["description"].strip()}

def query_llm(state: dict) -> dict:
    """Query Gemini to get the category."""
    description = state["description"]
    response = llm_chain.invoke({"description": description})
    return {"response": response.content.strip()} 

def extract_category(state: dict) -> str:
    """Extract the category from the Gemini response."""
    response = state["response"]
    categories = ["Bug", "Feature Request", "Improvement"]
    for category in categories:
        if category.lower() in response.lower():
            return category
    return "Uncategorized"


workflow = Graph()

workflow.add_node("preprocess", preprocess_description)
workflow.add_node("query_llm", query_llm)
workflow.add_node("extract_category", extract_category)

workflow.add_edge("preprocess", "query_llm")
workflow.add_edge("query_llm", "extract_category")

workflow.set_entry_point("preprocess")
workflow.set_finish_point("extract_category")


analyzer_workflow = workflow.compile()