# dr-penguin
A Line bot AI assistant integrated with LangChain, OpenAI API, DALL-E 3

## Overview
### Linebot Demo
<img src="https://raw.githubusercontent.com/alan10607/dr-penguin/doc/pic/readme8.jpg" width="250"/>
<style>
  table {
    width: 100%;
  }
  td:nth-child(1) {
    width: 30%;
  }
  td:nth-child(2) {
    width: 30%;
  }
  td:nth-child(3) {
    width: 40%;
  }
</style>

| Function | Description | Demo |
|---|---|---|
| Self Introduction | Assistant follows instructions to introduce itself | <img src="https://raw.githubusercontent.com/alan10607/dr-penguin/doc/pic/readme1.jpg" width="300"/> |
| History Memory | Assistant remembers conversations and responds based on chat history | <img src="https://raw.githubusercontent.com/alan10607/dr-penguin/doc/pic/readme2.jpg" width="300"/> |
| Tool - Google Search <br><br> *Use SerpAPI to google search current event or something unknown* | Google search to obtain accurate weather and perform calculations | <img src="https://raw.githubusercontent.com/alan10607/dr-penguin/doc/pic/readme3.jpg" width="300"/> |
| | Inquire about good restaurants nearby | <img src="https://raw.githubusercontent.com/alan10607/dr-penguin/doc/pic/readme4.jpg" width="300"/> |
| | Go further, inquire about restaurant ratings and review comments | <img src="https://raw.githubusercontent.com/alan10607/dr-penguin/doc/pic/readme7.jpg" width="300"/> |
| Tool - Image Generator <br><br> *Use DALL-E 3 to generate requested images* | Generate Dr. Penguin's selfie | <img src="https://raw.githubusercontent.com/alan10607/dr-penguin/doc/pic/readme5.jpg" width="300"/> <br>Generated image: <img src="https://raw.githubusercontent.com/alan10607/dr-penguin/doc/pic/readme6.png" width="300"/> |



### OpenAI Assistants API Beta
```
$python src/assistant.py 
```
```
Assistant id:  {assistant_id}
Thread id:  {thread}
Type 'quit' to quit chat
Question >>> hi, who are you
Run status: queued
Run status: in_progress
Run status: in_progress
Run status: completed
Answer >>>  Hello! I'm an AI developed by OpenAI, designed to assist with a wide range of tasks and questions you might have. How can I help you today?
-----------------

Question >>> how is the weather in Taipei                    
Run status: queued
Run status: in_progress
Run status: requires_action
Google search query: current weather in Taipei
Get result: {'type': 'weather_result', 'temperature': '21', 'unit': 'Celsius', 'precipitation': '0%', 'humidity': '55%', 'wind': '19 公里/時', 'location': '台北市', 'date': '星期六 下午5:00', 'weather': '晴'}
google_search:  {'type': 'weather_result', 'temperature': '21', 'unit': 'Celsius', 'precipitation': '0%', 'humidity': '55%', 'wind': '19 公里/時', 'location': '台北市', 'date': '星期六 下午5:00', 'weather': '晴'}
Run status: queued
Run status: in_progress
Run status: in_progress
Run status: completed
Answer >>>  The current weather in Taipei is clear with a temperature of 21 degrees Celsius. There is no precipitation with a humidity level at 55%, and the wind is blowing at 19 kilometers per hour. It's a nice day! If you need more details or a forecast, let me know.
-----------------

Question >>> give me a star night photo
Run status: queued
Run status: in_progress
Run status: requires_action
dalle3_image_generator:  {"query":"star-filled night sky"} => https://oaidalleapiprodscus.blob.core.windows.net/private/org-e53HPrTsrTnUKVEkF4Uxddvu/user-TxgaoFmu9lA9ymVLcjP0TSBE/img-fnhbYEUIUElxEqfR5d636kOF.png?st=2024-01-13T14%3A03%3A08Z&se=2024-01-13T16%3A03%3A08Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-01-13T04%3A39%3A51Z&ske=2024-01-14T04%3A39%3A51Z&sks=b&skv=2021-08-06&sig=QuRGJ%2BB9Lm8/4%2B8/L3Ngx7MllAx9V8nRNQsRrelQgbM%3D
Run status: queued
Run status: in_progress
Run status: in_progress
Run status: completed
Answer >>>  Here is a photo of a star-filled night sky for you:

![Star-filled Night Sky](https://oaidalleapiprodscus.blob.core.windows.net/private/org-e53HPrTsrTnUKVEkF4Uxddvu/user-TxgaoFmu9lA9ymVLcjP0TSBE/img-fnhbYEUIUElxEqfR5d636kOF.png?st=2024-01-13T14%3A03%3A08Z&se=2024-01-13T16%3A03%3A08Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-01-13T04%3A39%3A51Z&ske=2024-01-14T04%3A39%3A51Z&sks=b&skv=2021-08-06&sig=QuRGJ%2BB9Lm8/4%2B8/L3Ngx7MllAx9V8nRNQsRrelQgbM%3D)
-----------------

Question >>> quit
Quit chat...
```

