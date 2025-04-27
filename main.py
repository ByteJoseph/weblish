from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from dotenv import load_dotenv
from jsmin import jsmin
import os
import google.generativeai as genai
import re
from functools import lru_cache
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"]    
)

load_dotenv()
def get_api_key() -> str:
    try:
        yourkey = os.environ["GOOGLE_API_KEY"]
        return yourkey
    except:
        # read data from .env file
        yourkey = os.getenv("GOOGLE_API_KEY")
        if yourkey != None:
            return yourkey
        else:
            raise Exception(">>> No api key found !!!")
        
genai.configure(api_key=get_api_key())
model = genai.GenerativeModel('gemini-2.0-flash')
@lru_cache
def translate(script):
    genjs = model.generate_content(
        "give only the JavaScript code to do: " + script +
        ": no error. in a single format. No comments. No HTML. No CSS.not as funtion. Make sure there are no bugs. You are a code-generating machine. generate js code blindly"
    )
   # return genjs.text
    match = re.search(r'```javascript\s*(.*?)\s*```', genjs.text, flags=re.DOTALL)
    print(genjs.text)
    if match:
      return jsmin(match.group(1))
    else:
      return "No match found" 

@app.get("/",response_class=PlainTextResponse)
async def index() -> str:
    with open("browser/bridge.js", "r") as file:
        javascript:str = jsmin(file.read())
    return javascript


@app.get("/compile",response_class=PlainTextResponse)
async def compile(script) -> str:
    result = translate(script=script)
    if result != "No match found":
        return result
    else:
        return f"alert('error: {result}');"
    

@app.get("/health",response_class=PlainTextResponse)
async def health() -> str:
    return "Active"
@app.get("/license",response_class=PlainTextResponse)
async def license() -> str:
    with open("LICENSE","r") as license_file:
        license_file=license_file.read()
    return license_file
