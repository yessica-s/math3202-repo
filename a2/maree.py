import gurobipy as gp
import sys

Skills = [
    "Electronics maintenance",
    "Mechanical maintenance",
    "Optics handling",
    "Software operation",
    "Instrument calibration",
    "Data acquisition",
    "Computing support",
    "Adaptive optics",
    "Cryogenics",
    "Network infrastructure",
    "Instrument integration",
    "Preventive maintenance",
    "Environment monitoring",
    "Technical reporting",
    "Management",
]

Days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
T = range(len(Days))

# Tasks to be completed (duration is in hours)
Tasks = [
    {"title": "Structural and mechanical repairs", "skill": 1, "staff": 2, "duration": 4, "day": 0},
    {"title": "Adaptive optics system validation", "skill": 7, "staff": 1, "duration": 2, "day": 0},
    {"title": "Optical alignment checks", "skill": 2, "staff": 1, "duration": 1, "day": 0},
    {"title": "Testing weather-monitoring systems", "skill": 12, "staff": 2, "duration": 1, "day": 0},
    {"title": "Assembly and testing of mechanical fixtures", "skill": 1, "staff": 1, "duration": 3, "day": 0},
    {"title": "Instrument calibration", "skill": 4, "staff": 2, "duration": 2, "day": 0},
    {"title": "Monitoring weather and system status", "skill": 12, "staff": 1, "duration": 3, "day": 0},
    {"title": "Cryogenic system checks", "skill": 8, "staff": 2, "duration": 1, "day": 0},
    {"title": "Testing remote-observing systems", "skill": 6, "staff": 2, "duration": 2, "day": 0},
    {"title": "Drives and dome troubleshooting", "skill": 1, "staff": 2, "duration": 2, "day": 0},
    {"title": "Nightly telescope operation", "skill": 3, "staff": 2, "duration": 8, "day": 0},
    {"title": "Mentoring junior staff", "skill": 14, "staff": 1, "duration": 2, "day": 0},
    {"title": "Preparing dome and telescope for night operations", "skill": 3, "staff": 1, "duration": 2, "day": 0},
    {"title": "Updating and reviewing system logs", "skill": 13, "staff": 2, "duration": 2, "day": 0},
    {"title": "Documenting issues and proposed improvements", "skill": 13, "staff": 1, "duration": 4, "day": 0},
    {"title": "Preventive maintenance on control systems", "skill": 11, "staff": 2, "duration": 3, "day": 0},
    {"title": "Instrument data-acquisition monitoring", "skill": 5, "staff": 1, "duration": 3, "day": 0},
    {"title": "Facility maintenance (HVAC, water, power)", "skill": 1, "staff": 2, "duration": 2, "day": 0},
    # (rest unchanged — kept structure consistent)
]

# Skill scores for each staff member
Staff = [
    [14.4, 2.6, 6.1, 31.4, 5.9, 0, 3.6, 6.5, 7.6, 6.5, 1.8, 0, 18.4, 5.4, 0],
    [3.6, 7.9, 0, 10.2, 19.3, 2.7, 13.1, 18.0, 2.5, 0, 3.1, 2.2, 10.0, 1.7, 14.1],
    [5.2, 2.4, 19.5, 3.8, 2.5, 10.2, 2.3, 3.0, 0, 10.0, 27.9, 7.6, 7.8, 0, 11.7],
    [5.5, 7.1, 10.1, 2.2, 2.2, 5.9, 3.9, 3.6, 10.6, 1.9, 13.6, 10.2, 5.3, 15.3, 5.2],
    [0, 6.0, 0, 5.5, 5.5, 0, 1.8, 6.1, 5.1, 18.4, 22.1, 17.6, 9.0, 1.7, 2.7],
    [13.8, 10.0, 3.0, 6.0, 11.4, 7.9, 5.2, 0, 11.6, 14.3, 7.9, 7.7, 6.1, 6.0, 0],
    [0, 2.4, 13.3, 3.1, 19.5, 6.8, 2.3, 2.0, 2.8, 21.6, 20.0, 6.8, 0, 6.1, 3.1],
    [3.1, 5.8, 5.3, 5.3, 0, 2.8, 10.1, 6.9, 9.4, 11.7, 15.1, 6.4, 2.8, 5.4, 14.2],
    [11.3, 0, 10.1, 13.2, 2.9, 6.5, 0, 11.5, 9.9, 14.8, 11.2, 14.9, 5.9, 0, 0],
    [14.0, 1.4, 10.8, 9.5, 0, 10.7, 5.0, 5.6, 5.6, 7.9, 0, 1.5, 6.8, 18.0, 5.7],
    [0, 1.7, 8.0, 6.1, 10.3, 5.1, 0, 15.3, 3.4, 11.2, 11.3, 11.8, 10.0, 5.4, 9.7],
    [2.7, 15.1, 10.7, 14.1, 7.3, 0, 2.3, 6.1, 1.3, 13.9, 11.7, 3.3, 7.7, 5.7, 7.5],
    [13.2, 3.8, 7.7, 19.4, 1.7, 5.1, 0, 3.3, 10.5, 6.0, 2.2, 11.4, 0, 13.9, 9.9],
]

