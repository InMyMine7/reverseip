import requests
import concurrent.futures
import os
import threading

def clear():
    os.system("cls" if os.name == "nt" else "clear")

OUTPUT_FILE = 'result.txt'
MAX_WORKERS = 20
write_lock = threading.Lock() 

def reverse_ip_lookup(ip_or_domain):
    try:
        url = f"https://sexreverseipz.vercel.app/reverse?ip={ip_or_domain}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        domains = data.get("domains", [])
        return ip_or_domain, domains
    except:
        return ip_or_domain, []

def save_result(domains):
    with write_lock:
        with open(OUTPUT_FILE, 'a') as out:
            for domain in domains:
                out.write(domain + '\n')


def get_user_input():
    clear()
    print("=== Reverse IP Lookup ===")
    choice = input("Enter 'f' for input from file or directly enter domain/IP: ").strip().lower()
    
    targets = []
    
    if choice == 'f':
        path = input("Enter the file path (example: input.txt): ").strip()
        if not os.path.exists(path):
            print(f"[!] File '{path}' not found.")
            return []
        with open(path, 'r', encoding='utf-8') as f:
            targets = [line.strip() for line in f if line.strip()]
    else:
        raw = input("Enter a list of domains/IPs (separate with commas/spaces/newlines): \n")
        raw = raw.replace(',', '\n').replace(' ', '\n')
        targets = [line.strip() for line in raw.splitlines() if line.strip()]

    return list(set(targets)) 

def main():
    targets = get_user_input()
    if not targets:
        print("[!] No targets to process.")
        return

    open(OUTPUT_FILE, 'w').close()

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_target = {executor.submit(reverse_ip_lookup, target): target for target in targets}
        for future in concurrent.futures.as_completed(future_to_target):
            target = future_to_target[future]
            try:
                ip, domains = future.result()
                if domains:
                    print(f"[+] {ip} -> {len(domains)} domain(s)")
                    save_result(domains)
                else:
                    print(f"[-] {ip} -> No result")
            except Exception as e:
                print(f"[!] Error for {target}: {e}")

    print(f"\n[✔] Done! The results are saved in '{OUTPUT_FILE}'.")

if __name__ == '__main__':
    main()
