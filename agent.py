from tools import run_binwalk, run_strings

def main(firmware_path):
    print(f"\n[+] Analyzing firmware: {firmware_path}\n")
    
    # Run binwalk for extraction and print result location
    try:
        extract_dir, binwalk_output = run_binwalk(firmware_path)
        print(f"[+] Binwalk complete. Extracted contents to: {extract_dir}")
        print("First 20 lines of binwalk output:")
        print('\n'.join(binwalk_output.splitlines()[:20]))
        print(f"\n[+] Full binwalk output saved to: {firmware_path.split('.')[0]}_binwalk.txt")
    except Exception as e:
        print(f"[-] Error with binwalk: {e}")

    # Run strings and print short preview
    try:
        strings_output = run_strings(firmware_path)
        print("[+] Strings complete. Example output:")
        print('\n'.join(strings_output.splitlines()[:20]))
        print(f"\n[+] Full strings output saved to: {firmware_path.split('.')[0]}_strings.txt")
    except Exception as e:
        print(f"[-] Error with strings: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python agent.py <firmware_binary>")
        sys.exit(1)
    firmware_file = sys.argv[1]
    main(firmware_file)