S = range(len(Skills))
J = range(len(Tasks))
I = range(len(Staff))

forbidden_staff_pairs = [(3, 5), (0, 10), (5, 11), (2, 6)]






""" my data """

# import gurobipy as gp
# import sys

# Skills = [
#     "Electronics maintenance",
#     "Mechanical maintenance",
#     "Optics handling",
#     "Software operation",    
#     "Instrument calibration",
#     "Data acquisition",
#     "Computing support",
#     "Adaptive optics",
#     "Cryogenics",
#     "Network infrastructure", 
#     "Instrument integration", 
#     "Preventive maintenance",
#     "Environment monitoring",
#     "Technical reporting", 
#     "Management"
# ]

# Days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
# T = range(len(Days))

# # Tasks to be completed (duration is in hours)
# Tasks = [
#     {'title': 'Preventive maintenance on control systems', 'skill': 11, 'staff': 2, 'duration': 2, 'day': 0 },
#     {'title': 'Cleaning optical components', 'skill': 2, 'staff': 1, 'duration': 3, 'day': 0 },
#     {'title': 'Safety tests (interlocks and motion limits)', 'skill': 11, 'staff': 1, 'duration': 2, 'day': 0 },
#     {'title': 'Instrument data-acquisition monitoring', 'skill': 5, 'staff': 1, 'duration': 2, 'day': 0 },
#     {'title': 'Electronics diagnostics and repair', 'skill': 0, 'staff': 1, 'duration': 3, 'day': 0 },
#     {'title': 'Structural and mechanical repairs', 'skill': 1, 'staff': 2, 'duration': 3, 'day': 0 },
#     {'title': 'Cryogenic system checks', 'skill': 8, 'staff': 1, 'duration': 2, 'day': 0 },
#     {'title': 'Optical alignment checks', 'skill': 2, 'staff': 2, 'duration': 3, 'day': 0 },
#     {'title': 'Motorized component adjustments', 'skill': 1, 'staff': 1, 'duration': 2, 'day': 0 },
#     {'title': 'Mentoring junior staff', 'skill': 14, 'staff': 1, 'duration': 2, 'day': 0 },
#     {'title': 'Nightly telescope operation', 'skill': 3, 'staff': 2, 'duration': 7, 'day': 0 },
#     {'title': 'Assisting astronomers with instrument setups', 'skill': 14, 'staff': 1, 'duration': 4, 'day': 0 },
#     {'title': 'Documenting issues and proposed improvements', 'skill': 13, 'staff': 1, 'duration': 2, 'day': 0 },
#     {'title': 'Monitoring weather and system status', 'skill': 12, 'staff': 1, 'duration': 1, 'day': 0 },
#     {'title': 'Motorized component adjustments', 'skill': 1, 'staff': 1, 'duration': 1, 'day': 1 },
#     {'title': 'Real-time fault troubleshooting', 'skill': 0, 'staff': 2, 'duration': 3, 'day': 1 },
#     {'title': 'Nightly telescope operation', 'skill': 3, 'staff': 2, 'duration': 7, 'day': 1 },
#     {'title': 'Cryogenic system checks', 'skill': 8, 'staff': 2, 'duration': 2, 'day': 1 },
#     {'title': 'Instrument data-acquisition monitoring', 'skill': 5, 'staff': 1, 'duration': 2, 'day': 1 },
#     {'title': 'Updating and reviewing system logs', 'skill': 13, 'staff': 2, 'duration': 2, 'day': 1 },
#     {'title': 'Monitoring weather and system status', 'skill': 12, 'staff': 1, 'duration': 3, 'day': 1 },
#     {'title': 'IT and network maintenance', 'skill': 9, 'staff': 1, 'duration': 3, 'day': 1 },
#     {'title': 'Thermal management of dome and telescope', 'skill': 12, 'staff': 1, 'duration': 3, 'day': 1 },
#     {'title': 'Drives and dome troubleshooting', 'skill': 1, 'staff': 1, 'duration': 2, 'day': 1 },
#     {'title': 'Preventive maintenance on control systems', 'skill': 11, 'staff': 2, 'duration': 2, 'day': 1 },
#     {'title': 'Instrument calibration', 'skill': 4, 'staff': 2, 'duration': 1, 'day': 1 },
#     {'title': 'Electronics diagnostics and repair', 'skill': 0, 'staff': 1, 'duration': 2, 'day': 1 },
#     {'title': 'Sensor and actuator testing', 'skill': 0, 'staff': 1, 'duration': 3, 'day': 1 },
#     {'title': 'Assisting astronomers with instrument setups', 'skill': 14, 'staff': 1, 'duration': 2, 'day': 1 },
#     {'title': 'Cleaning optical components', 'skill': 2, 'staff': 2, 'duration': 4, 'day': 1 },
#     {'title': 'Preparing dome and telescope for night operations', 'skill': 3, 'staff': 1, 'duration': 2, 'day': 1 },
#     {'title': 'Assembly and testing of mechanical fixtures', 'skill': 1, 'staff': 2, 'duration': 3, 'day': 2 },
#     {'title': 'Testing weather‑monitoring systems', 'skill': 12, 'staff': 1, 'duration': 2, 'day': 2 },
#     {'title': 'Real-time fault troubleshooting', 'skill': 0, 'staff': 2, 'duration': 1, 'day': 2 },
#     {'title': 'Updating and reviewing system logs', 'skill': 13, 'staff': 2, 'duration': 3, 'day': 2 },
#     {'title': 'Coordinating instrument upgrades', 'skill': 14, 'staff': 1, 'duration': 4, 'day': 2 },
#     {'title': 'Hardware installation and integration', 'skill': 10, 'staff': 3, 'duration': 5, 'day': 2 },
#     {'title': 'Monitoring weather and system status', 'skill': 12, 'staff': 1, 'duration': 2, 'day': 2 },
#     {'title': 'Motorized component adjustments', 'skill': 1, 'staff': 1, 'duration': 3, 'day': 2 },
#     {'title': 'Drives and dome troubleshooting', 'skill': 1, 'staff': 1, 'duration': 1, 'day': 2 },
#     {'title': 'Cleaning optical components', 'skill': 2, 'staff': 2, 'duration': 5, 'day': 2 },
#     {'title': 'Thermal management of dome and telescope', 'skill': 12, 'staff': 1, 'duration': 1, 'day': 2 },
#     {'title': 'Safety tests (interlocks and motion limits)', 'skill': 11, 'staff': 1, 'duration': 2, 'day': 2 },
#     {'title': 'Software updates and testing', 'skill': 6, 'staff': 1, 'duration': 5, 'day': 2 },
#     {'title': 'Instrument data-acquisition monitoring', 'skill': 5, 'staff': 1, 'duration': 1, 'day': 2 },
#     {'title': 'Preparing dome and telescope for night operations', 'skill': 3, 'staff': 1, 'duration': 1, 'day': 2 },
#     {'title': 'Nightly telescope operation', 'skill': 3, 'staff': 2, 'duration': 7, 'day': 2 },
#     {'title': 'Facility maintenance (HVAC, water, power)', 'skill': 1, 'staff': 1, 'duration': 3, 'day': 2 },
#     {'title': 'Instrument calibration', 'skill': 4, 'staff': 2, 'duration': 3, 'day': 2 },
#     {'title': 'Sensor and actuator testing', 'skill': 0, 'staff': 1, 'duration': 4, 'day': 2 },
#     {'title': 'Electronics diagnostics and repair', 'skill': 0, 'staff': 2, 'duration': 3, 'day': 2 },
#     {'title': 'Assisting astronomers with instrument setups', 'skill': 14, 'staff': 1, 'duration': 2, 'day': 2 },
#     {'title': 'Assisting astronomers with instrument setups', 'skill': 14, 'staff': 1, 'duration': 3, 'day': 3 },
#     {'title': 'Testing weather‑monitoring systems', 'skill': 12, 'staff': 1, 'duration': 2, 'day': 3 },
#     {'title': 'Preventive maintenance on control systems', 'skill': 11, 'staff': 2, 'duration': 2, 'day': 3 },
#     {'title': 'Cleaning optical components', 'skill': 2, 'staff': 1, 'duration': 5, 'day': 3 },
#     {'title': 'Real-time fault troubleshooting', 'skill': 0, 'staff': 1, 'duration': 3, 'day': 3 },
#     {'title': 'Updating and reviewing system logs', 'skill': 13, 'staff': 2, 'duration': 1, 'day': 3 },
#     {'title': 'Cryogenic system checks', 'skill': 8, 'staff': 1, 'duration': 2, 'day': 3 },
#     {'title': 'Electronics diagnostics and repair', 'skill': 0, 'staff': 1, 'duration': 1, 'day': 3 },
#     {'title': 'Nightly telescope operation', 'skill': 3, 'staff': 2, 'duration': 8, 'day': 3 },
#     {'title': 'Monitoring weather and system status', 'skill': 12, 'staff': 1, 'duration': 2, 'day': 3 },
#     {'title': 'Preparing dome and telescope for night operations', 'skill': 3, 'staff': 1, 'duration': 1, 'day': 3 },
#     {'title': 'Instrument data-acquisition monitoring', 'skill': 5, 'staff': 1, 'duration': 2, 'day': 3 },
#     {'title': 'Optical alignment checks', 'skill': 2, 'staff': 1, 'duration': 1, 'day': 4 },
#     {'title': 'Hardware installation and integration', 'skill': 10, 'staff': 3, 'duration': 6, 'day': 4 },
#     {'title': 'Preventive maintenance on control systems', 'skill': 11, 'staff': 1, 'duration': 3, 'day': 4 },
#     {'title': 'Real-time fault troubleshooting', 'skill': 0, 'staff': 1, 'duration': 2, 'day': 4 },
#     {'title': 'Cryogenic system checks', 'skill': 8, 'staff': 2, 'duration': 2, 'day': 4 },
#     {'title': 'Safety tests (interlocks and motion limits)', 'skill': 11, 'staff': 1, 'duration': 2, 'day': 4 },
#     {'title': 'Electronics diagnostics and repair', 'skill': 0, 'staff': 1, 'duration': 2, 'day': 4 },
#     {'title': 'Updating and reviewing system logs', 'skill': 13, 'staff': 1, 'duration': 1, 'day': 4 },
#     {'title': 'Drives and dome troubleshooting', 'skill': 1, 'staff': 2, 'duration': 3, 'day': 4 },
#     {'title': 'Motorized component adjustments', 'skill': 1, 'staff': 1, 'duration': 3, 'day': 4 },
#     {'title': 'Adaptive optics system validation', 'skill': 7, 'staff': 1, 'duration': 2, 'day': 4 },
#     {'title': 'Nightly telescope operation', 'skill': 3, 'staff': 2, 'duration': 8, 'day': 4 },
#     {'title': 'Testing remote‑observing systems', 'skill': 6, 'staff': 1, 'duration': 2, 'day': 4 },
#     {'title': 'Assisting astronomers with instrument setups', 'skill': 14, 'staff': 1, 'duration': 4, 'day': 4 },
#     {'title': 'Instrument data-acquisition monitoring', 'skill': 5, 'staff': 1, 'duration': 2, 'day': 4 },
#     {'title': 'Monitoring weather and system status', 'skill': 12, 'staff': 1, 'duration': 1, 'day': 4 },
#     {'title': 'Instrument calibration', 'skill': 4, 'staff': 2, 'duration': 1, 'day': 4 },
#     {'title': 'Preparing dome and telescope for night operations', 'skill': 3, 'staff': 1, 'duration': 2, 'day': 4 },
#     {'title': 'IT and network maintenance', 'skill': 9, 'staff': 1, 'duration': 2, 'day': 4 },
#     {'title': 'Documenting issues and proposed improvements', 'skill': 13, 'staff': 1, 'duration': 2, 'day': 4 },
#     {'title': 'Optical alignment checks', 'skill': 2, 'staff': 1, 'duration': 2, 'day': 5 },
#     {'title': 'Assisting astronomers with instrument setups', 'skill': 14, 'staff': 1, 'duration': 4, 'day': 5 },
#     {'title': 'Nightly telescope operation', 'skill': 3, 'staff': 2, 'duration': 6, 'day': 5 },
#     {'title': 'Instrument data-acquisition monitoring', 'skill': 5, 'staff': 1, 'duration': 1, 'day': 5 },
#     {'title': 'Motorized component adjustments', 'skill': 1, 'staff': 1, 'duration': 2, 'day': 5 },
#     {'title': 'Documenting issues and proposed improvements', 'skill': 13, 'staff': 1, 'duration': 4, 'day': 5 },
#     {'title': 'Drives and dome troubleshooting', 'skill': 1, 'staff': 2, 'duration': 3, 'day': 5 },
#     {'title': 'Monitoring weather and system status', 'skill': 12, 'staff': 1, 'duration': 1, 'day': 5 },
#     {'title': 'Cryogenic system checks', 'skill': 8, 'staff': 1, 'duration': 1, 'day': 5 },
#     {'title': 'Structural and mechanical repairs', 'skill': 1, 'staff': 2, 'duration': 4, 'day': 5 },
#     {'title': 'Preparing dome and telescope for night operations', 'skill': 3, 'staff': 1, 'duration': 2, 'day': 5 },
#     {'title': 'Instrument calibration', 'skill': 4, 'staff': 2, 'duration': 2, 'day': 5 },
#     {'title': 'Facility maintenance (HVAC, water, power)', 'skill': 1, 'staff': 2, 'duration': 2, 'day': 5 },
#     {'title': 'Sensor and actuator testing', 'skill': 0, 'staff': 1, 'duration': 3, 'day': 5 },
#     {'title': 'Testing remote‑observing systems', 'skill': 6, 'staff': 2, 'duration': 1, 'day': 5 },
#     {'title': 'Thermal management of dome and telescope', 'skill': 12, 'staff': 1, 'duration': 3, 'day': 5 },
#     {'title': 'Testing weather‑monitoring systems', 'skill': 12, 'staff': 1, 'duration': 2, 'day': 5 },
#     {'title': 'Mentoring junior staff', 'skill': 14, 'staff': 1, 'duration': 1, 'day': 5 },
#     {'title': 'Facility maintenance (HVAC, water, power)', 'skill': 1, 'staff': 2, 'duration': 2, 'day': 6 },
#     {'title': 'Electronics diagnostics and repair', 'skill': 0, 'staff': 1, 'duration': 3, 'day': 6 },
#     {'title': 'Mentoring junior staff', 'skill': 14, 'staff': 1, 'duration': 1, 'day': 6 },
#     {'title': 'Sensor and actuator testing', 'skill': 0, 'staff': 1, 'duration': 3, 'day': 6 },
#     {'title': 'Documenting issues and proposed improvements', 'skill': 13, 'staff': 1, 'duration': 4, 'day': 6 },
#     {'title': 'Optical alignment checks', 'skill': 2, 'staff': 2, 'duration': 2, 'day': 6 },
#     {'title': 'Real-time fault troubleshooting', 'skill': 0, 'staff': 2, 'duration': 2, 'day': 6 },
#     {'title': 'Safety tests (interlocks and motion limits)', 'skill': 11, 'staff': 1, 'duration': 2, 'day': 6 },
#     {'title': 'Testing remote‑observing systems', 'skill': 6, 'staff': 1, 'duration': 2, 'day': 6 },
#     {'title': 'Adaptive optics system validation', 'skill': 7, 'staff': 1, 'duration': 3, 'day': 6 },
#     {'title': 'Cryogenic system checks', 'skill': 8, 'staff': 2, 'duration': 2, 'day': 6 },
#     {'title': 'Preparing dome and telescope for night operations', 'skill': 3, 'staff': 1, 'duration': 2, 'day': 6 },
#     {'title': 'Monitoring weather and system status', 'skill': 12, 'staff': 1, 'duration': 1, 'day': 6 },
#     {'title': 'Drives and dome troubleshooting', 'skill': 1, 'staff': 1, 'duration': 3, 'day': 6 },
#     {'title': 'Nightly telescope operation', 'skill': 3, 'staff': 1, 'duration': 6, 'day': 6 },
#     {'title': 'Instrument calibration', 'skill': 4, 'staff': 2, 'duration': 3, 'day': 6 },
#     {'title': 'Assembly and testing of mechanical fixtures', 'skill': 1, 'staff': 2, 'duration': 2, 'day': 6 }
# ]

