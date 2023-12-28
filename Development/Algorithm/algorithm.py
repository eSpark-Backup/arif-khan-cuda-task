import subprocess
import os

# Function to convert hexadecimal to decimal
def hex_to_dec(hex_str):
    return int(hex_str, 16)

# Function to add two hexadecimal numbers
def add_hex(hex_str, increment):
    return hex(hex_to_dec(hex_str) + hex_to_dec(increment))[2:]

# Function to run the keymath command and update the value
def run_keymath_command(decimal_value):
    command = "./keymath 022fa281fbfdba59cf9ce2c584866fc627ce9682dc9a4fa80a32730b7ebf193476 - {}".format(decimal_value)
    print(command)
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Check if the command was successful
    if result.returncode == 0:
        lines = result.stdout.strip().split('\n')
        
        # Check if there are at least two lines in the output
        if len(lines) >= 2:
            result_hex = lines[1].split(":")[1].strip()
            return result_hex

    # If the command fails or the output format is unexpected, return None
    return None

# Function to save result to data.txt
def save_to_data_txt(result_hex, decimal_value):
    try:
        file_path = os.path.join(os.getcwd(), "data.txt")
        with open(file_path, "a") as file:
            hex_value = hex(decimal_value)
            file.write(f"{result_hex} # - {hex_value}\n")
    except Exception as e:
        print(f"Error saving to data.txt: {e}")

# Main loop
start_value = "200000000001000000000000000000000"
end_value = "3ffffffffff000000000000000000000"

current_value = start_value

while current_value != end_value:
    # Convert current_value to decimal before using it in the keymath command
    decimal_value = hex_to_dec(current_value)

    # Run keymath command
    result_hex = run_keymath_command(decimal_value)

    if result_hex is not None:
        # Extract 66-character hex result
        result_hex = result_hex.strip()

        # Save to data.txt
        save_to_data_txt(result_hex, decimal_value)
    else:
        print(f"Error running keymath command for value: {current_value}")

    # Update value for the next iteration
    current_value = add_hex(current_value, "1000000000000000000000")  # Add 2^80 in hexadecimal

print("Done.")
