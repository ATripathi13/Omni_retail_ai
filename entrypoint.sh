#!/bin/bash
set -e

echo "Starting Omni Retail AI Entrypoint..."

# 1. Check if database exists (assuming shop_core.db is a proxy for all)
if [ ! -f "shop_core.db" ]; then
    echo "Database not found. Seeding data..."
    python -m app.seeders.seed_data
else
    echo "Database exists. Skipping seeding."
fi

# 2. Generate SQL Schemas (Deliverable requirement)
echo "Generating SQL Schemas..."
python generate_sql_schemas.py

# 3. Start the application
echo "Starting Uvicorn..."
exec uvicorn app.main_api:app --host 0.0.0.0 --port 8000
