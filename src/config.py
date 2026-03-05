import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to the Excel file in your project/data folder (adjust filename if needed)
EXCEL_PATH = os.path.join(BASE_DIR, "..", "data", "Metal Fitting Database.xlsx")

# Exact connector types for dropdown menu - these will be matched exactly in the database
SUPPORTED_CONNECTOR_TYPES = [
    "Cap",
    "Long Radius 90 Elbow",
    "Short Radius 90 Elbow",
    "Tee",
]

# Available sizes for each connector type (from database)
CONNECTOR_SIZES = {
    "Cap": ['0.5', '0.75', '1.0', '1.25', '1.5', '2.0', '2.5', '3.0', '3.5', '4.0', '5.0', '6.0', '8.0', '10.0', '12.0'],
    "Long Radius 90 Elbow": ['0.5', '0.75', '1.0', '1.25', '1.5', '2.0', '2.5', '3.0', '3.5', '4.0', '5.0', '6.0', '8.0', '10.0', '12.0'],
    "Short Radius 90 Elbow": ['1.0', '1.25', '1.5', '2.0', '2.5', '3.0', '3.5', '4.0', '5.0', '6.0', '8.0', '10.0', '12.0'],
    "Tee": ['0.5', '0.75', '1.0', '1.25', '1.5', '2.0', '2.5', '3.0', '3.5', '4.0', '5.0', '6.0', '8.0', '10.0', '12.0'],
}

# Offset columns - all connectors use "Offset" as primary, "Offset (G1)" as secondary
OFFSET_COLUMN = "Offset"
OFFSET_COLUMN_G1 = "Offset (G1)"

# Sheet name to read (explicit per your instruction)
SHEET_NAME = "Database"

# Connector image mapping for display
CONNECTOR_IMAGE_MAP = {
    "Cap": "cap.png",
    "Long Radius 90 Elbow": "long_radius_elbow.png",
    "Short Radius 90 Elbow": "short_radius_elbow.png",
    "Tee": "tee.png",
}
