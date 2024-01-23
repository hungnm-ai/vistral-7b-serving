import json
import asyncio
from typing import *
from fastapi import FastAPI
from transformers import AutoTokenizer
from api.sse import EventSourceResponse
from constants import HF_TOKEN, MODEL_NAME
from fastapi.responses import JSONResponse
from ctransformers import AutoModelForCausalLM
from api.models import LLMParameters, Conversation
from log import logger

app = FastAPI()

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME,
                                          token=HF_TOKEN)

# Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
model = AutoModelForCausalLM.from_pretrained("janhq/Vistral-7b-Chat-GGUF",
                                             model_file="vitral-7b-chat.Q4_K_M.gguf",
                                             model_type="mistral",
                                             context_length=4096,
                                             gpu_layers=100)


@app.on_event("startup")
def on_startup():
    print("Starting up...")


@app.on_event("shutdown")
def on_shutdown():
    print("Shutting down...")


@app.get("/ping")
def ping():
    return JSONResponse(content={"message": "I'm alive!"}, status_code=200)


@app.post("/generate")
def generate(conversations: List[Conversation], llm_parameters: LLMParameters = None):
    conversations_parsed = []
    for conversation in conversations:
        conversation.role = conversation.role.value
        conversations_parsed.append(dict(conversation)
                                    )
    input_str = tokenizer.apply_chat_template(conversations, tokenize=False)
    if llm_parameters is None:
        llm_parameters = LLMParameters()
    assistant = model(input_str,
                      **dict(llm_parameters))
    stream = llm_parameters.stream
    if stream:
        async def streaming_tokens():
            full_answer = ""
            for _token in assistant:
                full_answer += _token
                await asyncio.sleep(0.03)
                yield json.dumps({"token": _token})

            yield json.dumps({"token": "[DONE]"})

        if stream:
            return EventSourceResponse(streaming_tokens(), media_type='text/event-stream', ping=10000)
    else:
        logger.info(f"assistant: {assistant}")
        response = {
            "text": assistant
        }

        return JSONResponse(content=response, status_code=200)
