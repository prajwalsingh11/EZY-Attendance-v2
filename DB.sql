create database Ftest;
CREATE TABLE regteach (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    ss_que VARCHAR(255) NOT NULL,
    s_ans VARCHAR(255) NOT NULL,
    pwd VARCHAR(255)
);

INSERT INTO regteach (email, password, ss_que, s_ans, pwd) 
VALUES 
('kishnuyadav783@gmail.com', '6136', 'Your Date of Birth', '01/01/1990', NULL),
('example@example.com', 'example123', 'Your Nick Name', 'Nickname', NULL),
('test@test.com', 'test123', 'Your Favorite Book', 'Book', NULL);

