
CREATE TABLE store (
    store_id INT PRIMARY KEY,
    city TEXT NOT NULL,
    department TEXT NOT NULL,
);

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    job_title TEXT NOT NULL,
    age INT NOT NULL,
    gender TEXT NOT NULL,
    date_hired DATE NOT NULL,
    date_terminated DATE,
    years_employed INT NOT NULL,
    snapshot_record_year DATE NOT NULL,
    employee_status TEXT NOT NULL,
    status_year INT NOT NULL,
);
