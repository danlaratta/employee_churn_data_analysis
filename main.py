from etl import clean_employee_data, clean_store_data, get_raw_data, export_dfs, load_to_postgres

# Pipeline Runner
def main():
    # Extract
    raw_data = get_raw_data()

    # Clean
    employee_data = clean_employee_data(raw_data)
    store_data = clean_store_data(raw_data)
    dataframes = {'employee': employee_data, 'store': store_data}

    # Export and Load
    export_dfs(dataframes, 'data/cleaned', '.csv', False)
    load_to_postgres(dataframes)

if __name__ == '__main__':
    main()