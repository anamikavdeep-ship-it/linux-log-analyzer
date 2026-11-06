from collections import Counter

def analyze_logs(log_file):
    log_counts = Counter()
    error_messages = []

    with open(log_file, "r") as file:
        for line in file:
            if "ERROR" in line:
                log_counts["ERROR"] += 1
                error_messages.append(line.strip())

            elif "WARNING" in line:
                log_counts["WARNING"] += 1

            elif "INFO" in line:
                log_counts["INFO"] += 1

    return log_counts, error_messages


def main():
    log_file = "logs/server.log"

    log_counts, error_messages = analyze_logs(log_file)

    print("===== LINUX LOG ANALYSIS REPORT =====")
    print("INFO messages:", log_counts["INFO"])
    print("WARNING messages:", log_counts["WARNING"])
    print("ERROR messages:", log_counts["ERROR"])
    print("Total log entries:", sum(log_counts.values()))

    print("\n===== ERROR DETAILS =====")

    for error in error_messages:
        print(error)


if __name__ == "__main__":
    main()