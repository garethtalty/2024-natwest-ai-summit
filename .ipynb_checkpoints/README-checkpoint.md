# AI Summit Day 0 Setup

## Steps to test connections:
1. Install VS Code if you haven't already (and don't have another interpreter that you usually use). You can find it here: https://code.visualstudio.com/download
(This can either be completed within the terminal / command prompt in VS Code OR the standalone terminal / command prompt)
2. First clone this repo to your local machine using the command `git clone https://gitlab.com/Fayz-S/2024-natwest-ai-summit.git` in your terminal / cmd (in the folder where you want the repo to be downloaded)
3. Install miniconda (if you haven't already) from https://docs.anaconda.com/free/miniconda/ (be sure to download the correct version for your system)
4. Install the remaining required packages with the command `conda env create -f environment.yml` >>> This will create a new conda environment AND install the required packages for the test
5. Open VS Code (or other terminal) if you haven't already
6. Activate your new envrionment by running `conda activate ai_summit` in the terminal. Ensure that you can see the environment selected in the bottom right of the screen in VS Code. If not, click the environment currently activated and manually switch it to the new environment you've created
7. Take you Open AI API key and copy and paste it into the .env file (replace the current "xxxxxxxx" string)
8. 