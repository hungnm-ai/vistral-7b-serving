from ctransformers import AutoModelForCausalLM
from transformers import AutoTokenizer
from constants import HF_TOKEN

tokenizer = AutoTokenizer.from_pretrained("Viet-Mistral/Vistral-7B-Chat",
                                          token=HF_TOKEN)

tokenizer.apply_chat_template

# # Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
# model = AutoModelForCausalLM.from_pretrained("janhq/Vistral-7b-Chat-GGUF",
#                                              model_file="vitral-7b-chat.Q4_K_M.gguf",
#                                              model_type="mistral",
#                                              gpu_layers=50)
#
# system_prompt = "Bạn là một trợ lí Tiếng Việt nhiệt tình và trung thực. Hãy luôn trả lời một cách hữu ích nhất có thể, đồng thời giữ an toàn.\n"
# system_prompt += "Câu trả lời của bạn không nên chứa bất kỳ nội dung gây hại, phân biệt chủng tộc, phân biệt giới tính, độc hại, nguy hiểm hoặc bất hợp pháp nào. Hãy đảm bảo rằng các câu trả lời của bạn không có thiên kiến xã hội và mang tính tích cực."
# system_prompt += "Nếu một câu hỏi không có ý nghĩa hoặc không hợp lý về mặt thông tin, hãy giải thích tại sao thay vì trả lời một điều gì đó không chính xác. Nếu bạn không biết câu trả lời cho một câu hỏi, hãy trẳ lời là bạn không biết và vui lòng không chia sẻ thông tin sai lệch."
#
# input_str = f"""<|system|>
# {system_prompt}</s>
# <|user|>
# Xin chào</s>
# <|assistant|>"""
# print("Start...")
# for token in model(input_str,
#                    temperature=0.2,
#                    max_new_tokens=512,
#                    stop=["</s>"], stream=True):
#     print(token, end="", flush=True)
#
# print("End...")
