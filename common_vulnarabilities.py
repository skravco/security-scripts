import nmap
import requests

# Function to search for CVEs (Common Vulnerabilities and Exposures) related to a given service name


def search_cve(service_name):
    base_url = "https://cve.circl.lu/api/last/"
    params = {
        "type": "service",
        "value": service_name
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Check for HTTP request errors
        cve_data = response.json()   # Parse the JSON response
        return cve_data
    except requests.exceptions.RequestException as e:
        print("Error querying CVE database:", e)
        return None

# Function to perform vulnerability scanning on a target IP address


def vulnerability_scanner(target_ip):
    scanner = nmap.PortScanner()  # Create an instance of the Nmap scanner
    # Perform a version detection scan on ports 1 to 1024
    scanner.scan(target_ip, '1-1024', '-sV')
    result = scanner[target_ip]  # Get scan results for the target IP

    for proto in result.all_protocols():
        print('protocol : %s' % proto)
        lport = result[proto].keys()
        for port in lport:
            service = result[proto][port]['name']
            version = result[proto][port]['version']

            print('port : %s\tState : %s ' %
                  (port, result[proto][port]['state']))
            print('service : %s ' % service)
            print('version : %s ' % version)

            # Search for CVEs related to the detected service
            cve_results = search_cve(service)
            if cve_results:
                print('found vulnerabilities: ')
                for cve in cve_results:
                    print('CVE: %s, CVSS Score: %s' % (cve['id'], cve['cvss']))
            else:
                print('no known vulnerabilities found for this service.')
            print('---- ---- ---- ---- ---- ---- ---- ----')


# Call the vulnerability_scanner function with a target IP address
vulnerability_scanner('127.0.0.1')
