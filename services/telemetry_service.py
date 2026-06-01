from mock_data.vehicles import vehicle_database


def get_vehicle(vehicle_id: str):
    return vehicle_database.get(vehicle_id)