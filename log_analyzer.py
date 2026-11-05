
from collections import Counter

# Location of our log file
log_file = "logs/server.log"

# Store the log levels
log_counts = Counter()

# Read and analyse the log file
with open(log_file, "r") as file:
    for line in file:
        if "ERROR" in line:
            log_counts["ERROR"] += 1
        elif "WARNING" in line:
            log_counts["WARNING"] += 1
        elif "INFO" in line:
            log_counts["INFO"] += 1

# Display the results
print("===== LINUX LOG ANALYSIS REPORT =====")
print("INFO messages:", log_counts["INFO"])
print("WARNING messages:", log_counts["WARNING"])
print("ERROR messages:", log_counts["ERROR"])
print("Total log entries:", sum(log_counts.values()))
