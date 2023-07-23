import pandas as pd
import os
import matplotlib.pyplot as plt

def read_csv_files_in_folder(folder_path):
    csv_data = []

    # Get a list of files in the folder
    files = os.listdir(folder_path)

    for file in files:
        if file.endswith('.csv'):
            file_path = os.path.join(folder_path, file)
            df = pd.read_csv(file_path, sep='|')
            csv_data.append(df)

    return csv_data

# Function to plot the SRP dynacard graph
def plot_dynacard(surface_positions, surface_loads):
    plt.figure(figsize=(10, 6))
    plt.plot(surface_positions, surface_loads, marker='o', linestyle='-')
    plt.xlabel('Surface Position')
    plt.ylabel('Surface Load')
    plt.title('SRP Dynacard')
    plt.grid(True)
    plt.show()

# Function to identify dynacard problems
def identify_dynacard_problems(surface_loads, strokes_per_minute):
    # Implement your pattern recognition algorithm here
    # For simplicity, let's assume we have the SPM value available
    if strokes_per_minute < 8:
        return "Full load production & SPM < 8"
    elif strokes_per_minute > 3:
        return "Insufficient liquid supply & SPM > 3"
    else:
        if 0 in surface_loads:
            return "Stuck traveling valve"
        elif any(load < 0 for load in surface_loads):
            return "Tubing leak"
        elif all(load == 0 for load in surface_loads):
            return "Gas interference & gas lock"
        else:
            return "No significant problems identified."

# Function to provide troubleshooting suggestions
def provide_troubleshooting_suggestions(problem):
    # Provide suggestions based on identified problems
    if problem == "Full load production & SPM < 8":
        return ["Increase pump speed", "Increase stroke length"]
    elif problem == "Insufficient liquid supply & SPM > 3":
        return ["Decrease pump speed", "Decrease stroke length"]
    elif problem == "Stuck traveling valve":
        return [
            "If it is a new startup, wait for fluid to reach the surface.",
            "Check for fluid flow at the surface.",
            "Check for free-flowing well.",
            "Re-seat pump."
        ]
    elif problem == "Tubing leak":
        return [
            "If it is a new startup, wait for fluid to reach the surface.",
            "Check for fluid flow at the surface.",
            "Check for tubing leak."
        ]
    elif problem == "Gas interference & gas lock":
        return [
            "Re-space the pump lower to increase pump compression ratio.",
            "Improve gas separation.",
            "Increase plunger clearance to increase slippage."
        ]
    else:
        return []

if __name__ == "__main__":
    folder_path = "csv_file"  # Change to your folder path containing CSV files
    data = read_csv_files_in_folder(folder_path)

    for df in data:
        # Extract relevant columns for dynacard graph (Surface Positions, Surface Loads)
        surface_positions, surface_loads = df['Surface Positions'].tolist(), df['Surface Loads'].tolist()

        # Plot the dynacard graph
        plot_dynacard(surface_positions, surface_loads)

        # Identify dynacard problems (Assuming SPM value available, replace 9.09090909090909 with the actual SPM value)
        problem = identify_dynacard_problems(surface_loads, 9.09090909090909)

        # Provide troubleshooting suggestions
        suggestions = provide_troubleshooting_suggestions(problem)
        print("Dynacard Problem: ", problem)
        print("Troubleshooting Suggestions: ", suggestions)
