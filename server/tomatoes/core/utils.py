from ..models import SensorData

def get_k_highest_temp_days(sensor_data, k=2):
    results = []
    values = sensor_data
    
    temperatures = list(set(map(
        lambda element: element.get('data', {}).get('temperature', 0),
        values
    )))
    temperatures = sorted(temperatures, reverse=True)
    if len(temperatures) < 2:
        results = []
    else:
        results = list(set(map(lambda item: item["time"].date(), filter(
            lambda item: item.get("data", {}).get('temperature') == temperatures[1],
            values
        ))))
    return results