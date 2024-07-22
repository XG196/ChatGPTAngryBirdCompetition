# Team Name

CoT

## Team Members

Guo Xinyu

## Overview

The prompt engineering technique used by the submitted program is the Chain-of-Thoughts prompt. This prompt aims to
describe the detailed ideas that Uppercase English Characters can be formed. Several examples are provided to ChatGpt. 
It is hoped that the ChatGpt can learn the way of thinking to building Uppercase English Characters.

## Instructions

The zipped file is named CoT, after unzipping the CoT package, several folders and files can be found, Here is the 
detaild explanations. The CoT.py is the main file, and it is the entrance to communicate with ChatGpt, modify the 
following line of code, you can instruct ChatGpt generating different Uppercase English Characters:

run_evaluation("CoT", CoTPrompting, num_trials=10, characters=["O"])

The OPENAI_API_KEY is provided in the .env file. The requirements.txt file contains the Python 
packages dependencies which are necessary. The prompts folder contains the prompt file which is CoT.txt.

## How to Run

Include detailed instructions on how to run your program. This may include commands, configurations, or specific steps.

Open the terminal under the folder CoT. Config the Python environment (installing the dependencies). Config the 
Uppercase English Character that you want to generate in the CoT.py file. Run the following command:

python CoT.py

## Dependencies

python-dotenv~=1.0.0
chatgpt4pcg~=1.2.1
