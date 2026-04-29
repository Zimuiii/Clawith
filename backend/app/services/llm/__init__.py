"""LLM service module - unified LLM calling interface.

This module provides:
- call_llm: Basic LLM call with tool support
- call_llm_with_failover: LLM call with automatic failover
- call_agent_llm: Agent chat LLM call
- call_agent_llm_with_tools: Agent LLM call with tools for background tasks

Example:
    from app.services.llm import call_llm, call_llm_with_failover

    # Basic call (returns LLMResult with .content and .tool_messages)
    result = await call_llm(model, messages, agent_name, role_description)
    reply = result.content  # the text response

    # With failover
    result = await call_llm_with_failover(
        primary_model=primary,
        fallback_model=fallback,
        messages=messages,
        ...
    )
    reply = result.content
    # result.tool_messages contains intermediate assistant(tool_use) + tool(tool_result)
    # pairs that should be appended to the conversation list for message structure integrity.
"""

from .caller import (
    call_llm,
    call_llm_with_failover,
    call_agent_llm,
    call_agent_llm_with_tools,
    FailoverGuard,
    is_retryable_error,
    LLMResult,
)
from .client import LLMClient, LLMResponse, LLMError, LLMMessage
from .failover import classify_error, FailoverErrorType
from .utils import create_llm_client, get_max_tokens, get_model_api_key, get_provider_base_url, get_provider_manifest

__all__ = [
    # Core caller functions
    "call_llm",
    "call_llm_with_failover",
    "call_agent_llm",
    "call_agent_llm_with_tools",
    # Failover utilities
    "FailoverGuard",
    "is_retryable_error",
    "classify_error",
    "FailoverErrorType",
    # Client classes
    "LLMClient",
    "LLMResponse",
    "LLMError",
    "LLMMessage",
    "LLMResult",
    # Utilities
    "create_llm_client",
    "get_max_tokens",
    "get_model_api_key",
    "get_provider_base_url",
    "get_provider_manifest",
]
