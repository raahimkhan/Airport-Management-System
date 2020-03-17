DROP DATABASE IF EXISTS airline;
CREATE DATABASE airline ;
USE airline ;

DROP TABLE IF EXISTS ADMIN ;
CREATE TABLE ADMIN 
(
    admin_id int NOT NULL,
    admin_name varchar(25) NOT NULL,
    password varchar(25) NOT NULL,
    PRIMARY KEY (admin_id)
) ;

DROP TABLE IF EXISTS RECEPTIONIST;
CREATE TABLE RECEPTIONIST 
(
    receptionist_id int NOT NULL,
    receptionist_name varchar(25) NOT NULL,
    password varchar(25) NOT NULL,
    PRIMARY KEY (receptionist_id)
) ;

DROP TABLE IF EXISTS PASSENGER;
CREATE TABLE PASSENGER 
(
    passenger_id bigint NOT NULL,
    passenger_name varchar(25) NOT NULL,
    address varchar(255) NOT NULL,
    phone bigint NOT NULL,
    nationality varchar(255) NOT NULL,
    PRIMARY KEY (passenger_id)
) ;

DROP TABLE IF EXISTS FLIGHT;
CREATE TABLE FLIGHT
(
    flight_id varchar(25) NOT NULL,
    departure_airport varchar(25) NOT NULL,
    arrival_airport varchar(25) NOT NULL,
    departure_time time NOT NULL,
    arrival_time time NOT NULL,
    departure_date date NOT NULL,
    airplane varchar(25) NOT NULL,
    fare int NOT NULL,
    PRIMARY KEY (flight_id)
) ;

DROP TABLE IF EXISTS TICKET_HISTORY;
CREATE TABLE TICKET_HISTORY 
(
    ticket_id int NOT NULL AUTO_INCREMENT,
    flight_id varchar(25) NOT NULL,
    passenger_id bigint NOT NULL,
    seat_number int NOT NULL,
    booking_date date NOT NULL,
    PRIMARY KEY (ticket_id),

    CONSTRAINT FK_passenger_id FOREIGN KEY (passenger_id)
    REFERENCES PASSENGER(passenger_id) ON DELETE CASCADE,

    CONSTRAINT FK_flight_id FOREIGN KEY (flight_id)
    REFERENCES FLIGHT(flight_id) ON DELETE CASCADE
    -- FOREIGN KEY (passenger_id) REFERENCES PASSENGER (passenger_id) ON DELETE CASCADE,
    -- FOREIGN KEY (flight_id) REFERENCES FLIGHT (flight_id) ON DELETE CASCADE
) ;

INSERT INTO ADMIN VALUES (1, 'raahim', 'admin1') ;
INSERT INTO ADMIN VALUES (2, 'ali', 'admin2') ;
INSERT INTO ADMIN VALUES (3, 'ahad', 'admin3') ;
INSERT INTO ADMIN VALUES (4, 'usman', 'admin4') ;
INSERT INTO ADMIN VALUES (5, 'aashir', 'admin5') ;

INSERT INTO RECEPTIONIST VALUES (1, 'maham', 'rec1') ;
INSERT INTO RECEPTIONIST VALUES (2, 'muzammil', 'rec2') ;
INSERT INTO RECEPTIONIST VALUES (3, 'harum', 'rec3') ;
INSERT INTO RECEPTIONIST VALUES (4, 'humayun', 'rec4') ;
INSERT INTO RECEPTIONIST VALUES (5, 'mahad', 'rec5') ;

