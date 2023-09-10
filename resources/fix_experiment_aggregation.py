import os
import pandas as pd
import numpy as np

def list_subdir(dir):
    return [f for f in os.listdir(dir) if os.path.isdir(os.path.join(dir, f))]

def preprocess_values(df):
    df['Timestamp'] = df['Timestamp'] - df['Timestamp'][0]
    # conversion from microseconds to seconds
    df['Timestamp'] = df['Timestamp'] / 1000
    return df

def calculate_power(df):
    df['power'] = (abs(df['BATTERY_PROPERTY_CURRENT_NOW']) / 1000 / 1000) * (df['EXTRA_VOLTAGE'] / 1000)
    return df

def trapezoid_method(df):
    return np.trapz(df['power'].values, df['Timestamp'].values)

def aggregate_batterymanager_runs(logs_dir):
    runs = pd.DataFrame()
    run_number = 0
    for run_file in [f for f in os.listdir(logs_dir) if os.path.isfile(os.path.join(logs_dir, f))]:
        f_name = os.path.join(logs_dir, run_file)
        if not f_name.endswith(".csv"):
            continue
        run_df = pd.read_csv(f_name)

        stats = {}
        if 'BATTERY_PROPERTY_CURRENT_NOW' in run_df.columns and 'EXTRA_VOLTAGE' in run_df.columns:
            run_df = preprocess_values(run_df)
            run_df = calculate_power(run_df)
            avg_power = run_df['power'].mean()
            stats.update({'Avg power (W)': avg_power})
            stats.update({'Energy simple (J)': avg_power * run_df['Timestamp'].max()})
            stats.update({'Energy trapz (J)': trapezoid_method(run_df)})
        stats.update(run_df.mean().to_dict())
        stats.update({'run': run_number})
        run_number += 1

        runs = pd.concat([runs, pd.DataFrame(stats, index=[0])], ignore_index=True)

    runs = runs.drop(columns=['Timestamp', 'power'], axis=1)
    return runs

def aggregate(data_dir):
    df = pd.DataFrame()
    for device in list_subdir(data_dir):
        device_dir = os.path.join(data_dir, device)
        for subject in list_subdir(device_dir):
            subject_dir = os.path.join(device_dir, subject)
            if os.path.isdir(os.path.join(subject_dir, 'batterymanager')):
                runs_df = aggregate_batterymanager_runs(os.path.join(subject_dir, 'batterymanager'))
                runs_df['subject'] = subject
                runs_df['device'] = device
                df = pd.concat([df, runs_df], ignore_index=True)
    return df[df.columns[::-1]]

def aggregate_end(data_dir, output_file):
    print(('Output file: {}'.format(output_file)))
    rows = aggregate(data_dir)
    rows.to_csv(output_file, index=False)

aggregate_end('./data/Pixel3-W/Experiment100/batch4/output/2023.07.04_164236/data',\
              './data/Pixel3-W/Experiment100/batch4/output/2023.07.04_164236/Aggregated_Results_Batterymanager.csv')