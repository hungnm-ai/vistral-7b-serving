from typing import *
from enum import Enum
from pydantic import BaseModel, Field


class Role(Enum):
    system: str = "system"
    user: str = "user"
    assistant: str = "assistant"


class Conversation(BaseModel):
    role: Role = Field(..., description="Define the role of the conversation",
                       examples=["system", "user", "assistant"])
    content: str = Field(..., description="content of the conversation")


class LLMParameters(BaseModel):
    top_k: Optional[int] = Field(default=40, description="The top-k value to use for sampling.")
    top_p: Optional[float] = Field(default=0.95, description="The top-p value to use for sampling.")
    temperature: Optional[float] = Field(default=0.1, description="The temperature to use for sampling.")
    repetition_penalty: Optional[float] = Field(default=1.1, description="The repetition penalty to use for sampling.")
    stop: Optional[List[str]] = Field(default=["</s>"],
                                      description="A list of sequences to stop generation when encountered.")
    stream: Optional[bool] = Field(default=False, description="Whether to stream the generated text.")
