from model import ask_model

reply = ask_model("qwen3.5:latest", "You are a helpful assistant.", "Say hello in one sentence.")
print(reply)