--Example Database
--Create Cars table
CREATE TABLE Cars(
    ID INT PRIMARY KEY,
    Brand VARCHAR(50),
    Model VARCHAR(50),
    Year INT,
    Color VARCHAR(20)
);

--Insert data into Cars table
INSERT INTO Cars (ID, Brand, Model, Year, Color) VALUES
(1, 'Toyota', 'Corolla', 2020, 'White'),
(2, 'Honda', 'Civic', 2019, 'Grey'),
(3, 'Ford', 'Mustang', 2021, 'Red'),
(4, 'BMW', '3 Series', 2022, 'Black'),
(5, 'Mercedes', 'E Class', 2023, 'Blue'),
(6, 'Audi', 'A4', 2021, 'White'),
(7, 'Chevrolet', 'Camaro', 2022, 'Yellow'),
(8, 'Hyundai', 'Elantra', 2023, 'Silver'),
(9, 'Nissan', 'Altima', 2023, 'Green'),
(10, 'Subaru', 'Forester', 2022, 'Red'),
(11, 'Kia', 'Sorento', 2023, 'Blue'),
(12, 'Jeep', 'Cherokee', 2021, 'Black'),
(13, 'Mazda', 'CX-5', 2022, 'White'),
(14, 'Hyundai', 'Tucson', 2023, 'Silver'),
(15, 'Volkswagen', 'Passat', 2021, 'Grey'),
(16, 'Audi', 'Q5', 2022, 'Blue'),
(17, 'Mercedes', 'C Class', 2023, 'Black'),
(18, 'BMW', '5 Series', 2021, 'White'),
(19, 'Toyota', 'Camry', 2022, 'Silver'),
(20, 'Honda', 'Accord', 2023, 'Grey');
