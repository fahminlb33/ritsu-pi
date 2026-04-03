import json
import os
import sys
import urllib.request
import urllib.error

def manage_dns_record():
    # 1. Configuration from environment variables
    api_token = os.environ.get("CLOUDFLARE_API_TOKEN")
    zone_id = os.environ.get("CLOUDFLARE_ZONE_ID")
    host = os.environ.get("CNAME_HOST")
    value = os.environ.get("CNAME_VALUE")
    # New: Default A record IP from env (with a fallback just in case)
    default_a_ip = os.environ.get("DEFAULT_A_IP", "192.0.2.1")

    if not all([api_token, zone_id, host, value]):
        print("Error 1: Missing required environment variables.")
        sys.exit(1)

    base_url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }

    # 2. Logic Pivot: A Record vs CNAME
    # If host and value are identical, manage an A record instead
    is_a_record = (host == value)
    target_type = "A" if is_a_record else "CNAME"
    target_content = default_a_ip if is_a_record else value

    try:
        # 3. Search for existing record of the target type
        search_url = f"{base_url}?type={target_type}&name={host}"
        req = urllib.request.Request(search_url, headers=headers, method="GET")
        
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode())
            records = res_data.get("result", [])

        # 4. Payload Preparation
        payload = {
            "type": target_type,
            "name": host,
            "content": target_content,
            "ttl": 1, 
            "proxied": False  # Proxied set to False
        }
        data = json.dumps(payload).encode("utf-8")

        if records:
            existing = records[0]
            # No Change Check: content must match AND proxied must be False
            if existing.get("content") == target_content and existing.get("proxied") is False:
                print(f"No changes required: {host} is already {target_content} (DNS Only).")
                sys.exit(0) 

            print(f"Updating {target_type} record for {host}...")
            final_url = f"{base_url}/{existing['id']}"
            method = "PUT"
        else:
            print(f"Creating new {target_type} record for {host}...")
            final_url = base_url
            method = "POST"

        # 5. Execution
        final_req = urllib.request.Request(final_url, data=data, headers=headers, method=method)
        with urllib.request.urlopen(final_req) as response:
            result = json.loads(response.read().decode())
            if result.get("success"):
                print(f"Success: {target_type} record {method}ed.")
                sys.exit(0)
            else:
                print(f"Error 3: API logic failure: {result.get('errors')}")
                sys.exit(3)

    except urllib.error.HTTPError as e:
        print(f"Error 2: HTTP {e.code}: {e.read().decode()}")
        sys.exit(2)
    except Exception as e:
        print(f"Error 3: Unexpected error: {e}")
        sys.exit(3)

if __name__ == "__main__":
    manage_dns_record()
