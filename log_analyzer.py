
from collections import Counter

# Location of our log file
log_file = "logs/server.log"

# Store the log levels
log_counts = Counter()
error_messages = []

# Read and analyse the log file
with open(log_file, "r") as file:
    for line in file:
        if "ERROR" in line:
            log_counts["ERROR"] += 1
            error_messages.append(line.strip())
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
print("\n===== ERROR DETAILS =====")

for error in error_messages:
    print(error)
