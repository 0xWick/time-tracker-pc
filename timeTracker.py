import time
import pygetwindow as gw

# Initialize variables
current_window = None
start_time = None
app_data = {}

def track_app_time():
    global current_window, start_time

    while True:
        new_window = gw.getActiveWindow()

        if new_window != current_window:
            # Calculate the time spent on the previous window
            if current_window is not None:
                end_time = time.time()
                elapsed_time = end_time - start_time
                app_name = current_window.title

                if app_name in app_data:
                    app_data[app_name] += elapsed_time
                else:
                    app_data[app_name] = elapsed_time

                # Save the data to TrackRecords.txt
                with open("TrackRecords.txt", "a") as file:
                    current_datetime = time.strftime("%Y-%m-%d %H:%M:%S")
                    file.write(f"{current_datetime} - Time spent on {app_name}: {elapsed_time:.2f} seconds\n")

            # Update current window and start time
            current_window = new_window
            start_time = time.time()

        time.sleep(1)  # Check the active window every 1 second

if __name__ == "__main__":
    try:
        track_app_time()
    except KeyboardInterrupt:
        # Print the final app usage data when the script is terminated
        for app, time_spent in app_data.items():
            print(f"Total time spent on {app}: {time_spent:.2f} seconds")
