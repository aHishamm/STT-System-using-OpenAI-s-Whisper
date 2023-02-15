### Whisper API Test 
The python script simply uses the Whisper API as the backend and Gradio web app framework as the frontend 

### Prerequisite Packages
```bash
pip install gradio 
pip install git+https://github.com/openai/whisper.git 
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
