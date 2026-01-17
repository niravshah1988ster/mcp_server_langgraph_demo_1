from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Weather")

@mcp.tool()
async def get_weather(location:str)->str:
    """Get the weather for a given location.
    
    Args:
        location: The name of the location to get weather for (e.g., "California", "New York")
    
    Returns:
        A string describing the weather at the specified location
    """
    return "It's always raining in California"

if __name__=="__main__":
    mcp.run(transport="streamable-http")
