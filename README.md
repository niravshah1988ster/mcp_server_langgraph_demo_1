## This project shows details about how MCP Host (cursor , claude, etc ) used custom created MCP server

### Add uv packages after activating uv virtual environment
uv add -r requirements.txt --active

### To run project :
Terminal_1 (MCP Server with stdio): python mathserver.py
Terminal_2 (MCP Server with http): python weather.py
Terminal_3 (MCP Client uses MCP server) : python client.py 

