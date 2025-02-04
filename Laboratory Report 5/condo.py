import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('solmaris_condo.db')
cursor = conn.cursor()

# Create Renter table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Renter (
    RenterID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT NOT NULL,
    MiddleInitial CHAR(1),
    LastName TEXT NOT NULL,
    Address TEXT,
    City TEXT,
    State TEXT,
    PostalCode TEXT,
    PhoneNumber TEXT,
    Email TEXT
)
''')

# Create Property table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Property (
    PropertyID INTEGER PRIMARY KEY AUTOINCREMENT,
    LocationNumber INTEGER NOT NULL,
    LocationName TEXT,
    Address TEXT,
    City TEXT,
    State TEXT,
    PostalCode TEXT,
    UnitNumber TEXT,
    SquareFootage INTEGER,
    NumberOfBedrooms INTEGER,
    NumberOfBathrooms INTEGER,
    MaxPersons INTEGER,
    BaseWeeklyRate REAL
)
''')

# Create RentalAgreement table
cursor.execute('''
CREATE TABLE IF NOT EXISTS RentalAgreement (
    AgreementID INTEGER PRIMARY KEY AUTOINCREMENT,
    RenterID INTEGER,
    StartDate TEXT NOT NULL,
    EndDate TEXT NOT NULL,
    WeeklyRentalAmount REAL,
    FOREIGN KEY (RenterID) REFERENCES Renter (RenterID)
)
''')

# Insert sample data into Renter table
cursor.executemany('''
INSERT INTO Renter (FirstName, MiddleInitial, LastName, Address, City, State, PostalCode, PhoneNumber, Email) 
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
''', [
    ("John", "A", "Doe", "123 Elm St", "Miami", "FL", "33101", "555-1234", "john.doe@example.com"),
    ("Jane", "B", "Smith", "456 Pine Ave", "Orlando", "FL", "32801", "555-5678", "jane.smith@example.com")
])

# Insert sample data into Property table
cursor.executemany('''
INSERT INTO Property (LocationNumber, LocationName, Address, City, State, PostalCode, UnitNumber, SquareFootage, NumberOfBedrooms, NumberOfBathrooms, MaxPersons, BaseWeeklyRate) 
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', [
    (1, "Oceanview Condos", "789 Beach Blvd", "Miami", "FL", "33139", "101", 1200, 2, 2, 4, 1500.00),
    (2, "Sunset Villas", "321 Sunset Rd", "Orlando", "FL", "32803", "202", 1500, 3, 2, 6, 2000.00)
])

# Insert sample data into RentalAgreement table
cursor.executemany('''
INSERT INTO RentalAgreement (RenterID, StartDate, EndDate, WeeklyRentalAmount) 
VALUES (?, ?, ?, ?)
''', [
    (1, "2025-02-01", "2025-02-08", 1500.00),
    (2, "2025-02-10", "2025-02-17", 2000.00)
])

# Commit changes
conn.commit()

# Display the data from all tables
def display_table(table_name):
    print(f"\n{table_name} Table:")
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Display all tables
display_table("Renter")
display_table("Property")
display_table("RentalAgreement")

# Close the connection
conn.close()
