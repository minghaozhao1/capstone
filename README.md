# Capstone

This it the repo for Minghao's capstone project. 



# instructions one setup virtual env in accre

1. install virtual env to have an envirment to install other packages on Accre

<img width="833" alt="Screen Shot 2023-04-15 at 7 53 06 PM" src="https://user-images.githubusercontent.com/89414303/232260393-6b7b0b49-d079-4a10-951e-6a4159dd60ae.png">


2. In the installed virtaul env, install python package nodeenv 

follow instruction on https://pypi.org/project/nodeenv/ to install nodeenv 

3. install nvm 

`curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.2/install.sh | bash`  
`chmod +x ~/.nvm/nvm.sh`   
`source ~/.bashrc`  
`nvm install 16`  
(if it alerts you about unsetting config, please follow to do so)  
after unset  
`nvm use 16`  
now you have node and npm successfully installed in this virtual enviroment.   

4. install all the necessay packages needed for this project under the python venv, etc Bio, json. 

# Intro

This project aims to assist ZJYang Lab in parsing simulation-generated data stored in Accre. Currently, the data is stored in a raw directory format, with files stored on physical disks, making it challenging to use machine learning approaches effectively. Researchers are required to manually collect the data they need, resulting in time-consuming searching processes. The goal of this project is to streamline and automate the data retrieval process, eliminating redundancy and reducing the time and effort required for researchers to access the required data.

# Solution

In this project, an automated process will be implemented to collect data from the current file structure. The data to be used as search keys will be parsed individually and converted into String format, while other data intended for machine learning will be in binary format. The project will then return the relative path of the file, facilitating efficient data retrieval and processing.

# Goal
The objective of this project is to utilize computational tools to streamline data processing, making it more accessible and convenient. This will allow for greater flexibility and openness, facilitating the sharing of simulation data with a broader community of researchers.
