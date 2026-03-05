import re

def analyze_log(file_path):
    ip_addresses = {}

    with open(file_path, "r") as file:
        for line in file:
            match = re.search(r"\d+\.\d+\.\d+\.\d+", line)

            if match:
                ip = match.group()

                if ip in ip_addresses:
                    ip_addresses[ip] += 1
                else:
                    ip_addresses[ip] = 1

    print("IP Address Activity:\n")

    for ip, count in ip_addresses.items():
        print(f"{ip} appeared {count} times")


if __name__ == "__main__":
    log_file = input("Enter log file path: ")
    analyze_log(log_file)
