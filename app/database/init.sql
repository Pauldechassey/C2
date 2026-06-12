-- init.sql
CREATE ENUM command_status AS (
    'PENDING',
    'DONE',
    'FAILED'
);

CREATE TABLE IF NOT EXISTS commands (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    command TEXT NOT NULL,
    output TEXT,
    order INTEGER NOT NULL,
    status command_status NOT NULL DEFAULT 'PENDING',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
