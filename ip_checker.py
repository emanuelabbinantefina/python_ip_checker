"""
IP Traffic Analyzer
Analizza una lista di indirizzi IP e segnala quelli presenti in blacklist.
In un ambiente reale, la blacklist verrebbe caricata da file, database o API.
"""

SUSPICIOUS_IPS = {
    "192.168.1.50",
    "45.33.22.11",
    "10.0.0.99",
    "172.16.5.200"
}

def check_traffic(ip_list: list[str]) -> int:
  
    # Confronta una lista di IP con la blacklist e stampa un report.

    print(f"[*] Avvio analisi traffico di rete su {len(ip_list)} indirizzi...")
    
    blocked_count = 0

    for ip in ip_list:
        if ip in SUSPICIOUS_IPS:
            print(f"[ALERT] Indirizzo IP bloccato o sospetto rilevato: {ip}")
            blocked_count += 1
        else:
            print(f"[PASS] Traffico regolare dall'IP: {ip}")

    print(f"\n[RAPPORTO] Analisi completata. Trovati {blocked_count} eventi di sicurezza.")
    return blocked_count


if __name__ == "__main__":
    # Traffico di test per simulare un caso reale
    current_traffic = [
        "127.0.0.1",      # Localhost
        "45.33.22.11",    # Blacklist
        "192.168.1.1",    # Gateway locale
        "8.8.8.8",        # DNS Google
        "10.0.0.99"       # Blacklist
    ]

    check_traffic(current_traffic)
