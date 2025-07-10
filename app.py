from gtts import gTTS 
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
import uuid
import os

app = FastAPI()

class ScriptRequest(BaseModel):
    script: str

@app.post("/generate-script")
async def generate_script(request: ScriptRequest):
    try:
        # Generate a unique filename
        filename = f"/tmp/{uuid.uuid4()}.mp3"
        
        # Generate the speech
        tts = gTTS(text=request.script, lang="en", slow=True, tld="com.au")
        tts.save(filename)
        
        # Return the MP3 file
        return FileResponse(filename, media_type="audio/mpeg", filename="speech.mp3")

    except Exception as e:
        return {"error": str(e)}





