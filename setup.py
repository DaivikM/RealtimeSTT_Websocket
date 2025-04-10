'''
The setup.py file is essential part of the packaging and
distributing python projects. It is used by setuptools
(or distutils in older Python versions) to define the configuration
of your poject, such as its metadata, dependencies and more.
'''

from setuptools import setup, find_packages
from typing import List

def get_requiements()->List[str]:
    '''
    This function will return a list of requirements
    
    '''
    requirement_lst:List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            # Read lines from the file
            lines = file.readlines()
            # Process each line
            for line in lines:
                requirement = line.strip()
                # Ignore only lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print('No requirements.txt file found.')

    return requirement_lst

setup(
    name="RealtimeSTT_Websocket",
    version="0.0.1",
    author="Daivik Mohan",
    author_email="dmohandm11@gmail.com",
    description="This project converts speech into text using Hugging Face and Vosk models. It streams audio from the browser microphone via WebSocket for fast, accurate transcription.",
    packages=find_packages(),
    install_requires=get_requiements()
)