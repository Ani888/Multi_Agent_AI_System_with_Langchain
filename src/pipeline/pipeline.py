# combine all the agents here in pipeline

from src.agents.agents  import build_search_agent, build_reader_agent, writer_chain, critic_chain

def run_research_pipeline(topic : str) -> dict :
        state = {} # creating state memory (tempory memory) after agent succssfully executed memory is relaesed

        #step 1 : search agent working
        print("\n"+"="*50)
        print("step 1 - search agent is working ...")
        print("="*50)

        search_agent = build_search_agent()
        search_result = search_agent.invoke({
                "messages" : [("user",
                              f"Find recent, reloable and detailed information about: {topic}")]
        })

        state["search_result"] =search_result['messages'][-1].content

        print("\n search result ", state ['search_result'])


        # step 2 :  reader agent
        print("\n"+"="*50)
        print("step 2 - Reader agent is scraping top resources ...")
        print("="*50)

        reader_agent = build_reader_agent()
        reader_result = reader_agent.invoke({
                "messages" : [( "user",
                        f"Baased on the following search result about '{topic}', "
                        f"pick the most relevant URL and scrape it for deeper content.\n\n"
                        f"Search result:\n{state['search_result'][:800]}"

                )]
        })

        state['scraped_content'] =reader_result ['messages'][-1].content

        print("\nscraped content : \n",state['scraped_content'])


        #Step 3 : writer chain
        print("\n"+"="*50)
        print("step 3 - Writer is drafting the report ...")
        print("="*50)

        research_combined = (
                f"SEARCH RESULTS : \n {state['search_result']} \n\n"
                f"DETAILED SCRAPED CONTENT: \n {state['scraped_content']}"
        )

        state["report"] = writer_chain.invoke({
                "topic": topic,
                "research" : research_combined
        })

        print("\n Final Report\n", state['report'])

        #Step 4 : critic report
        print("\n"+"="*50)
        print("step 4 - Critic is reviewing the report ...")
        print("="*50)

        state["feedback"] = critic_chain.invoke({
                "report": state['report']
        })

        print("\n Critic Report \n", state['feedback'])

        return state
