from dotenv import load_dotenv
import os
import time
from langchain_cerebras import ChatCerebras
from mcp import StdioServerParameters as Params
import mcp.client.stdio as stdio
from mcp import ClientSession
import asyncio
load_dotenv()

async def call_llm_with_retry(llm, messages, max_retries=3):
    """Call LLM with retry logic for rate limiting"""
    for attempt in range(max_retries):
        try:
            return await llm.ainvoke(messages)
        except Exception as e:
            if "429" in str(e) or "rate" in str(e).lower():
                wait_time = (attempt + 1) * 2
                print(f"Rate limited, waiting {wait_time} seconds...")
                await asyncio.sleep(wait_time)
            else:
                raise e
    raise Exception("Max retries exceeded")

async def run():
    #step 1: file paths
    server_script=os.path.abspath("mcp-server/main.py")
    python_executable=os.path.abspath(".venv/Scripts/python.exe")

    #step 2: initialise the llm
    llm=ChatCerebras(model= "gpt-oss-120b")

     #step 3: launching the parameters
    server_params= Params(command=python_executable, args=[server_script])

    #step 4: connecting to the server

    async with stdio.stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            while True:
                user_query=input("Ask PDF (or exit): ")
                if user_query.lower() in ["exit", "quit"]:
                    break
                try:
                    mcp_response= await session.call_tool("ask_pdf", {"q": user_query})
                    context_text=mcp_response.content[0].text
                    
                    # Create messages for LLM
                    messages = [
                        {"role": "user", "content": f"""Here is a resume:

{context_text}

Based on the resume above, answer this question: {user_query}

Provide a detailed answer using only information from the resume."""}
                    ]
                    
                    ai_response= await call_llm_with_retry(llm, messages)
                    print(f"Bot: {ai_response.content}\n")
                except Exception as e:
                    print(f"Error: {str(e)}\n")
if __name__=="__main__":
   asyncio.run(run())