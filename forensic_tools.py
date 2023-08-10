import pytsk3
import datetime

# Specify the path to the image file you want to analyze
image_file_path = 'path/to/image.dd'

# Create an Img_Info object to represent the image file
img_info = pytsk3.Img_Info(image_file_path)

# Create a FS_Info object to represent the file system within the image
file_system = pytsk3.FS_Info(img_info)

# Function to convert a Unix timestamp to a human-readable datetime string


def convert_timestamp(ts):
    # Convert the Unix timestamp to a UTC datetime object
    utc_datetime = datetime.datetime.utcfromtimestamp(ts)
    # Format the datetime object as a string in 'YYYY-MM-DD HH:MM:SS' format
    formatted_datetime = utc_datetime.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_datetime

# Function to analyze and print information about a file


def analyze_file(file_info):
    # Print the name of the file (decoded from bytes to UTF-8)
    print('file name: ', file_info.name.name.decode('utf-8'))

    # Print the inode (address) of the file
    print('inode: ', file_info.meta.addr)

    # Print the type of the file (e.g., regular file, directory, etc.)
    print('file_type: ', file_info.meta.type)

    # Print the size of the file in bytes
    print('size: ', file_info.meta.size)

    # Print the access time of the file (converted to a human-readable format)
    print('access time: ', convert_timestamp(file_info.meta.atime))

    # Print the modification time of the file (converted to a human-readable format)
    print('modification time: ', convert_timestamp(file_info.meta.mtime))

    # Print the creation time of the file (converted to a human-readable format)
    print('creation time: ', convert_timestamp(file_info.meta.crtime))

    # Print a separator line for clarity
    print('-', 40)

# The code execution starts here


# Now you can call the 'analyze_file' function on specific files to print their information.
# For example, you can loop through all files in the file system and analyze each one:
for entry in file_system.open_dir(path='/'):
    # Check if the entry is a file
    if entry.info.meta.type == pytsk3.TSK_FS_META_TYPE_REG:
        # Call the analyze_file function to print information about the file
        analyze_file(entry.info)