# # Skill scores for each staff member
# Staff = [
#     [0,13.3,0,14.9,11.4,19.6,0,0,2.2,7.6,13.7,7.6,21.3,2.8,0],
#     [0,1.9,0,10.7,5.3,14.7,2.2,11.8,0,0,7.5,19.4,0,27.1,14.5],
#     [15.9,7.8,9.8,15.7,1.6,0,7.1,0,1.5,3.3,6.1,7.8,10.1,15.1,11.0],
#     [21.2,1.6,1.1,2.0,19.0,10.4,2.2,10.8,5.2,4.0,6.4,11.7,3.3,3.5,2.9],
#     [6.2,1.8,1.3,11.8,21.8,1.5,11.0,7.1,5.3,6.8,3.9,0,1.6,14.6,10.3],
#     [3.1,5.5,11.0,0,7.3,6.5,2.7,9.6,2.2,6.6,9.8,17.3,10.1,1.3,11.0],
#     [0,3.9,3.2,2.5,11.7,9.8,7.1,7.2,9.6,3.1,5.9,5.4,0,17.6,21.0],
#     [3.5,10.8,7.7,1.6,15.9,2.1,9.0,10.2,1.9,3.3,0,7.9,17.8,6.5,11.8],
#     [3.2,9.4,23.9,5.7,1.4,0,9.3,1.3,6.4,10.4,2.7,3.2,7.7,6.0,14.9],
#     [5.7,6.0,15.9,0,15.7,9.8,7.7,0,9.5,9.8,1.8,5.8,5.0,13.3,0],
#     [0,6.9,5.7,11.5,11.8,17.0,15.2,11.8,2.7,1.3,7.0,1.1,2.6,2.1,11.7],
#     [7.7,1.3,5.1,15.6,17.5,18.7,0,1.9,2.0,0,10.0,10.0,0,7.8,10.8],
#     [5.8,22.3,13.6,1.5,2.7,9.6,3.5,0,1.7,6.5,1.2,15.3,3.4,15.8,2.6]
# ]

