import openai
import re

openai.api_key = open("openai_key", "r").read()

def generate_chinese_report(markdown_file:str)->str:
    # Read the contents of the Markdown file
    with open(markdown_file, 'r', encoding='utf-8') as f:
        markdown_text = f.read()

    # Remove any Markdown formatting that would interfere with GPT-3
    plain_text = re.sub('[^A-Za-z0-9\s\u4e00-\u9fa5]+', '', markdown_text)

    # Generate a report using GPT-3 with Chinese model
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"please generate a report with the following content in traditional Chinese.\n" + plain_text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extract the generated report from the API response
    report_text = response.choices[0].text
    return report_text

print(generate_chinese_report("test.md"))