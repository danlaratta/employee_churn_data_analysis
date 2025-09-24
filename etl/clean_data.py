import pandas as pd 

def clean_store_data(df: pd.DataFrame) -> pd.DataFrame:
    # make copy of df, don't mutate the df passed in
    df = df.copy() 

    # lowercase all column names
    df.columns = df.columns.str.lower()

    # drop non-store columns
    df = df.drop([
        'employeeid', 'recorddate_key', 'birthdate_key', 'orighiredate_key', 'terminationdate_key', 'age', 'length_of_service', 
        'job_title', 'gender_short', 'gender_full', 'termreason_desc', 'termtype_desc', 'status_year', 'status', 'business_unit'
    ], axis=1)

    # rename columns
    df = df.rename(columns={
        'department_name': 'department',
        'city_name': 'city',
        'store_name': 'store_id',
    })

    return df


def clean_employee_data(df: pd.DataFrame) -> pd.DataFrame:
    # make copy of df, don't mutate the df passed in
    df = df.copy() 

    # lowercase all column names
    df.columns = df.columns.str.lower()

    # drop non-store columns
    df = df.drop([
        'birthdate_key', 'gender_full', 'termreason_desc', 'termtype_desc', 
        'business_unit', 'department_name', 'city_name', 'store_name'
    ])

    # rename columns
    df = df.rename(columns={
        'employeeid' : 'employee_id',
        'recorddate_key' : 'snapshot_record_year',
        'orighiredate_key' : 'date_hired',
        'terminationdate_key' : 'date_terminated',
        'length_of_service' : 'years_employed',
        'gender_short' : 'gender',
        'status' : 'employee_status',
    }, axis=1)

    # Replace incorrect date with None
    df['date_terminated'] = df['date_terminated'].replace('1/1/1900', None)

    # Fix date data type
    cols = ['snapshot_date', 'date_hired', 'date_terminated']
    df[cols] = df[cols].apply(lambda x: pd.to_datetime(x, format='%m/%d/%Y'))

    return df