# S = range(len(Skills))
# J = range(len(Tasks))
# I = range(len(Staff))

# forbidden_staff_pairs = [(1,5), (8,9), (2,3), (7,12)]

""" """







# Constraints setup


maxWorkDays = 5
maxDailyHours = 10
maxWeeklyHours = 36

model = gp.Model("A2 - Ancestral")

# Decision variables
TA = model.addVars(I, J, vtype=gp.GRB.BINARY, name="TA")
TH = model.addVars(J, lb=0.0, vtype=gp.GRB.CONTINUOUS, name="TH")
SS = model.addVars(I, lb=0.0, vtype=gp.GRB.CONTINUOUS, name="SS")
WH = {(i, t): model.addVar() for i in I for t in T}

WorkDay = model.addVars(I, T, vtype=gp.GRB.BINARY, name="WorkDay")

C = {}

# Duration constraint
C["Duration"] = model.addConstrs(
    (TH[j] == Tasks[j]["duration"] * gp.quicksum(TA[i, j] for i in I) for j in J)
)

# Training variables
Train = model.addVars(I, S, vtype=gp.GRB.BINARY, name="Train")

C["OneTrainPerStaff"] = model.addConstrs(
    (gp.quicksum(Train[i, s] for s in S) <= 1 for i in I)
)

