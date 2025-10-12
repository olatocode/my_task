<!-- @format -->

# Supabase CSV Loader

This small utility loads all CSV files in this folder into a Supabase Postgres database.

What it does

- Connects to a Postgres database using the `SUPABASE_DB_URL` environment variable.
- Scans the folder for `*.csv` files and writes each to a table named after the CSV file (stem).
- By default it replaces existing tables; you can switch to append mode.

Quick start

1. Copy `.env.example` to `.env` and fill `SUPABASE_DB_URL` with your Supabase Postgres URI.
2. Create a virtualenv and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate    # on Windows use .venv\Scripts\activate
pip install -r requirements.txt
```

3. Run the loader from this folder:

```bash
python supabase_load.py --folder . --mode replace
```

Notes

- The script uses pandas to read CSVs and SQLAlchemy (with psycopg2) to write to Postgres.
- Ensure your Supabase network rules allow connections from your IP or use an SSH tunnel.
