-- Create a new database with a new user with select privileges
-- The user_0d_2 password should be set to user_0d_2_pwd
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS user_0d_2@localhost;
SET PASSWORD FOR user_0d_2@localhost = 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2 . * TO user_0d_2@localhost;
FLUSH PRIVILEGES;
