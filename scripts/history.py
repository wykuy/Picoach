import json
from datetime import datetime

def log_workout(total_time, intervals):
    date = datetime.now().strftime('%Y-%m-%d')
    workout = {
        "date": date,
        "intervals_completed": intervals,
        "average_speed": 12.3,  # Dummy speed for now, replace with actual data
        "total_distance": 1500,  # Dummy distance for now, replace with actual data
        "total_time": total_time
    }
    
    try:
        with open('config/history_log.json', 'r') as f:
            history = json.load(f)
    except FileNotFoundError:
        history = []

    history.append(workout)

    with open('config/history_log.json', 'w') as f:
        json.dump(history, f, indent=4)
