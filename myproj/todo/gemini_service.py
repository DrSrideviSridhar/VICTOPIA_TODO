import os
'''import google.generativeai as genai
from typing import List, Dict, Any

class GeminiService:
    def __init__(self):
        api_key = os.environ.get('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.0-flash')

    def prioritize_tasks(self, tasks: List[Dict]) -> str:
        """Prioritize a list of tasks"""
        if not tasks:
            return "No tasks to prioritize"
        
        task_list = "\n".join([f"- {task['title']}" for task in tasks])
        prompt = f"""
        Here are my current tasks:
        {task_list}
        
        Please help me prioritize them by:
        1. Analyzing their urgency and importance
        2. Suggesting an order in which to complete them
        3. Explaining why this order makes sense
        
        Keep your response concise an
        d actionable.
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Error prioritizing tasks: {e}")
            return "Error occurred while prioritizing tasks."
            '''