import os
from cerebras.cloud.sdk import Cerebras
import yaml


with open("config.yaml") as f:
    config = yaml.safe_load(f)

client = Cerebras(
    # This is the default and can be omitted
    api_key=config["CEREBRAS_API_KEY"]
)

stream = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "how much calories in a single avocado. details but short and brief answer!"
        }
    ],
    model="gpt-oss-120b",
    stream=True,
    max_completion_tokens=65536,
    temperature=1,
    top_p=1,
    reasoning_effort="medium",
)

for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")

print()

