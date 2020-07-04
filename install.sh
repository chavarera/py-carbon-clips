#!/bin/bash
git clone https://github.com/chavarera/py-carbon-clips.git
virtualenv -p python3 venv
source venv/bin/activate
cd py-carbon-clips
pip install -r requirements.txt
