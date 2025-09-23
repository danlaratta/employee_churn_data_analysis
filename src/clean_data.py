import pandas as pd 

def clean_store_data(df: pd.DataFrame) -> pd.DataFrame:
    # lowercase all column names
    df.columns = df.columns.str.lower()

    # drop non-store columns
    df.drop([
        'employeeid', 'recorddate_key', 'birthdate_key', 'orighiredate_key', 'terminationdate_key', 'age', 'length_of_service', 
        'job_title', 'gender_short', 'gender_full', 'termreason_desc', 'termtype_desc', 'status_year', 'status', 'business_unit'
    ])

    # rename columns
    df.rename(columns={
        'department_name': 'department',
        'city_name': 'city',
        'store_name': 'store_id',
    })

    return df


def clean_employee_data(df: pd.DataFrame) -> None:
    # lowercase all column names
    df.columns = df.columns.str.lower()

    # drop non-store columns
    df.drop([
        'birthdate_key', 'gender_full', 'termreason_desc', 'termtype_desc', 
        'business_unit', 'department_name', 'city_name', 'store_name'
    ])

    # rename columns
    df.rename(columns={
        'employeeid' : 'employee_id',
        'recorddate_key' : 'snapshot_date',
        'orighiredate_key' : 'date_hired',
        'terminationdate_key' : 'date_terminated',
        'length_of_service' : 'years_employed',
        'gender_short' : 'gender',
        'status_year' : '',
        'status' : 'employee_status',
    })

    # Replace incorrect date with None
    df['date_terminated'] = df['date_terminated'].replace('1/1/1900', None)

    # Fix date data type
    cols = ['snapshot_date', 'date_hired', 'date_terminated']
    df[cols] = df[cols].apply(lambda x: pd.to_datetime(x, format='%m/%d/%Y'))
