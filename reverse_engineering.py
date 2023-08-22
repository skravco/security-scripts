import r2pipe

def reverse_engineering(file_path):
    """
    Performs reverse engineering analysis using Radare2.

    Args:
        file_path (str): The path to the binary file.

    Returns:
        None
    """

    # Open the binary with Radare2
    r2 = r2pipe.open(file_path)

    # Analyze the binary
    r2.cmd('aaa')

    # Get a list of functions
    functions = r2.cmdj('aflj')

    # Display information about found functions
    print('Functions found:')
    for function in functions:
        print(f"Address: {function['offset']} - Name: {function['name']}")

    # Specify a function name for disassembly
    function_name = 'main'
    print(f'\nDisassembly of {function_name}:')
    print(r2.cmd(f'pdf @ {function_name}'))

    # Quit Radare2
    r2.quit()

# Path to the binary file for reverse engineering
file_path = 'path/to/binary'
reverse_engineering(file_path)
