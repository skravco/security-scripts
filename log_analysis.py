import re
from collections import defaultdict, Counter
import datetime as dt  # Import the datetime module as 'dt' for easier use

class LogAnalyzer:
    def __init__(self, log_paths):
        # Initialize the LogAnalyzer class with a list of log file paths
        self.log_paths = log_paths
        # Create a defaultdict of Counters to store suspicious activities
        self.suspicious_activities = defaultdict(Counter)

    def analyze_logs(self):
        # Iterate through each log file path
        for log_path in self.log_paths:
            # Open the log file for reading
            with open(log_path, 'r') as log_file:
                # Iterate through each line in the log file
                for line in log_file:
                    # Analyze the current line for suspicious activities
                    self._analyze_line(line)
        
        # Report the aggregated suspicious activities
        self._report_suspicious_activities()

    def _analyze_line(self, line):
        # Extract the IP address and timestamp from the log line
        ip_address = self._extract_ip(line)
        timestamp = self._extract_timestamp(line)

        # Check if the line indicates a failed login
        if 'failed login' in line:
            # Increment the failed login count for the IP address
            self.suspicious_activities[ip_address]['failed login'] += 1

        # Check if the line indicates an SQL injection attempt
        if 'SQL injection' in line: 
            # Increment the SQL injection count for the IP address
            self.suspicious_activities[ip_address]['sql_injection'] += 1

        # Check if the line indicates a 404 error (admin scan)
        if '404' in line:
            # Increment the admin scan count for the IP address
            self.suspicious_activities[ip_address]['admin_scan'] += 1

    def _extract_ip(self, line):
        # Use regular expression to extract IP address from the line
        match = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line)
        return match.group() if match else None 

    def _extract_timestamp(self, line):
        # Use regular expression to extract timestamp from the line
        match = re.search(r'\[(.+?)\]', line)
        # Convert the extracted timestamp to a datetime object
        return dt.datetime.strptime(match.group(1), '%d/%b/%Y:%H:%M:%S %z') if match else None

    def _report_suspicious_activities(self):
        # Iterate through each IP address and its associated suspicious activities
        for ip, activities in self.suspicious_activities.items():
            print(f'Suspicious activities from IP {ip}:')  # Use an f-string to format the IP address
            # Iterate through each type of suspicious activity and its count
            for activity, count in activities.items():
                print(f'{activity}: {count} occurrences')

# List of log file paths
log_paths = ['web_server_log.txt', 'auth_log.txt']

# Create an instance of LogAnalyzer with the specified log paths
analyzer = LogAnalyzer(log_paths)

# Analyze the logs and report suspicious activities
analyzer.analyze_logs()
