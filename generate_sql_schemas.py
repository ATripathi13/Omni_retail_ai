import sqlite3
import os

DB_FILES = ['shop_core.db', 'ship_stream.db', 'pay_guard.db', 'care_desk.db']
OUTPUT_DIR = 'schemas'

def generate_sql_dump():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Created directory: {OUTPUT_DIR}")

    for db_file in DB_FILES:
        if not os.path.exists(db_file):
            print(f"Warning: {db_file} not found. Skipping.")
            continue
            
        print(f"Dumping {db_file}...")
        try:
            conn = sqlite3.connect(db_file)
            with open(f"{OUTPUT_DIR}/{db_file.replace('.db', '.sql')}", 'w', encoding='utf-8') as f:
                for line in conn.iterdump():
                    f.write(f'{line}\n')
            conn.close()
            print(f"Successfully created {OUTPUT_DIR}/{db_file.replace('.db', '.sql')}")
        except Exception as e:
            print(f"Error dumping {db_file}: {e}")

if __name__ == "__main__":
    generate_sql_dump()
