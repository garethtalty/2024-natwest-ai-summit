# AI Summit Day 0 Setup
Hi! This is the NatWest 2024 AI Summit Repository, containing sample code for creating your use cases.

## Steps to steup the repository:
1. If you don't already have one, install an IDE. We recommend using VS Code (found here: https://code.visualstudio.com/download. Be sure to download the correct version for your operating system).
2. If you don't already have Git, you can install it by following the instructions here: https://github.com/git-guides/install-git. 
3. Only **one** of your team members needs to do this step. Fork this repository by clicking the fork button at the top right of this webpage. This will create a copy that your team can use and edit as desired.
4. Each team member should now be able  to clone the forked repository by running "git clone <forked_repo_link>" on your local machine using Git bash or your MacOS/Linux terminal - the link can be found on the top right hand side of your forked repo page, under the blue "code" button. This will create a local version of the repository on your device.  
5. We strongly recommend using an environments manager such as Pyenv or miniconda for the project. However, if you'd prefer not to or are having difficulty setting this one up, you can skip steps 6-11:

**For Pyenv (recommended for more experienced users with Linux, WSL or MacOS)**:
6.  Install pyenv - instructions can be found here:  https://realpython.com/intro-to-pyenv/.
7.  Ensure that the following lines of code are copied into your .bashrc file (Linux), .zshrc file (MacOS). 
```
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```
8. Install Python 3.12 by running `pyenv install -v 3.12` (if you haven't already).
9. Create the pyenv environment by running `pyenv virtualenv 3.12 <environment_name>`.
10. Navigate to your cloned repository and run `pyenv local <environment_name>`. This will ensure the environment is activated whenever you navigate into this folder.
11. Install the requirements for the repo by running `pip install -r requirements.txt`. 

**For Miniconda**
1. Install miniconda from https://docs.anaconda.com/free/miniconda/ (be sure to download the correct version for your operating system). If you have minconda already, ensure it is up to date by running `conda update -n base -c defaults conda`. This should cause `(base)` to appear behind your file location on CLI, meaning conda has been installed and is active.
2. For the following steps you will need to open a command line interface (CLI). This will differ depending on your operating system:
   * Windows: Powershell (4.0)
   * MacOS & Linux: Terminal

Note that your CLI can also be opened via most IDE's. including VS Code.

8. Install the remaining required packages by running the following command in your CLI `conda env create -f environment.yml` >>> This will create a new conda environment AND install the required packages to run this repo.
9. Open VS Code (or other IDE) if you haven't already.
10. Activate your new envrionment by running `conda activate ai_summit` in your CLI. If using VS Code, you shouyld be able to see the environment selected in the bottom right of the screen in VS Code. If not, click the environment currently activated and manually switch it to the new environment you've created.

Once you have your environment setup, you should now test the OpenAI Connection:

12. Take your Open AI API key and copy and paste it into the .env file, replacing the current default value.
13. Open the "OpenAI_test.ipynb" file and run the whole notebook. 

Finally, you should test the Streamlit application:
14. Navigate to the streamlit folder in your CLI and run `streamlit run Home.py`. This should open the sample streamlit application. From here, you can check that the functionality works and do an OpenAI connection test as well using the OpenAI Chatbot page.

That should be you set up. Happy hacking!!

## Notes
### Conda environment setup issues
If you have issues using the environment.yml file to creaet your conda environment, try these steps instead in your CLI:

1. Create the environment on it's own by running `conda env create -n ai_summit_env`.
2. Activate your environment by running `conda activate ai_summit_env`. This should cause `(ai_summit_env)` to appear behind your file location on CLI, meaning the environment is active.
3. Install pip into your custom environment by running `conda install pip`.
4. Install the necessary packages by navigating to your cloned repo and running `pip install -r requirements.txt`. 
5. The environment should now be setup and ready for you to use. Continue from step 12.


# Useful Resources

