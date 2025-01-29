from openai import OpenAI
from typing import Optional, List, Dict


class AIHandler:
    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo"):
        """Initialize AI Handler with OpenAI API configuration"""
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def generate_response(
            self,
            user_message: str,
            system_prompt: Optional[str] = None,
            temperature: float = 0.7,
            max_tokens: int = 150
    ) -> str:
        """Generate AI response using OpenAI's Chat Completion API"""
        messages = []

        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})

        messages.append({"role": "user", "content": user_message})

        try:
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens
            )

            return completion.choices[0].message.content.strip()

        except Exception as e:
            return f"Error generating response: {str(e)}"

    def generate_contextual_response(
            self,
            conversation_history: List[Dict[str, str]],
            user_message: str,
            system_prompt: Optional[str] = None
    ) -> str:
        """Generate response with context from previous conversation"""
        messages = conversation_history.copy()

        if system_prompt:
            messages.insert(0, {"role": "system", "content": system_prompt})

        messages.append({"role": "user", "content": user_message})

        try:
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=messages
            )

            return completion.choices[0].message.content.strip()

        except Exception as e:
            return f"Error generating contextual response: {str(e)}"