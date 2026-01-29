from mcp.server.fastmcp import FastMCP
from pypdf import PdfReader
import os

mcp=FastMCP("PDF Server")
f=os.path.join(os.path.dirname(__file__),
               "..",
               "Priyanka-resume.pdf")
@mcp.tool()
def ask_pdf(q: str) -> str:
    txt="\n".join(p.extract_text() for p in PdfReader(f).pages)
    if len(txt)<10000:
        return txt
    words=[k.lower() for k in q.lower().split() if len(k)>2]
    matches=[l for l in txt.split("\n") if any(w in l.lower() for w in words)]
    return "\n".join(matches[:20]) if matches else txt[:5000]
if __name__=="__main__":
    mcp.run()