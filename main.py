from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from dotenv import load_dotenv
from jsmin import jsmin
import os
import google.generativeai as genai
import re
from functools import lru_cache


app=FastAPI()
load_dotenv()
def api_key() -> str:
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
        
genai.configure(api_key=api_key())
model = genai.GenerativeModel('gemini-1.5-flash')

@lru_cache(maxsize=1000)
def translate(script):
    genjs = model.generate_content("give only the javascript code with no bug to do:"+script+": in single file.no comments.no html.no css")
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
        translate.cache_clear()
        return "reached gemini api limit"
    

@app.get("/health",response_class=PlainTextResponse)
async def health() -> str:
    return "Active"
