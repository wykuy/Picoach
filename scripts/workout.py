import time
from history import log_workout

def start_workout(work_time, rest_time, intervals):
    total_time = 0
    for i in range(intervals):
        print(f"Starting interval {i+1}")
        # Simulate workout (replace with actual sensor data)
        time.sleep(work_time)  # Simulate work phase
        print(f"Work phase {i+1} completed. Resting now.")
        time.sleep(rest_time)  # Simulate rest phase
        total_time += (work_time + rest_time)

    log_workout(total_time, intervals)

def log_workout(total_time, intervals):
    # Function to log the completed workout in the history_log.json
    print(f"Workout complete! Total time: {total_time}s, Intervals completed: {intervals}")
    # Here, you could update the history_log.json file
