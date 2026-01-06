import sqlite3
# this is a database initialization code

# create connection with database, if it not exist, it will create a new one
conn = sqlite3.connect('database.db')
# cursor will allow to execute SQL commands
cursor = conn.cursor()

# create OS distribution table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS os_distribution (
    os TEXT NOT NULL,
    share REAL NOT NULL
    )
    """)

# deletes data in case if code will be initialized more than once
cursor.execute("DELETE FROM os_distribution")
# insert a meaningful data to the table
data = [
    ('Linux Distributions', 63.1),
    ('Windows Server', 30.2),
    ('Unix/Other', 6.7)
]
cursor.executemany("INSERT INTO os_distribution VALUES (?, ?)", data)
# commits data to the database
conn.commit()

# create Cloud market share table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS cloud_market_share (
    company TEXT NOT NULL,
    share INTEGER NOT NULL
    )
    """)
cursor.execute("DELETE FROM cloud_market_share")
data = [
    ('Alibaba', 4),
    ('AWS', 29),
    ('Google Cloud', 13),
    ('Microsoft Azure', 20),
    ('Others', 34)
]
cursor.executemany("INSERT INTO cloud_market_share VALUES (?, ?)", data)
conn.commit()

# create AWS Availability Zones table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS aws_availability_zones (
    region TEXT NOT NULL,
    zones INTEGER NOT NULL
    )
    """)
cursor.execute("DELETE FROM aws_availability_zones")
data = [
    ('North America', 31),
    ('Europe', 27),
    ('Asia Pacific', 32),
    ('Middle East & Africa', 15),
    ("South America", 12),
]
cursor.executemany("INSERT INTO aws_availability_zones VALUES (?, ?)", data)
conn.commit()

# create Number of Data Centers table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS data_center_numbers (
    company TEXT NOT NULL,
    num_of_data_centers INTEGER NOT NULL
    )
    """)
cursor.execute("DELETE FROM data_center_numbers")
data = [
    ('Alibaba', 92),
    ('AWS', 135),
    ('Microsoft Azure', 134),
    ('Google Cloud', 130),
    ('Others', 76)
]
cursor.executemany("INSERT INTO data_center_numbers VALUES (?, ?)", data)
conn.commit()


cursor.close()  # closes the cursor
conn.close()    # closes the connection