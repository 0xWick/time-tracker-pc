# time-tracker-pc

A simple Python script to track how much time you spend on different applications.

## How to Use:

### Prerequisites:

Make sure you have Python installed.

### Setup:

1. Create a virtual environment (optional but recommended):

```
python -m venv myEnv
```


2. Activate the virtual environment:

- On Windows:

  ```
  myEnv\Scripts\activate
  ```

- On macOS and Linux:

  ```
  source myEnv/bin/activate
  ```

### Running the Script:

1. Clone this repository or download the Python script (`time_tracker.py`) to your computer.

2. Navigate to the directory where you saved `time_tracker.py` in your terminal.

3. Run the script using Python:

```
python time_tracker.py
```


4. The script will start tracking the time spent on each application you use. It will update in real-time as you switch between applications.

### Stopping the Script:

- To stop the script, press `Ctrl + C` in the terminal.

### Viewing the Tracked Data:

The script will record the time spent on each application in a file named "TrackRecords.txt" in the same directory where the script is located. Each entry in the file includes the current date and time, as well as the time spent on the application.

You can open "TrackRecords.txt" to view your application usage history.

### TODO List:

- [ ] Start on PC Startup
- [ ] Run In Background
- [x] Barebone UI in Electron or a Simpler Way (Python)
- [ ] Add data analysis and visualization features
- [x] Implement data persistence between script runs
- [ ] Add a Database

### Important Notes:

- This script monitors active windows, so it may not work perfectly on all systems due to differences in window management between operating systems.

- The script does not persist data between runs. It appends data to the "TrackRecords.txt" file, so make sure to save or analyze the data as needed before running the script again.

- Ensure that you have the necessary permissions to write to the directory where the script is located to save the tracking data.

- To analyze the data further or create visualizations, you can import the data from "TrackRecords.txt" into a spreadsheet or use data analysis tools.
