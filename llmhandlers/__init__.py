from .constants import LLMPROVIDERS
from .base import LLMBase
from .openaillm  import OpenAILLM

def get_llm_provider(provider: LLMPROVIDERS) -> LLMBase:
    if not provider:
        return None
    model_name = get_model(provider)
    llm_map = {
        LLMPROVIDERS.OPENAI.value: OpenAILLM(model_name=model_name),
        LLMPROVIDERS.GROK.value: OpenAILLM(model_name=model_name)
    }

    return llm_map[provider.value]


def get_model(provider: LLMPROVIDERS) -> str:
    if not provider:
        return None
    
    models = {
        LLMPROVIDERS.OPENAI.value: 'gpt-4o',
        LLMPROVIDERS.GROK.value: 'grok-4'
    }
    return models[provider.value]