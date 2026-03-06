import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to the Excel file in your project/data folder (adjust filename if needed)
EXCEL_PATH = os.path.join(BASE_DIR, "..", "data", "Metal Fitting Database.xlsx")

# Exact connector types for dropdown menu - these will be matched exactly in the database
SUPPORTED_CONNECTOR_TYPES = [
    "Cap",
    "Concentric Reducer",
    "Eccentric Reducer",
    "Long Pattern Lap Joint Stub End ",
    "Long Radius 90 Elbow",
    "Reducing Outlet Tee",
    "Short Pattern Lap Joint Stub End",
    "Short Radius 90 Elbow",
    "Tee",
]

# Available sizes for each connector type (from database)
CONNECTOR_SIZES = {
    "Cap": ['0.5', '0.75', '1.0', '1.25', '1.5', '2.0', '2.5', '3.0', '3.5', '4.0', '5.0', '6.0', '8.0', '10.0', '12.0', '100'],
    "Concentric Reducer": ['3/4 x 1/2', '3/4 x 3/8', '1 x 3/4', '1 x 1/2', '1 1/4 x 1', '1 1/4 x 3/4', '1 1/4 x 1/2', '1 1/2 x 1 1/4', '1 1/2 x 1', '1 1/2 x 3/4', '1 1/2 x 1/2', '2 x 1 1/2', '2 x 1 1/4', '2 x 1', '2 x 3/4', '2 1/2 x 2', '2 1/2 x 1 1/2', '2 1/2 x 1 1/4', '2 1/2 x 1', '3 x 2 1/2', '3 x 2', '3 x 1 1/2', '3 x 1 1/4', '3 1/2 x 3', '3 1/2 x 2 1/2', '3 1/2 x 2', '3 1/2 x 1 1/2', '3 1/2 x 1 1/4', '4 x 3 1/2', '4 x 3', '4 x 2 1/2', '4 x 2', '4 x 1 1/2', '5 x 4', '5 x 3 1/2', '5 x 3', '5 x 2 1/2', '5 x 2', '6 x 5', '6 x 4', '6 x 3 1/2', '6 x 3', '6 x 2 1/2', '8 x 6', '8 x 5', '8 x 4', '8 x 3 1/2', '10 x 8', '10 x 6', '10 x 5', '10 x 4', '12 x 10', '12 x 8', '12 x 6', '12 x 5', '14 x 12', '14 x 10', '14 x 8', '14 x 6', '16 x 14', '16 x 12', '16 x 10', '16 x 8', '18 x 16', '18 x 14', '18 x 12', '18 x 10'],
    "Eccentric Reducer": ['3/4 x 1/2', '3/4 x 3/8', '1 x 3/4', '1 x 1/2', '1 1/4 x 1', '1 1/4 x 3/4', '1 1/4 x 1/2', '1 1/2 x 1 1/4', '1 1/2 x 1', '1 1/2 x 3/4', '1 1/2 x 1/2', '2 x 1 1/2', '2 x 1 1/4', '2 x 1', '2 x 3/4', '2 1/2 x 2', '2 1/2 x 1 1/2', '2 1/2 x 1 1/4', '2 1/2 x 1', '3 x 2 1/2', '3 x 2', '3 x 1 1/2', '3 x 1 1/4', '3 1/2 x 3', '3 1/2 x 2 1/2', '3 1/2 x 2', '3 1/2 x 1 1/2', '3 1/2 x 1 1/4', '4 x 3 1/2', '4 x 3', '4 x 2 1/2', '4 x 2', '4 x 1 1/2', '5 x 4', '5 x 3 1/2', '5 x 3', '5 x 2 1/2', '5 x 2', '6 x 5', '6 x 4', '6 x 3 1/2', '6 x 3', '6 x 2 1/2', '8 x 6', '8 x 5', '8 x 4', '8 x 3 1/2', '10 x 8', '10 x 6', '10 x 5', '10 x 4', '12 x 10', '12 x 8', '12 x 6', '12 x 5', '14 x 12', '14 x 10', '14 x 8', '14 x 6', '16 x 14', '16 x 12', '16 x 10', '16 x 8', '18 x 16', '18 x 14', '18 x 12', '18 x 10'],
    "Long Pattern Lap Joint Stub End ": ['1/2', '3/4', '1', '1 1/4', '1 1/2', '2', '2 1/2', '3', '3 1/2', '4', '5', '6', '8', '10', '12', '14', '16', '18'],
    "Long Radius 90 Elbow": ['0.5', '0.75', '1.0', '1.25', '1.5', '2.0', '2.5', '3.0', '3.5', '4.0', '5.0', '6.0', '8.0', '10.0', '12.0', '16'],
    "Reducing Outlet Tee": ['1/2 x 1/2 x 3/8', '1/2 x 1/2 x 1/4', '3/4 x 3/4 x 1/2', '3/4 x 3/4 x 3/8', '1 x 1 x 3/4', '1 x 1 x 1/2', '1 1/4 x 1 1/4 x 1', '1 1/4 x 1 1/4 x 3/4', '1 1/4 x 1 1/4 x 1/2', '1 1/2 x 1 1/2 x 1 1/4', '1 1/2 x 1 1/2 x 1', '1 1/2 x 1 1/2 x 3/4', '1 1/2 x 1 1/2 x 1/2', '2 x 2 x 1 1/2', '2 x 2 x 1 1/4', '2 x 2 x 1', '2 x 2 x 3/4', '2 1/2 x 2 1/2 x 2', '2 1/2 x 2 1/2 x 1 1/2', '2 1/2 x 2 1/2 x 1 1/4', '2 1/2 x 2 1/2 x 1', '3 x 3 x 2 1/2', '3 x 3 x 2', '3 x 3 x 1 1/2', '3 x 3 x 1 1/4', '3 1/2 x 3 1/2 x 3', '3 1/2 x 3 1/2 x 2 1/2', '3 1/2 x 3 1/2 x 2', '3 1/2 x 3 1/2 x 1 1/2', '4 x 4 x 3 1/2', '4 x 4 x 3', '4 x 4 x 2 1/2', '4 x 4 x 2', '4 x 4 x 1 1/2', '5 x 5 x 4', '5 x 5 x 3 1/2', '5 x 5 x 3', '5 x 5 x 2 1/2', '5 x 5 x 2', '6 x 6 x 5', '6 x 6 x 4', '6 x 6 x 3 1/2', '6 x 6 x 3', '6 x 6 x 2 1/2', '8 x 8 x 6', '8 x 8 x 5', '8 x 8 x 4', '8 x 8 x 3 1/2', '10 x 10 x 8', '10 x 10 x 6', '10 x 10 x 5', '10 x 10 x 4', '12 x 12 x 10', '12 x 12 x 8', '12 x 12 x 6', '12 x 12 x 5', '14 x 14 x 12', '14 x 14 x 10', '14 x 14 x 8', '14 x 14 x 6', '16 x 16 x 14', '16 x 16 x 12', '16 x 16 x 10', '16 x 16 x 8', '16 x 16 x 6', '18 x 18 x 16', '18 x 18 x 14', '18 x 18 x 12', '18 x 18 x 10', '18 x 18 x 8'],
    "Short Pattern Lap Joint Stub End": ['1/2', '3/4', '1', '1 1/4', '1 1/2', '2', '2 1/2', '3', '3 1/2', '4', '5', '6', '8', '10', '12', '14', '16', '18'],
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
    "Concentric Reducer": "concentric_reducer.png",
    "Eccentric Reducer": "eccentric_reducer.png",
    "Long Pattern Lap Joint Stub End ": "long_pattern_lap_joint_stub_end.png",  
    "Long Radius 90 Elbow": "long_radius_elbow.png",
    "Reducing Outlet Tee": "reducing_tee.png",
    "Short Pattern Lap Joint Stub End": "short_pattern_lap_joint_stub_end.png",
    "Short Radius 90 Elbow": "short_radius_elbow.png",
    "Tee": "tee.png",
}
