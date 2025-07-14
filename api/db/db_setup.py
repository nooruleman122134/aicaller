import sqlite3
import os

# ---- Configuration ----
DB_PATH = os.path.join(os.path.dirname(__file__), 'rides.db')

# ---- SQL Statements ----
CREATE_RIDES_TABLE = '''
CREATE TABLE IF NOT EXISTS rides (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    rider_name TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    status TEXT NOT NULL,
    complaint_flag INTEGER DEFAULT 0,
    issue_type TEXT
)
'''

INSERT_SAMPLE_RIDE = '''
INSERT INTO rides (rider_name, phone_number, status, complaint_flag, issue_type)
VALUES (?, ?, ?, ?, ?)
'''

# ---- Execution ----
def setup_database():
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        # Create table
        c.execute(CREATE_RIDES_TABLE)

        # Check if sample ride already exists
        c.execute("SELECT COUNT(*) FROM rides WHERE phone_number = ?", ("+923001234567",))
        count = c.fetchone()[0]

        if count == 0:
            c.execute(INSERT_SAMPLE_RIDE, ("Ali", "+923001234567", "arrived", 0, None))
            print("✅ Sample ride inserted.")
        else:
            print("ℹ️ Sample ride already exists. Skipping insert.")

        conn.commit()
        conn.close()
        print("✅ Database setup complete.")
    except Exception as e:
        print("❌ Error during DB setup:", e)

# ---- Run if file executed directly ----
if __name__ == "__main__":
    setup_database()
