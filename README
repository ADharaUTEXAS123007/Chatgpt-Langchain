In this repository, I have some the Langchain/LlmaIndex work
I am also working on making an AI agent for Indian agriculture 
--- Conversational AI about Indian Agriculture
    Folder : argiculture chat
    Run : pipenv run python main.py

    Example Output

    ╭─ system ─────────────────────────────────────────────────────────────────────────────────────────────────╮
│  You are an AI that has access to a SQLite database.                                                     │
│  The database has tables of : Agriculture                                                                │
│  Do not make any assumptions what tables existor what columns exist. Instead use the 'describe_tables'   │
│  function                                                                                                │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────╯

╭─ human ────────────────────────────────╮                                                                  
│What is RICE_PRODUCTION OF Dist Burdwan?│                                                                  
╰────────────────────────────────────────╯                                                                  

╭─ ai ────────────────────────────────────╮                                                                 
│describe_tables({"__arg1":"Agriculture"})│                                                                 
╰─────────────────────────────────────────╯                                                                 

╭─ function ─────────────────╮                                                                              
│CREATE TABLE "Agriculture" (│                                                                              
│"Dist_Code" INTEGER,        │                                                                              
│  "Year" INTEGER,           │                                                                              
│  "Code" INTEGER,           │                                                                              
│  "State" TEXT,             │                                                                              
│  "Dist" TEXT,              │                                                                              
│  "RICE_AREA" REAL,         │                                                                              
│  "RICE_PRODUCTION" REAL,   │                                                                              
│  "RICE_YIELD" REAL,        │                                                                              
│  "WHEAT_AREA" REAL,        │                                                                              
│  "WHEAT_PRODUCTION" REAL,  │                                                                              
│  "WHEAT_YIELD" REAL        │                                                                              
│)                           │                                                                              
╰────────────────────────────╯                                                                              

╭─ ai ─────────────────────────────────────────────────────────────────────────────────────╮                
│run_sqlite_query({"query":"SELECT RICE_PRODUCTION FROM Agriculture WHERE Dist='Burdwan'"})│                
╰──────────────────────────────────────────────────────────────────────────────────────────╯                

╭─ function─╮                                                                                               
│[[1597.43]]│   
╰───────────╯    

---Conversational chat after uploading a pdf on agriculture like plant diseases, crop yields, etc.-----

Below a pdf titled "Panama disease" was uploaded. A Conversational Agent was defined to answer your questions on the pdf.
The code for this is in the pdf folder.

Here is a screenshot

![Alt text](./images/image.png)


