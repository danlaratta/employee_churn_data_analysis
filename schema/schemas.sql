
CREATE TABLE store (
    store_id INT PRIMARY KEY,
    city_name TEXT NOT NULL,
    department_name TEXT NOT NULL,
);

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    job_title TEXT NOT NULL,
    gender TEXT NOT NULL,
    date_hired DATE NOT NULL,
    date_terminated DATE,
    service_length INT NOT NULL,
    year_snapshot_record DATE NOT NULL,
    employee_status TEXT NOT NULL,
    status_year INT NOT NULL,
);
