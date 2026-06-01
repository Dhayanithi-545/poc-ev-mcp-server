from mcp.server.fastmcp import FastMCP

from resources.vehicle_resource import get_vehicle_data
from tools.health_tool import check_vehicle_health
from tools.maintenance_tool import predict_maintenance
from prompts.diagnostic_prompt import diagnostic_summary_prompt

mcp = FastMCP("Montra EV Diagnostics Server")


@mcp.resource("vehicle://{vehicle_id}")
def vehicle_resource(vehicle_id: str):
    return get_vehicle_data(vehicle_id)


@mcp.tool()
def health_tool(vehicle_id: str):
    return check_vehicle_health(vehicle_id)


@mcp.prompt()
def diagnostic_prompt(vehicle_id: str):
    return diagnostic_summary_prompt(vehicle_id)

@mcp.tool()
def maintenance_tool(vehicle_id: str):
    return predict_maintenance(vehicle_id)


if __name__ == "__main__":
    print("Starting Montra EV MCP Server...")
    mcp.run()