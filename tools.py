import subprocess
import os

def run_binwalk(filepath):
    """
    Runs 'binwalk -Me' on the given firmware binary.
    Writes binwalk output to '<firmware-filename>_binwalk.txt'.
    Returns:
        extract_dir (str): Directory where binwalk extracted files.
        output (str): Binwalk command output.
    """
    extract_dir = f"_{os.path.basename(filepath)}.extracted"
    output_txt = f"{os.path.splitext(os.path.basename(filepath))[0]}_binwalk.txt"
    
    result = subprocess.run(['binwalk', '-Me', filepath], capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"binwalk failed: {result.stderr.strip()}")

    # Write command output to a file
    with open(output_txt, "w") as f:
        f.write(result.stdout)

    if not os.path.isdir(extract_dir):
        raise Exception(f"Extraction directory {extract_dir} not found after binwalk.")

    return extract_dir, result.stdout

def run_strings(filepath):
    """
    Runs 'strings' on the firmware binary.
    Writes output to '<firmware-filename>_strings.txt'.
    Returns:
        output (str): Strings command output.
    """
    output_txt = f"{os.path.splitext(os.path.basename(filepath))[0]}_strings.txt"

    result = subprocess.run(['strings', filepath], capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"strings failed: {result.stderr.strip()}")

    # Write command output to a file
    with open(output_txt, "w") as f:
        f.write(result.stdout)
    
    return result.stdout
