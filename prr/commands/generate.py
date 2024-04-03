import webbrowser
from typing import List

import typer
from openai import OpenAI
from rich.prompt import Prompt
from typer_config import use_yaml_config
from typer_config.callbacks import argument_list_callback

from prr.utils.git import read_last_commit_message, get_current_branch, get_git_remote_url

app = typer.Typer()


def default_template_file_exist():
    pass


def load_default_template_file():
    # if file exist read it and return its content else return empty
    # read
    filename = "template.md"
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("Template file not found")
    return ''


@app.command()
@use_yaml_config(default_value=".prr")
def pr(
        model: str = typer.Argument(default="gpt-3.5-turbo"),
        instructions: List[str] = typer.Argument(default=None, callback=argument_list_callback),
        template: str = typer.Argument(default=None, callback=load_default_template_file),
):
    client = OpenAI(
        # Defaults to os.environ.get("OPENAI_API_KEY")
    )

    # print(instructions)

    # map instructions to messages
    instructions_messages = []
    for instruction in instructions:
        instructions_messages.append({"role": "system", "content": instruction})

    commits = read_last_commit_message().split("\n")
    context_messages = [
        {"role": "user", "content": "These are the commit message I want to use:"}
    ]
    for commit in commits:
        context_messages.append({"role": "user", "content": "- " + commit})

    context_messages.append(
        {
            "role": "system",
            "content": "Use the following template to organize and describe the changes: <template>" + template + "</template>"
        })

    while True:
        user_message = Prompt.ask("Additional notes (Press Enter to skip)")
        if user_message == "":
            break
        context_messages.append({"role": "user", "content": user_message})

    messages = [
        *instructions_messages,
        *context_messages
    ]

    # print(messages)

    chat_completion = client.chat.completions.create(
        model=model,
        messages=messages,
    )

    pr_body = chat_completion.choices[0].message.content
    current_branch = get_current_branch()

    print(pr_body)

    pr_url = get_git_remote_url() + '/compare/' + current_branch + '?&title=default&expand=1&body=' + pr_body
    webbrowser.open(pr_url, new=2)