INSERT INTO PASSENGER (passenger_id, passenger_name, address, phone, nationality) VALUES ('3520290551055', 'Raahim Khan', 'LUMS', '03084352787', 'pakistani');
INSERT INTO PASSENGER (passenger_id, passenger_name, address, phone, nationality) VALUES ('3520290551076', 'Ahmed Farhan', 'FAST', '03084352786', 'indian');
INSERT INTO PASSENGER (passenger_id, passenger_name, address, phone, nationality) VALUES ('3520290551067', 'Ramez Salman', 'NUST', '03084352785', 'american');
INSERT INTO PASSENGER (passenger_id, passenger_name, address, phone, nationality) VALUES ('3520290551048', 'Hamza Farooq', 'GIKI', '03084352784', 'bangladesi');
INSERT INTO PASSENGER (passenger_id, passenger_name, address, phone, nationality) VALUES ('3520290551039', 'Aiyan Tufail', 'PIEAS', '03084352783', 'srilankan');
INSERT INTO PASSENGER (passenger_id, passenger_name, address, phone, nationality) VALUES ('3520290551025', 'Zoraiz Qureshi', 'UET', '03084352782', 'british');
INSERT INTO PASSENGER (passenger_id, passenger_name, address, phone, nationality) VALUES ('3520290551015', 'Farrukh Rasool', 'HARVARD', '03084352187', 'algerian');
INSERT INTO PASSENGER (passenger_id, passenger_name, address, phone, nationality) VALUES ('3520290551078', 'Bilal Rizwan', 'CAMBRIDGE', '03084352787', 'argentine');
INSERT INTO PASSENGER (passenger_id, passenger_name, address, phone, nationality) VALUES ('3520290551046', 'Nawaz Sharif', 'MIT', '03084352747', 'albanian');
INSERT INTO PASSENGER (passenger_id, passenger_name, address, phone, nationality) VALUES ('3520290551011', 'Salman Ayub', 'DHA', '03084353787', 'antiguan');
INSERT INTO PASSENGER (passenger_id, passenger_name, address, phone, nationality) VALUES ('4520290551011', 'Shahrukh Khan', 'PIA', '03084567787', 'indian');
INSERT INTO PASSENGER (passenger_id, passenger_name, address, phone, nationality) VALUES ('5520290551011', 'James Bond', 'MODEL TOWN', '03083463787', 'british');
INSERT INTO PASSENGER (passenger_id, passenger_name, address, phone, nationality) VALUES ('6520290551011', 'John Cena', 'CANTT', '03084973787', 'african');

INSERT INTO FLIGHT (flight_id, departure_airport, arrival_airport, departure_time, arrival_time, departure_date, airplane, fare) VALUES ('PK100', 'LHR', 'KHI', '10:50:11', '14:10:12', '2019-01-10','BOEING787', '5000') ;
INSERT INTO FLIGHT (flight_id, departure_airport, arrival_airport, departure_time, arrival_time, departure_date, airplane, fare) VALUES ('PK101', 'LHR', 'ISB', '23:20:11', '06:11:45', '2019-01-10','SR-71', '1500') ;
INSERT INTO FLIGHT (flight_id, departure_airport, arrival_airport, departure_time, arrival_time, departure_date, airplane, fare) VALUES ('PK102', 'ISB', 'LHR', '00:00:00', '09:00:00', '2019-01-10','JUMPJET', '6500') ;
INSERT INTO FLIGHT (flight_id, departure_airport, arrival_airport, departure_time, arrival_time, departure_date, airplane, fare) VALUES ('PK103', 'LHR', 'KHI', '13:01:06', '16:00:00', '2019-01-10','HYDRA55', '2500') ;
INSERT INTO FLIGHT (flight_id, departure_airport, arrival_airport, departure_time, arrival_time, departure_date, airplane, fare) VALUES ('PK104', 'HDD', 'JAG', '11:26:11', '17:10:11', '2019-05-26','LEARJET23', '4500') ;
INSERT INTO FLIGHT (flight_id, departure_airport, arrival_airport, departure_time, arrival_time, departure_date, airplane, fare) VALUES ('PK105', 'LHR', 'KHI', '17:00:00', '18:30:00', '2019-06-09','DOUGLAS3', '1000') ;
INSERT INTO FLIGHT (flight_id, departure_airport, arrival_airport, departure_time, arrival_time, departure_date, airplane, fare) VALUES ('PK106', 'GWD', 'FSD', '20:01:11', '23:10:11', '2019-07-11','CESSNA172', '1200') ;
INSERT INTO FLIGHT (flight_id, departure_airport, arrival_airport, departure_time, arrival_time, departure_date, airplane, fare) VALUES ('PK107', 'GWD', 'FSD', '21:01:11', '21:25:11', '2019-07-11','GULFSTREAM', '3700') ;
INSERT INTO FLIGHT (flight_id, departure_airport, arrival_airport, departure_time, arrival_time, departure_date, airplane, fare) VALUES ('PK108', 'CJL', 'CHB', '08:00:00', '09:00:00', '2019-09-10','BELLX1', '500') ;
INSERT INTO FLIGHT (flight_id, departure_airport, arrival_airport, departure_time, arrival_time, departure_date, airplane, fare) VALUES ('PK109', 'BHV', 'BNP', '05:00:39', '08:24:56', '2019-10-17','AIRBUS', '3100') ;
INSERT INTO FLIGHT (flight_id, departure_airport, arrival_airport, departure_time, arrival_time, departure_date, airplane, fare) VALUES ('PK110', 'ISB', 'LHR', '02:00:39', '11:24:56', '2019-01-10','BOEING787', '5500') ;
INSERT INTO FLIGHT (flight_id, departure_airport, arrival_airport, departure_time, arrival_time, departure_date, airplane, fare) VALUES ('PK111', 'GWD', 'FSD', '05:00:39', '08:24:56', '2019-07-11','AIRBUS', '3100') ;
INSERT INTO FLIGHT (flight_id, departure_airport, arrival_airport, departure_time, arrival_time, departure_date, airplane, fare) VALUES ('PK112', 'LHR', 'ISB', '05:00:39', '08:24:56', '2019-01-10','HYDRA55', '7500') ;


