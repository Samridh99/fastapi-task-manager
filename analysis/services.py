"""
Analysis service for task categorization using Google Gemini.
Converted from the original analyzer.py FastAPI implementation.
"""

from django.conf import settings
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnablePassthrough, RunnableSequence
from langgraph.graph import StateGraph
from typing import TypedDict, Dict, Any


class AnalysisState(TypedDict):
    """State structure for the analysis workflow."""
    description: str
    response: str


class TaskAnalyzer:
    """Service class for analyzing and categorizing tasks using Google Gemini."""
    
    def __init__(self):
        if not settings.GEMINI_API_KEY:
            raise ValueError("Missing Gemini API Key. Set GEMINI_API_KEY in environment variables.")
        
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-pro", 
            google_api_key=settings.GEMINI_API_KEY
        )
        
        self.prompt_template = PromptTemplate(
            input_variables=["description"],
            template="Categorize the following task description into one of these categories: 'Bug', 'Feature Request', 'Improvement'. Description: {description}",
        )
        
        self.llm_chain = RunnableSequence(
            RunnablePassthrough(),  # Pass the input directly to the prompt
            self.prompt_template,   # Apply the prompt template
            self.llm,              # Pass the output to Gemini
        )
        
        # Set up the workflow graph
        self.workflow = self._create_workflow()
        self.analyzer_workflow = self.workflow.compile()
    
    def _create_workflow(self):
        """Create the analysis workflow graph."""
        workflow = StateGraph(AnalysisState)
        
        workflow.add_node("preprocess", self._preprocess_description)
        workflow.add_node("query_llm", self._query_llm)
        workflow.add_node("extract_category", self._extract_category)
        
        workflow.add_edge("preprocess", "query_llm")
        workflow.add_edge("query_llm", "extract_category")
        
        workflow.set_entry_point("preprocess")
        workflow.set_finish_point("extract_category")
        
        return workflow
    
    def _preprocess_description(self, state: AnalysisState) -> Dict[str, Any]:
        """Pre-process the task description (e.g., clean text)."""
        return {"description": state["description"].strip()}
    
    def _query_llm(self, state: AnalysisState) -> Dict[str, Any]:
        """Query Gemini to get the category."""
        description = state["description"]
        response = self.llm_chain.invoke({"description": description})
        return {"response": response.content.strip()}
    
    def _extract_category(self, state: AnalysisState) -> str:
        """Extract the category from the Gemini response."""
        response = state["response"]
        categories = ["Bug", "Feature Request", "Improvement"]
        for category in categories:
            if category.lower() in response.lower():
                return category
        return "Uncategorized"
    
    def analyze(self, description: str) -> str:
        """
        Analyze a task description and return its category.
        
        Args:
            description (str): The task description to analyze
            
        Returns:
            str: The categorized type (Bug, Feature Request, Improvement, or Uncategorized)
        """
        result = self.analyzer_workflow.invoke({"description": description})
        return result


# Global analyzer instance
_analyzer = None


def get_analyzer():
    """Get or create the global task analyzer instance."""
    global _analyzer
    if _analyzer is None:
        _analyzer = TaskAnalyzer()
    return _analyzer