import time

class llm_mockup():
    """A mockup class for simulating LLM model in the absence of the actual model."""
    
    def __init__(self, timeout=3):
        self.timeout = timeout

    def predict_mockup(self, query):
        """ Mockup function to simulate the predict function of the LLM model."""
        
        print("Retrieval step...")
        retrieved_docs  = self.rag_retrieval(query)
        
        print("Predicting...")
        answer = self.llm_generation(retrieved_docs, query)
        
        return answer
    
    def rag_retrieval(self, query, search_type="similarity", num_results=5):
        """ Mockup function to simulate the retrieval step of the LLM model."""
        print(f"Retrieval step with search type {search_type} and number of results {num_results}...")
        
        time.sleep(self.timeout)
        
        mock_results = [f"document_{i}" for i in range(num_results)]
        return mock_results
    
    def llm_generation(self, context, query):
        """ Mockup function to simulate the generation step of the LLM model."""
        print("Generating answer...")
        time.sleep(self.timeout)
        return "This is a mockup answer."