from services.telemetry_service import get_vehicle


def get_vehicle_data(vehicle_id: str) -> str:
    vehicle = get_vehicle(vehicle_id)

    if not vehicle:
        return f"No data found for {vehicle_id}"

    return str(vehicle)