INSERT INTO TICKET_HISTORY (flight_id, passenger_id, seat_number, booking_date) VALUES ('PK100', '3520290551055', 12, '2019-01-08') ;
INSERT INTO TICKET_HISTORY (flight_id, passenger_id, seat_number, booking_date) VALUES ('PK101', '3520290551076', 13, '2019-01-17') ;
INSERT INTO TICKET_HISTORY (flight_id, passenger_id, seat_number, booking_date) VALUES ('PK102', '3520290551067', 14, '2019-01-05') ;
INSERT INTO TICKET_HISTORY (flight_id, passenger_id, seat_number, booking_date) VALUES ('PK103', '3520290551048', 15, '2019-04-14') ;
INSERT INTO TICKET_HISTORY (flight_id, passenger_id, seat_number, booking_date) VALUES ('PK104', '3520290551039', 16, '2019-05-21') ;
INSERT INTO TICKET_HISTORY (flight_id, passenger_id, seat_number, booking_date) VALUES ('PK105', '3520290551025', 17, '2019-06-05') ;
INSERT INTO TICKET_HISTORY (flight_id, passenger_id, seat_number, booking_date) VALUES ('PK106', '3520290551015', 18, '2019-07-10') ;
INSERT INTO TICKET_HISTORY (flight_id, passenger_id, seat_number, booking_date) VALUES ('PK107', '3520290551078', 19, '2019-08-23') ;
INSERT INTO TICKET_HISTORY (flight_id, passenger_id, seat_number, booking_date) VALUES ('PK108', '3520290551046', 20, '2019-09-01') ;
INSERT INTO TICKET_HISTORY (flight_id, passenger_id, seat_number, booking_date) VALUES ('PK109', '3520290551011', 25, '2019-10-13') ;
INSERT INTO TICKET_HISTORY (flight_id, passenger_id, seat_number, booking_date) VALUES ('PK110', '3520290551055', 11, '2019-01-02') ;
INSERT INTO TICKET_HISTORY (flight_id, passenger_id, seat_number, booking_date) VALUES ('PK101', '3520290551067', 34, '2019-01-13') ;
INSERT INTO TICKET_HISTORY (flight_id, passenger_id, seat_number, booking_date) VALUES ('PK105', '3520290551015', 28, '2019-05-28') ;
