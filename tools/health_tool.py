from services.telemetry_service import get_vehicle


def check_vehicle_health(vehicle_id: str):
    """
    ALWAYS use this tool to fetch the latest
    real-time vehicle health and telemetry.

    Never assume previous vehicle health values.
    Always call this tool for fresh diagnostics.
    """

    vehicle = get_vehicle(vehicle_id)

    if not vehicle:
        return {
            "error": f"No data found for {vehicle_id}"
        }

    battery_health = vehicle["battery_health"]
    motor_temp = vehicle["motor_temp"]
    range_km = vehicle["range_km"]

    battery_status = "GOOD"
    temperature_status = "NORMAL"
    range_status = "GOOD"

    if battery_health < 85:
        battery_status = "LOW"

    if motor_temp > 65:
        temperature_status = "HIGH"

    if range_km < 150:
        range_status = "LOW"

    service_required = (
        battery_status == "LOW"
        or temperature_status == "HIGH"
        or range_status == "LOW"
    )

    return {
        "vehicle_id": vehicle_id,
        "battery_health": battery_health,
        "battery_status": battery_status,
        "motor_temp": motor_temp,
        "temperature_status": temperature_status,
        "range_km": range_km,
        "range_status": range_status,
        "service_required": service_required
    }