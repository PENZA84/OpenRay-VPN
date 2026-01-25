#!/usr/bin/env python3
import json
import os
import sys
import re
from typing import Set

# Import from src package
import src.constants as C
from src.io_ops import read_lines
from src.parsing import extract_host

def main():
    print("=== OpenRay History Cleanup ===")
    
    if not os.path.exists(C.AVAILABLE_FILE):
        print(f"Error: {C.AVAILABLE_FILE} not found.")
        return

    print(f"Reading existing proxies from {C.AVAILABLE_FILE}...")
    current_proxies = set(read_lines(C.AVAILABLE_FILE))
    print(f"Found {len(current_proxies)} current valid proxies.")
    
    # 1. Clean check_counts.json
    CHECK_COUNTS_FILE = os.path.join(C.STATE_DIR, 'check_counts.json')
    if os.path.exists(CHECK_COUNTS_FILE):
        print(f"Cleaning {CHECK_COUNTS_FILE}...")
        try:
            with open(CHECK_COUNTS_FILE, 'r', encoding='utf-8') as f:
                counts = json.load(f)
            
            old_count = len(counts)
            # Filter counts: keep if proxy URI is in current_proxies
            filtered_counts = {k: v for k, v in counts.items() if k in current_proxies}
            new_count = len(filtered_counts)
            
            with open(CHECK_COUNTS_FILE, 'w', encoding='utf-8') as f:
                json.dump(filtered_counts, f, indent=2)
            
            print(f"  Check counts: {old_count} -> {new_count} entries (Removed {old_count - new_count})")
        except Exception as e:
            print(f"  Error cleaning check counts: {e}")

    print("\nCleanup complete!")

if __name__ == "__main__":
    main()
