from langchain.tools import StructuredTool
from pydantic.v1 import BaseModel

def write_report(filename, html):
    with open(filename, "w") as f:
        f.write(html)
        
class WriteReportArgs(BaseModel):
    filename: str
    html: str
    
write_report_tool = StructuredTool.from_function(
    func=write_report,
    name="write_report",
    description="Write an HTML file to disk. Use this tool when someone asks for a report.",
    args_schema=WriteReportArgs,
)
