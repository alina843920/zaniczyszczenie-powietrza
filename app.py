from flask import Flask, request, jsonify
from views import WeatherPollutionView, ClosestDataView
from client import get_air_quality


app = Flask(__name__)

app.add_url_rule('/data', view_func=WeatherPollutionView.as_view('weather_pollution_view'))
app.add_url_rule('/closest-data', view_func=ClosestDataView.as_view('closest_data_view'))
@app.route('/get_air_quality', methods=['GET'])
def fetch_air_quality():
    city = request.args.get("city", "Warsaw")
    try:
        air_quality_data = get_air_quality(city)
        return jsonify(air_quality_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()
