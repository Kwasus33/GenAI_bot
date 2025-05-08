# GenAI_bot
Generative AI to assist users in filling out a helpdesk form

## Project Setup
* Used below directory name "GenAI_bot" is project's main directory
1. Get your Gemini API Key from: https://aistudio.google.com/apikey
2. Clone the repository:

   ```bash
   git clone https://github.com/Kwasus33/GenAI_bot.git
   cd GenAI_bot
   ```

3. Create a .env file in "GenAI_bot" directory:
    ```bash
    cd GenAI_bot
    cp .env.example .env
    ```
    Content of .env file would look like this: 
    ```bash
    GEMINI_API_KEY=your_key
    ```
    Change phrase  **'your_key'** to generated Gemini Api Key 

4. You need to add PYTHONPATH environment variable on your system so python will recognize src directory as a module
```bash
# unix
export PYTHONPATH=$PYTHONPATH:path/to/GenAI_bot/src

# windows
$env:PYTHONPATH="$env:PYTHONPATH;path\to\GenAI_bot\src" 
```
Change **path/to/GenAI_bot/src** to your system full path to src module (directory) of this project

## About app
* app can be run with 2 optional arguments:
    * if we run **python3 src/main.py --path "out.json"** - there will be created file out.json with whole chat session (user inputs + llm responses)
    * if we run **python3 src/main.py --path "out.json" --length 10** - there will be created file out.json with last 10 interactions from chat session (user inputs + llm responses)
        
* usage: main.py [-h] [--path PATH] [--length LENGTH]

Chatbot Helpdesk AI: Start a chat session and optionally save it to a file.

options:
-h, --help       show this help message and exit
--path PATH      Path to json file to store chat session
--length LENGTH  Length of saved to file chat session

* When you run the app, chat session starts - u need to talk to that chatbot and answer it's questions to successfully fill in a given form. When all fields are filled in you will see thanks and session with chatbot will end.

## Setting up environment and running app locally on Unix
* if you don't have installed python3.12, do it, then type:

```bash
cd GenAI_bot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 src/main.py (arguments described above can be added)
```

## Setting up docker environment and running app in container

```bash
(run docker app in the background)
cd GenAI_bot 
docker build -t helpdesk-ai . 
docker run --env-file .env -it helpdesk-ai

# change "CMD ["python", "src/main.py", "--path", "results.json"]" to "CMD ["python", "src/main.py"]" 
# in Dockerfile if you don't want to have full chat session logged
 
# change "CMD ["python", "src/main.py", "--path", "results.json"]" to "CMD ["python", "src/main.py", "--path", "results.json", "--length", 10]" 
# in Dockerfile if want to have last 10 logs of chat session
```

## Running tests locally (need to have PATHONPATH variable exported)
```bash
cd GenAI_bot 
pytest tests/*
```
