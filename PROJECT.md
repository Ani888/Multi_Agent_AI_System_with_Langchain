                    tavily     weather api
                        |       |

input--------------> agent (LLM) -----------> output

Multi- agent research assistant a fully autonomous AI system that thinks, searches, reads and writes on its own. Instead of a single AI answering your question from tools, we are deploying a team of specialized intelligent agents that collaborate together to produces a professional research report on any topic you give them. the search agent goes live on the internet and find the most relavant and rect sources. The reader agent then dive into those sources, scraping and extracting meanningful content. The writer agent take all the gathered intelligence and crafts a well-structured, detailed report. And finally critic agent reviews the intire report, scores it and gives feedback just like a senior researcher reviewing ajunior's work. Every single agent is powered by LLM connected through Langchain's modern LCEL pipeline, and orchestration a shared memory syetem that makes them work as one unified brain.

LCEL : langchain expression language

![alt text](<Screenshot 2026-09-29 at 2.53.15 AM.png>)

in pic
1st agent ---------> tool 1 : tavily api : real time search operation over the internet
and save in state memory (same db)
2nd agents --------> tool2 : it will take all the url from tool1 and it will extract (scraping through BeautifulSoup (a tool to extact or read from the url)) the information from the url and website
and save in another state memory

writer chain : it we write content which data is extrected by BeautifulSoup
write a draft
and then goes to critic chain and then generate final report

Steps:

1. Environment setup and folder structure
2. create tools
3. create agents
4. create pipeline
5. Run and test

What is problem with single agent?
