from mcp.server.fastmcp import FastMCP
import tools

mcp = FastMCP("host info mcp")
mcp.add_tool(tools.get_host_info)

@mcp.tool()
def foo():
    return ""

def main():
    print("hello from ai mcp")



if __name__ == '__main__':
    main()