CREATE USER app_user WITH ENCRYPTED PASSWORD 'app_pass';
CREATE DATABASE app_db;
GRANT ALL PRIVILEGES ON DATABASE app_db TO app_user;