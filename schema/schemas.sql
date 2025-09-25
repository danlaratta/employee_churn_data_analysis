CREATE TABLE store (
    store_id INT PRIMARY KEY,
    city TEXT NOT NULL,
    department TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS employees (
    employee_id INT NOT NULL,
    store_id INT NOT NULL,
    job_title TEXT NOT NULL,
    age INT NOT NULL,
    gender TEXT NOT NULL,
    date_hired DATE NOT NULL,
    date_terminated DATE,
    years_employed INT NOT NULL,
    snapshot_record_year DATE NOT NULL,
    employee_status TEXT NOT NULL,
    status_year INT NOT NULL,
    PRIMARY KEY (employee_id, snapshot_record_year), -- Composite primary key
    FOREIGN KEY (store_id) REFERENCES store(store_id)
);