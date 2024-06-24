**Description**  
Speech Analysis Dashboard created using OpenAI whisper and Ollama.The dashboard analyzes an audio input and produces a transcription of the Audio.   
Additionally, sentiment analysis is done using a transformer model(distilbert).  
Ollama is used to generate a summary from the transcription as it generate a better summary compared to transformers.  

**Installation Steps**

**Create a virtual environment locally**  
cd path/to/your/project  
python -m venv .env  

Switch to virtual environment =   
In windows - .\env\Scripts\activate  
In macOs / Linux = source env/bin/activate  

**Install Requirements**  
pip install -r requirements.txt  

**Run application** 
python app.py  

**Screenshot of Interface**  
![Screenshot 2024-06-21 232836](https://github.com/subinyounas/Speech-Analysis/assets/75063342/289f9c55-85e1-485e-86d3-6e8688797d78)
