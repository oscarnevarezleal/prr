# prrr

This is a simple tool to help you manage your pull requests.

## Requirements

This project requires and OpenAPI token to exist in your environment variables.

```shell
OPENAI_API_KEY=your_api_key
``` 

## Installation

```bash
pip install prrr
```

## Usage

### initialize your project
```shell
prrr init
```

### Generate PR
```shell
prrr pr gen
```

Use a pinch of personality
```shell
prrr pr gen --tone creative
```

## Help

```bash
 Usage: prrr [OPTIONS] COMMAND [ARGS]...                                                                                                                                         
                                                                                                                                                                                
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --help                                                       Show this message and exit.                                                                                     │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ init                                                                                                                                                                         │
│ pr                             Generate a Pull Request                                                                                                                       │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```
