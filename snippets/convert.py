import yaml
import os

def convert_curl_to_markdown(curl_command):
    return f"```bash cURL\n{curl_command}\n```"

def process_yaml_file():
    # Read YAML file
    with open('./code-samples.yaml', 'r') as file:
        code_samples = yaml.safe_load(file)

    # Create output directory if it doesn't exist
    os.makedirs('code_samples', exist_ok=True)

    # Process each code sample
    for sample_name, curl_command in code_samples.items():
        # Create markdown content
        markdown_content = convert_curl_to_markdown(curl_command)
        
        # Create file for each code sample
        output_file = f"code_samples/{sample_name}.md"
        with open(output_file, 'w') as f:
            f.write(markdown_content)

if __name__ == "__main__":
    process_yaml_file()
