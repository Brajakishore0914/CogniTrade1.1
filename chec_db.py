import os
import sys
from dotenv import load_dotenv
from supabase import create_client

# Add Backend to path to import settings if needed
sys.path.append(os.path.join(os.getcwd(), 'Backend'))

load_dotenv('Backend/.env')

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")

if not url or not key:
    print("Error: SUPABASE_URL or SUPABASE_SERVICE_ROLE_KEY not found in Backend/.env")
    sys.exit(1)

supabase = create_client(url, key)

tables = ["users", "portfolios", "predictions", "quiz_scores", "paper_positions", "paper_trades", "cash_ledger"]

print(f"Checking tables for Supabase URL: {url}")
for table in tables:
    try:
        res = supabase.table(table).select("*", count="exact").limit(0).execute()
        count = res.count
        print(f"Table '{table}': {count} records found.")
    except Exception as e:
        print(f"Error checking table '{table}': {e}")