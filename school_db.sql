USE school_db;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id VARCHAR(50) NOT NULL UNIQUE,
    name VARCHAR(100) NOT NULL,
    grade VARCHAR(10) NOT NULL,
    email VARCHAR(100) NOT NULL,
    profile_picture VARCHAR(255),
    password VARCHAR(255) NOT NULL
);