C["MaxTotalTrainings"] = model.addConstr(
    gp.quicksum(Train[i, s] for i in I for s in S) <= 5
)

# Linearization
U = model.addVars(I, J, vtype=gp.GRB.BINARY, name="U")


def task_skill_index(j):
    return Tasks[j]["skill"]


C["Skills"] = model.addConstrs(
    (
        SS[i]
        == gp.quicksum(
            Staff[i][task_skill_index(j)] * TA[i, j] + 7 * U[i, j]
            for j in J
        )
        for i in I
    )
)

for i in I:
    for j in J:
        k = task_skill_index(j)
        model.addConstr(U[i, j] <= TA[i, j])
        model.addConstr(U[i, j] <= Train[i, k])
        model.addConstr(U[i, j] >= TA[i, j] + Train[i, k] - 1)

# Assignment constraint
C["StaffAssignment"] = model.addConstrs(
    (gp.quicksum(TA[i, j] for i in I) == Tasks[j]["staff"] for j in J)
)

# Objective
model.setObjective(gp.quicksum(SS[i] for i in I), gp.GRB.MAXIMIZE)

model.optimize()

if model.status == gp.GRB.OPTIMAL:
    print("Optimal task assignments:")
    for j in J:
        assigned = [i for i in I if TA[i, j].X > 0.5]
        print(f"{Tasks[j]['title']} {Tasks[j]['day']} {assigned}")

    print("\nTotal skill utilization:", sum(SS[i].X for i in I))

print(model.ObjVal)