### langchain v0.1.0
```
$ python src/langchain_assistant.py
```
```
Type 'quit' to quit chat
Question >>> hello


> Entering new AgentExecutor chain...
Hello! How can I assist you today?

> Finished chain.
{'input': 'hello', 'output': 'Hello! How can I assist you today?'}
Answer >>>  Hello! How can I assist you today?
-----------------

Question >>> 台北天氣如何


> Entering new AgentExecutor chain...

Invoking: `Google_Search` with `台北天氣`


{'type': 'weather_result', 'temperature': '22', 'unit': 'Celsius', 'precipitation': '0%', 'humidity': '51%', 'wind': '23 公里/時', 'location': '台北市', 'date': '星期六 下午5:00', 'weather': '大致晴朗'}根據最新資訊，台北市目前的天氣狀況是大致晴朗，溫度約為攝氏22度，降雨機率為0%，相對濕度為51%，風速為每小時23公里。請注意天氣可能會有變化，建議您隨時留意天氣預報。

> Finished chain.
{'input': '台北天氣如何', 'output': '根據最新資訊，台北市目前的天氣狀況是大致晴朗，溫度約為攝氏22度，降雨機率為0%，相對濕度為51%，風速為每小時23公里。請注意天氣可能會有變化，建議您隨時留意天氣預報。'}
Answer >>>  根據最新資訊，台北市目前的天氣狀況是大致晴朗，溫度約為攝氏22度，降雨機率為0%，相對濕度為51%，風速為每小時23公里。請注意天氣可能會有變化，建議您隨時留意天氣預報。
-----------------

Question >>> quit
Quit chat...
```


## Troubleshooting
### AWS Layer environment variables 
In Lambda page > Configuration > Environment variables
```
LINE_CHANNEL_ACCESS_TOKEN
LINE_CHANNEL_SECRET
OPENAI_API_KEY
SERPAPI_API_KEY
OPENAI_ASSISTANT_ID
```

### How to create layer?
0. If use Mac M1 chip, need to use docker to build layer in arm64 environment
```
docker pull arm64v8/ubuntu
docker run -it arm64v8/ubuntu

# in docker
root@3e836bc53a63:/# lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 22.04.3 LTS
Release:	22.04
Codename:	jammy
root@3e836bc53a63:/# uname -a
Linux 3e836bc53a63 5.10.76-linuxkit #1 SMP PREEMPT Mon Nov 8 11:22:26 UTC 2021 aarch64 aarch64 aarch64 GNU/Linux
```

1. Install requirements
```
python -m venv aws-lambda
source aws-lambda/bin/activate
pip install -r requirements.txt

deactivate
```
If `pip install multidict` show this error in python3.12 arm64 env
```
Building wheels for collected packages: PyYAML, multidict

...

ERROR: Could not build wheels for multidict, which is required to install pyproject.toml-based projects
```

Try
```
sudo apt-get install python3.12-dev
```

2. Wrap in to zip
File path should be `python/lib/python3.12/site-packages/{install_here}`
```
zip -r my-layer.zip python
```

3. Copy out zip and upload to AWS sebsite
```
docker cp 3e836bc53a63:{path_of_my-layer.zip} {local_path}
```