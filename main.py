import requests
import time
import os
import random
import threading
from colorama import Fore, init

init(autoreset=True)

# Function to clear screen
def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

# Typing effect for animation
def typing_effect(text, delay=0.02, color=Fore.WHITE):
    for char in text:
        print(color + char, end="", flush=True)
        time.sleep(delay)
    print()

# Animated input with box style
def animated_input_box(prompt_text):
    box_width = len(prompt_text) + 4
    print(Fore.CYAN + "╔" + "═" * box_width + "╗")
    print(Fore.CYAN + f"║  {prompt_text}  ║")
    print(Fore.CYAN + "╚" + "═" * box_width + "╝")
    return input(Fore.GREEN + "➜ ")

# Animated logo display
def display_animated_logo():
    clear_screen()
    logo_lines = [
        ("/$$      /$$ /$$$$$$$        /$$$$$$$  /$$$$$$$  /$$$$$$ /$$   /$$  /$$$$$$  /$$$$$$$$      ", Fore.CYAN),
        ("| $$$    /$$$| $$__  $$      | $$__  $$| $$__  $$|_  $$_/| $$$ | $$ /$$__  $$| $$_____/      ", Fore.CYAN),
        ("| $$$$  /$$$$| $$  \\ $$      | $$  \\ $$| $$  \\ $$  | $$  | $$$$| $$| $$  \\__/| $$            ", Fore.CYAN),
        ("| $$ $$/$$ $$| $$$$$$$/      | $$$$$$$/| $$$$$$$/  | $$  | $$ $$ $$| $$      | $$$$$         ", Fore.CYAN),
        ("| $$  $$$| $$| $$__  $$      | $$____/ | $$__  $$  | $$  | $$  $$$$| $$      | $$__/         ", Fore.CYAN),
        ("| $$\\  $ | $$| $$  \\ $$      | $$      | $$  \\ $$  | $$  | $$\\  $$$| $$    $$| $$            ", Fore.CYAN),
        ("| $$ \\/  | $$| $$  | $$      | $$      | $$  | $$ /$$$$$$| $$ \\  $$|  $$$$$$/| $$$$$$$$      ", Fore.CYAN),
        ("|__/     |__/|__/  |__/      |__/      |__/  |__/|______/|__/  \\__/ \\______/ |________/      ", Fore.CYAN),
        ("                                                                                             ", Fore.CYAN),
    ]

    for line, color in logo_lines:
        typing_effect(line, 0.005, color)

    # Displaying details section
    details = [
        ("         ╭───────────────────────── < ~ DETAILS ~  > ─────────────────────────╮", Fore.CYAN),
        ("         │   【•】 YOUR COUNTRY  ➤ INDIA                                      │", Fore.YELLOW),
        ("         │   【•】 YOUR REGION   ➤ BIHAR                                      │", Fore.YELLOW),
        ("         │   【•】 YOUR CITY     ➤ PATNA                                      │", Fore.YELLOW),
        ("         ╰────────────────────────────< ~ DETAILS ~  >────────────────────────╯", Fore.CYAN),
        ("╔═════════════════════════════════════════════════════════════════════════════════════╗", Fore.YELLOW),
        ("║  NAME       : BROKEN-PRINCE        GOD ABBUS                     RAKHNA             ║", Fore.CYAN),
        ("║  GITHUB     : BROKEN PRINCE         AUTOMATED SCRIPT             WORKING            ║", Fore.GREEN),
        ("║  BRAND      : POST CONVO           HATA DIYA                    HAI BILKUL          ║", Fore.CYAN),
        ("║  WHATSAPP   : +917543864229         MESSAGE ME                   GOD ABBUS NO       ║", Fore.GREEN),
        ("╚═════════════════════════════════════════════════════════════════════════════════════╝", Fore.YELLOW),
    ]

    for line, color in details:
        typing_effect(line, 0.01, color)

    typing_effect("             <<━━━━━━━━━━━━━━━━━━⏮️⚓𝘽𝙍𝙊𝙆𝙀𝙉-𝙋𝙍𝙄𝙉𝘾𝙀⚓⏭️━━━━━━━━━━━━━━━━━>>", 0.02, Fore.YELLOW)
    time.sleep(1)

# Function to post comments automatically with multi-threading
def post_comment(token, post_id, commenter_name, comments, delay, proxy_list):
    x, failed_attempts = 0, 0

    while True:
        try:
            time.sleep(delay + random.uniform(1, 3))

            comment_text = comments[x].strip()
            comment_with_name = f"{commenter_name}: {comment_text}"

            proxy = random.choice(proxy_list) if proxy_list else None
            proxies = {"http": proxy, "https": proxy} if proxy else None

            data = {'message': comment_with_name, 'access_token': token}
            response = requests.post(f'https://graph.facebook.com/{post_id}/comments/', data=data, proxies=proxies).json()

            if 'id' in response:
                print(Fore.GREEN + f"[✔] Comment Sent Successfully: {comment_with_name}")
            else:
                failed_attempts += 1
                print(Fore.RED + f"[❌] Failed to post comment {failed_attempts}: {comment_with_name}")
                print(Fore.RED + f"[❌] Response: {response}")

            x = (x + 1) % len(comments)

        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"[!] Network Error: {e}")
            time.sleep(5)
            continue

# Function to run multiple threads for faster commenting
def run_multi_threaded(token, post_id, commenter_name, comments, delay, proxy_list, num_threads):
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=post_comment, args=(token, post_id, commenter_name, comments, delay, proxy_list))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

# Main function
def main():
    display_animated_logo()
    print(Fore.GREEN + "[✔] Facebook Auto Commenter (Token-Based)\n")

    token = animated_input_box("ENTER YOUR FACEBOOK TOKEN")
    post_id = animated_input_box("ENTER POST ID")
    commenter_name = animated_input_box("ENTER YOUR NAME")
    delay = int(animated_input_box("ENTER DELAY IN SECONDS"))
    comment_file_path = animated_input_box("ENTER YOUR COMMENT FILE PATH")
    num_threads = int(animated_input_box("ENTER NUMBER OF THREADS (1-5)"))

    use_proxies = animated_input_box("DO YOU WANT TO USE PROXIES? (yes/no)").strip().lower()
    proxy_list = []
    
    if use_proxies == "yes":
        proxy_file = animated_input_box("ENTER PROXY FILE PATH")
        try:
            with open(proxy_file, 'r') as file:
                proxy_list = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print(Fore.RED + "[❌] Error: Proxy file not found!")
            return

    try:
        with open(comment_file_path, 'r') as file:
            comments = file.readlines()
    except FileNotFoundError:
        print(Fore.RED + "[❌] Error: Comment file not found!")
        return

    run_multi_threaded(token, post_id, commenter_name, comments, delay, proxy_list, num_threads)

# Run the script
if __name__ == "__main__":
    main()
