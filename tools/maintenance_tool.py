from services.telemetry_service import get_vehicle


def predict_maintenance(vehicle_id: str):
    """
    Predict maintenance risk level
    based on latest telemetry.
    """

    vehicle = get_vehicle(vehicle_id)

    if not vehicle:
        return {
            "error": f"No data found for {vehicle_id}"
        }

    battery_health = vehicle["battery_health"]
    motor_temp = vehicle["motor_temp"]
    charge_cycles = vehicle["charge_cycles"]

    risk_score = 0

    # Battery health check
    if battery_health < 85:
        risk_score += 1

    # Temperature check
    if motor_temp > 65:
        risk_score += 1

    # Charge cycle aging
    if charge_cycles > 300:
        risk_score += 1

    if risk_score == 0:
        risk_level = "LOW"
        recommendation = "No maintenance needed."

    elif risk_score == 1:
        risk_level = "MEDIUM"
        recommendation = "Schedule vehicle inspection."

    else:
        risk_level = "HIGH"
        recommendation = "Immediate maintenance recommended."

    return {
        "vehicle_id": vehicle_id,
        "risk_level": risk_level,
        "recommendation": recommendation,
        "risk_score": risk_score
    }
