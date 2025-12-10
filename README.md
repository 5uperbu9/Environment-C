# Agent-S Evaluation with diffrent scaled language model on Windows–WSL with NVIDIA RTX 4060
## Installation
1. Install VMWare Workstation(Pro)
2. Install python 3.10
2. To install language model with Ollama, run<br>
`ollama pull YOUR_LANGUAGE_MODEL_NAME`
3. To install OSWorld, run<br>
`git clone https://github.com/xlang-ai/OSWorld`
4. To install dependencies, run<br>
`pip install -r requirements.txt`

## Run Agent-S
Firstly, set local llm url in gui_agents\s3\agents\__init__.py and run.
Modify the arguments in run_local.py, then run
```
cd osworld_setup/s3
.\run_local.bat
```

## Evaluation
Modify the arguments in run_judge.py, then run
```
.\run_judge.bat
```
