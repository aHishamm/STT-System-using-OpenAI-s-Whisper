### Whisper API Test 
The python script simply uses the Whisper API as the backend and Gradio web app framework as the frontend 

### Prerequisite Packages
```bash
pip install gradio 
pip install git+https://github.com/openai/whisper.git 
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download en_core_web_sm
python -m spacy download xx_ent_wiki_sm
pip install spacy-fastlang
```
ffmpeg should also be installed 
```bash 
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg
```