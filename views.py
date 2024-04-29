from flask import jsonify, request
from views import MethodView
from models import WeatherPollutionData
from services import validate_weather_data
from datetime import datetime
import re

data_storage = []

class WeatherPollutionView(MethodView):
    def post(self):
        data = request.json
        timestamp = data["timestamp"]

        if not re.match(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", timestamp):
            raise ValueError("ERROR")

        validate_weather_data(data)

        weather_data = WeatherPollutionData(
            timestamp=timestamp,
            temperature=data["temperature"],
            pressure=data["pressure"],
            humidity=data["humidity"],
        )
        data_storage.append(weather_data)

        return jsonify({"message": "DONE"}), 201


class ClosestDataView(MethodView):
    def get(self):
        requested_time = request.args.get("timestamp")

        if not requested_time:
            return jsonify({"message": "ERROR timestamp"}), 400

        try:
            req_datetime = datetime.strptime(requested_time, "%Y-%m-%dT%H:%M:%S")
        except ValueError:
            return jsonify({"message": "ERROR timestamp"}), 400

        closest_data = min(
            data_storage,
            key=lambda x: abs(req_datetime - datetime.fromisoformat(x.timestamp)),
        )

        return jsonify({
            "timestamp": closest_data.timestamp,
            "temperature": closest_data.temperature,
            "pressure": closest_data.pressure,
            "humidity": closest_data.humidity,
        }), 200
