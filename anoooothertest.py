import time
import datetime

# Get the current time in seconds
start_time = time.time()

# Your code or any operations here
time.sleep(10)
# Get the current time again
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Convert elapsed time to a timedelta object
delta = datetime.timedelta(seconds=elapsed_time)

# Extract minutes and seconds from the timedelta object
minutes = delta.seconds // 60
seconds = delta.seconds % 60

# Format the time as MM:SS
elapsed_time_str = '{:02}:{:02}'.format(minutes, seconds)

print("Elapsed time in MM:SS format:", elapsed_time_str)
