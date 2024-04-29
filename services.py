def validate_weather_data(data):
    if not -50 <= data["temperature"] <= 50:
        raise ValueError("Temperatura poza zakresem")

    if not 950 <= data["pressure"] <= 1100:
        raise ValueError("Ciśnienie poza zakresem")

    if not 0 <= data["humidity"] <= 100:
        raise ValueError("Wilgotność poza zakresem")
