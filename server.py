from fastapi import FastAPI
from pydantic import BaseModel
import openai, os
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()
app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"])
openai.api_key=os.getenv("OPENAI_API_KEY")

class Msg(BaseModel):
    message:str

@app.post("/chat")
async def chat(m:Msg):
    r=openai.chat.completions.create(model="gpt-4o-mini",messages=[{"role":"user","content":m.message}])
    return {"reply":r.choices[0].message["content"]}
