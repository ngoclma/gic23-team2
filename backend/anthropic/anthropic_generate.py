import os
import json
import urllib3
import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv

# Defaults
ENDPOINT_URL = os.environ.get("ENDPOINT_URL", "https://api.anthropic.com/v1/complete")
DEFAULT_MODEL = os.environ.get("DEFAULT_MODEL","claude-2")

def call_llm(parameters, prompt):
    data = parameters
    data["prompt"] = prompt

    headers = {
        "anthropic-version": "2023-06-01", 
        "x-api-key": "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",
        "content-type": "application/json",
        "accept": "application/json"
    }
    http = urllib3.PoolManager()
    try:
        response = http.request(
            "POST",
            ENDPOINT_URL,
            body=json.dumps(data),
            headers=headers
        )
        if response.status != 200:
            raise Exception(f"Error: {response.status} - {response.data}")
        # print(response.data)
        generated_text = json.loads(response.data)["completion"].strip()
        return generated_text
    except Exception as err:
        print(err)
        raise


# set model params
model_params = {
    "model": DEFAULT_MODEL,
    "temperature": 0,
    "max_tokens_to_sample": 128
}
question = "Where is Singapore?"
# prompt template for Anthropic - see this page for more info: 
# https://docs.anthropic.com/claude/docs/constructing-a-prompt#use-the-correct-format
prompt = f"\n\nHuman: {question}\n\nAssistant:"

generated_text = call_llm(model_params, prompt)
print(f"Prompt: {prompt}")
print(json.dumps(generated_text))