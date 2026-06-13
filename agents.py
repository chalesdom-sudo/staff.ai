class RouterAgent:
    """Decides which agent handles the query"""
    def route(self, query: str) -> str:
        return "RetrieverAgent" if "policy" in query.lower() else "GeneratorAgent"

# RetrieverAgent + GeneratorAgent coming next commit
