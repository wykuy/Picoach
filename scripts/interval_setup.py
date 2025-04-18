import json

def load_intervals():
    try:
        with open('config/interval_config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"work_time": 30, "rest_time": 15, "intervals": 5}  # Default values

def save_intervals(work_time, rest_time, intervals):
    config = {
        "work_time": work_time,
        "rest_time": rest_time,
        "intervals": intervals
    }
    with open('config/interval_config.json', 'w') as f:
        json.dump(config, f)
