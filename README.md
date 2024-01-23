# Serving LLM in GGUF Format for Multi-Tasking

----

_Welcome to our project! 🚀 Harnessing the capabilities of Language Model (LLM) architectures, we use FastAPI to deploy
the LLM [Vistral-7b-Chat-GGUF](https://huggingface.co/janhq/Vistral-7b-Chat-GGUF).
Subsequently, we expose an API to facilitate the execution of various Natural Language Processing (NLP) tasks such as
chatbot interactions, question answering, text summarization, and more. 🌐✨_

## Key Features

* Model: Vistral-7b-Chat-GGUF
* API: FastAPI-powered for efficiency
* Tasks: Chatbot, QA, Summarization, NLP tasks
* Compatibility: Runs seamlessly on consumer CPUs, CUDA-enabled GPUs, and Apple's chips.

## 1.Usage

### 1.1 Install libraries

#### Install ctransformers

We uses **ctransformers** to load GGUF model. To install, you can choose one of the following ways, depending on your
device:

**CPU**

```bash
pip install ctransformers
```

**CUDA**

```bash 
pip install ctransformers[cuda]
```

**Metal** (Apple's chip)

```bash
CT_METAL=1 pip install ctransformers --no-binary ctransformers
```

#### Install other dependencies

```bash
pip install -r requirements.txt
```

#### Add .env File
Before running the service, you need to create a .env file and add your Hugging Face token variable. Ensure that your token has the necessary permissions to access [Viet-Mistral/Vistral-7B-Chat](https://huggingface.co/Viet-Mistral/Vistral-7B-Chat).

Create a file named .env in the root directory of your project and add the following line:

```
HF_TOKEN=<your Hugging Face token>

```
Replace <your Hugging Face token> with your actual Hugging Face token. This token is crucial for authenticating and accessing the Vistral-7B-Chat model.


### 1.2 Run the Server:

``` bash
sh run.sh
```

## 2. API Documentation

#### 2.1 Check health

```bash
curl -X GET http://localhost:8080/ping
```

#### 2.2 Generate new tokens

Endpoint: `/generate`

Method: `POST`

Parameters:

* `conversation`

    ```json
    [
      {
        "role": "str",
        "content": "str"
      }
    ]
    ```
  
  _role will receive one of 3 values: **system** | **user** | **assistant**_ 


* `LLMParameters`
    
    | parameters         | data type | Default    | Description                                              |
    |--------------------|-----------|------------|----------------------------------------------------------|
    | top_k              | int       | 40         | The top-k value to use for sampling.                     |
    | top_p              | float     | 0.95       | The top-p value to use for sampling.                     |
    | temperature        | float     | 0.1        | The temperature value to use for sampling.               |
    | repetition_penalty | float     | 1.1        | The repetition penalty to use for sampling.              |
    | stop               | List[str] | ["\</s>" ] | A list of sequences to stop generation when encountered. |
    | stream             | bool      | false      | Whether to stream the generated text                     |


**Example Usage**

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "conversation": [
        {"role": "system", "content": "Bạn là một trợ lý ảo AI"},
        {"role": "user", "content": "chào bạn"}
    ]
  }' \
  http://localhost:8080/generate

```

## 3. Quick Examples

### 3.1 Chatbot

### 3.2 Text summarization

### 3.3 Question answering

