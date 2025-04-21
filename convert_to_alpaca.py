import json

def convert_to_alpaca_format(openai_data):
    alpaca_data = []

    for message in openai_data['messages']:
        if message['role'] == 'user':
            user_prompt = message['content']
        elif message['role'] == 'assistant':
            assistant_response = message['content']
            alpaca_data.append({
                "instruction": user_prompt.strip(),
                "input": "",
                "output": assistant_response.strip()
            })

    return alpaca_data

if __name__ == "__main__":
    with open("../training_data/openai_export.json", "r", encoding="utf-8") as infile:
        openai_data = json.load(infile)

    formatted = convert_to_alpaca_format(openai_data)

    with open("../training_data/formatted_conversations.json", "w", encoding="utf-8") as outfile:
        json.dump(formatted, outfile, indent=2)

    print("✅ Conversion complete. Ready for fine-tuning!")
