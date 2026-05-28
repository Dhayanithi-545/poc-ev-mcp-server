from mcp.server.fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("Montra EV Diagnostics Server")

vehicle_database = {
    "TN-EV-204": {
        "battery_health": 82,
        "motor_temp": 67,
        "range_km": 142,
        "charge_cycles": 320,
    },
    "TN-EV-305": {
        "battery_health": 91,
        "motor_temp": 58,
        "range_km": 167,
        "charge_cycles": 190,
    },
}

#resource
@mcp.resource("vehicle://{vehicle_id}")
def get_vehicle_data(vehicle_id: str) -> str:
    """
    Returns vehicle telemetry
    """

    vehicle = vehicle_database.get(vehicle_id)

    if not vehicle:
        return f"No data found for {vehicle_id}"

    return str(vehicle)

# @mcp.tool()
# def analyze_vehicle_health(
#     battery_health: int,
#     motor_temp: int,
#     range_km: int
# ) -> str:
#     """
#     Analyze vehicle health
#     """

#     issues = []

#     if battery_health < 85:
#         issues.append("Battery health is below optimal.")

#     if motor_temp > 65:
#         issues.append("Motor temperature is high.")

#     if range_km < 150:
#         issues.append("Vehicle range performance is low.")

#     if not issues:
#         return "Vehicle health looks good."

#     return " | ".join(issues)


#  # PROMPT

# @mcp.tool()
# def check_vehicle_health(vehicle_id: str) -> str:
#     """
#     Check vehicle health automatically
#     """

#     mock_vehicle_data = {
#         "TN-EV-204": {
#             "battery_health": 82,
#             "motor_temp": 67,
#             "range_km": 142,
#             "charge_cycles": 320,
#         },
#         "TN-EV-305": {
#             "battery_health": 91,
#             "motor_temp": 58,
#             "range_km": 167,
#             "charge_cycles": 190,
#         },
#     }

#     vehicle = mock_vehicle_data.get(vehicle_id)

#     if not vehicle:
#         return f"No data found for vehicle {vehicle_id}"

#     battery_health = vehicle["battery_health"]
#     motor_temp = vehicle["motor_temp"]
#     range_km = vehicle["range_km"]

#     issues = []

#     if battery_health < 85:
#         issues.append("Battery health is below optimal.")

#     if motor_temp > 65:
#         issues.append("Motor temperature is high.")

#     if range_km < 150:
#         issues.append("Vehicle range performance is low.")

#     if not issues:
#         return f"{vehicle_id} health looks good."

#     return f"{vehicle_id}: " + " | ".join(issues)

@mcp.tool()
def check_vehicle_health(vehicle_id: str) -> str:
    """
    Check vehicle health automatically
    """

    vehicle = vehicle_database.get(vehicle_id)

    if not vehicle:
        return f"No data found for {vehicle_id}"

    battery_health = vehicle["battery_health"]
    motor_temp = vehicle["motor_temp"]
    range_km = vehicle["range_km"]

    issues = []

    if battery_health < 85:
        issues.append("Battery health is below optimal.")

    if motor_temp > 65:
        issues.append("Motor temperature is high.")

    if range_km < 150:
        issues.append("Vehicle range performance is low.")

    if not issues:
        return f"{vehicle_id} health looks good."

    return f"{vehicle_id}: " + " | ".join(issues)

@mcp.prompt()
def diagnostic_summary_prompt(vehicle_id: str) -> str:
    """
    Diagnostic summary template
    """

    return f"""
    Generate a professional diagnostic report
    for vehicle {vehicle_id}.

    Include:
    1. Battery Health
    2. Motor Temperature
    3. Range Performance
    4. Risk Level
    5. Maintenance Recommendation
    """


 # RUN SERVER

if __name__ == "__main__":
    print("Starting Montra EV MCP Server...")
    mcp.run()