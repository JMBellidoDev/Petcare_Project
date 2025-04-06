update pet set image = decode('', 'hex') where pet.id = 35;
select * from client_pets cp ;

INSERT INTO app_user (username, hashed_password, email, enabled, role)
VALUES 
('user_12345', '$2b$12$NlJiZ6evAKUvHVy5/MWDLexFw5Y5Mg.XOpGIpREchvr3xz9tUoTke', 'user12345@example.com', true, 'client'), -- Password: 'Password1!'
('vet_clinic_1', '$2b$12$fngVg6zSxh45AKxbKnO3VubJ9xXjCneET2vNFSu7jDU3F1VVCNMUy', 'vet_clinic_1@example.com', true, 'vet_entity'), -- Password: 'VetClinic#1'
('veterinario_1', '$2b$12$QqHo0Ht8iZpUAanyxDgJKeujrZJqP7nQSZG9JLsBBmVSSxGfz/zIG', 'veterinario1@example.com', true, 'vet'), -- Password: 'VetPass#2023'
('cliente_54321', '$2b$12$irDfNC6OQcYjzgucAuw2C.dGVzI/Hn8tz.PN4RCcVgJOfoxjjndva', 'cliente54321@example.com', true, 'client'), -- Password: 'Client_321'
('vet_clinic_2', '$2b$12$uvl7GSeQ7ddiEAXVAkIf5.Ik55yZcBBRhCmTCWMj.R5l6kXVII.R6', 'vet_clinic_2@example.com', true, 'vet_entity'); -- Password: 'ClinicPass!2'

INSERT INTO vet_entity (id, name, cif, address, phone_number)
VALUES 
(2, 'Clinica Veterinaria Central', 'A12345678', 'Calle Mayor 123, Madrid, España', '915123456'),
(5, 'Centro Veterinario Sur', 'B87654321', 'Avenida del Sur 45, Sevilla, España', '954987654');

INSERT INTO vet (id, national_id_document, name, registration_number, vet_entity_id)
VALUES 
(3, '12345678X', 'Luis Perez Sanchez', 'REG123456', 2);

INSERT INTO client (id, national_id_document, name, birthdate, address, phone_number)
VALUES 
(1, '98765432L', 'Carlos Fernandez Lopez', '1980-05-15', 'Calle de la Paz 67, Valencia, España', '963852741'),
(4, 'X7654321Y', 'Maria Torres Garcia', '1995-10-10', 'Gran Via 45, Barcelona, España', '931234567');

INSERT INTO pet (chip_number, type, breed, name, birthdate, alive, castrated)
VALUES 
('CHIP001', 'dog', 'Labrador Retriever', 'Max', '2015-08-01', true, true),
('CHIP002', 'cat', 'Siamese', 'Mia', '2017-04-12', true, false),
('CHIP003', 'ferret', 'Standard', 'Fiona', '2018-03-23', true, false),
('CHIP004', 'horse', 'Andalusian', 'Spirit', '2010-07-15', true, true),
('CHIP005', 'rabbit', 'Dutch', 'Bunny', '2019-09-30', true, false);

INSERT INTO client_pets (pet_id, client_id, show)
VALUES 
(1, 1, true), -- Max es la mascota de Carlos Fernandez Lopez
(2, 4, true), -- Mia es la mascota de Maria Torres Garcia
(3, 1, true), -- Fiona es la mascota de Carlos Fernandez Lopez
(4, 4, true), -- Spirit es la mascota de Maria Torres Garcia
(5, 1, true); -- Bunny es la mascota de Carlos Fernandez Lopez

INSERT INTO report (pet_id, vet_id, reason, diagnosis, treatment, report_date)
VALUES 
(1, 3, 'Dolor abdominal', 'Gastritis leve', 'Dieta blanda y antiácidos', '2023-05-10 14:30:00'),
(2, 3, 'Picazón excesiva', 'Alergia a pulgas', 'Tratamiento antipulgas', '2023-06-12 11:00:00'),
(3, 3, 'Pérdida de apetito', 'Estomatitis', 'Antiinflamatorio y antibióticos', '2023-04-05 16:00:00'),
(4, 3, 'Cojea de la pata trasera', 'Desgarro muscular', 'Reposo y fisioterapia', '2023-07-20 09:00:00'),
(5, 3, 'Pérdida de peso', 'Infección parasitaria', 'Antiparasitarios', '2023-08-15 13:45:00');

INSERT INTO appointment (pet_id, vet_id, client_id, appointment_date)
VALUES 
(1, 3, 1, '2024-09-15 10:00:00'),
(2, 3, 4, '2024-10-05 12:30:00'),
(3, 3, 1, '2024-09-20 15:00:00'),
(4, 3, 4, '2024-11-02 09:30:00'),
(5, 3, 1, '2024-12-12 11:00:00');

INSERT INTO app_user (username, hashed_password, email, enabled, role)
VALUES 
('user_23456', '$2b$12$8wUdMha3ii8bkFCu4MOzzuB4N/1MHG8J2p7odRi2E2z5i7mUqIgUe', 'user23456@example.com', true, 'client'), -- Password: 'ClientPass#1'
('user_34567', '$2b$12$cYQt3emEOSgPvoNiuD.Vne6igcPzgbXCTfgCpmFQ49THcm5WzPf/m', 'user34567@example.com', true, 'client'), -- Password: 'ClientPass#2'
('user_45678', '$2b$12$fzTmEOElk/pFIGhXL5Ngl.B8ZlgdnJR1OiVhW9vL1tVtsX5bOU5Y.', 'user45678@example.com', true, 'client'), -- Password: 'ClientPass#3'
('user_56789', '$2b$12$Q/Py2CADDZosUx/iP0uHpu4leul.Fso4QmGfMnbro.rhGlPHC9wse', 'user56789@example.com', true, 'client'), -- Password: 'ClientPass#4'
('user_67890', '$2b$12$jT33WPjSGjITLDhPI62qNuQaJKOPj8IUsVdwGIMmZqOAgojlv.Dfi', 'user67890@example.com', true, 'client'), -- Password: 'ClientPass#5'
('vet_clinic_3', '$2b$12$9Q6Pc7t/93UOceRxcpXHze4QFv4pTIsUHLk2Az6n3fKw0DPE2Qtuq', 'vet_clinic_3@example.com', true, 'vet_entity'), -- Password: 'ClinicPass#3'
('vet_clinic_4', '$2b$12$Th96gSgZl0tXW4bjQ4cx4OF8qzQuUt6VA7nyKrxS72O1Yg8U0tL5e', 'vet_clinic_4@example.com', true, 'vet_entity'), -- Password: 'ClinicPass#4'
('vet_clinic_5', '$2b$12$mrnZIt/VVq412QFSljiPCutEZfBy0pB72Z/ejC0IRud/w1n8/4qrK', 'vet_clinic_5@example.com', true, 'vet_entity'), -- Password: 'ClinicPass#5'
('vet_clinic_6', '$2b$12$W0eYtx6CgC5ZyHHOyTK9wOUFMbdMN1Fi9wU7v86dyC0X2jQaN.pxa', 'vet_clinic_6@example.com', true, 'vet_entity'), -- Password: 'ClinicPass#6'
('vet_clinic_7', '$2b$12$jzkjryT/B98jDALOUPn8v.G5AsO20JgGpIqNgo2J.paVG3LGN9vJ2', 'vet_clinic_7@example.com', true, 'vet_entity'), -- Password: 'ClinicPass#7'
('vet_2', '$2b$12$u.u7RHJcwWG2E0BYsEclAunv08OrOHPupkndki6152tcVLKI8BpEC', 'vet_2@example.com', true, 'vet'), -- Password: 'VetPass#4'
('vet_3', '$2b$12$74SEL0vsgg1Y3fzCf5ONWuHj6pfQRdEEjy.eaKvJdZESELKWLuhTy', 'vet_3@example.com', true, 'vet'), -- Password: 'VetPass#5'
('vet_4', '$2b$12$TGd3omexN4eYL/7TrWp1ku5faamzDMaoLPmkiPbInnd7HaKSeumGK', 'vet_4@example.com', true, 'vet'), -- Password: 'VetPass#6'
('vet_5', '$2b$12$88h3j8vExB694yvN7LZcMuiF0wCsiYngxqsiu7.Pn5Lpo0IY23IQ2', 'vet_5@example.com', true, 'vet'), -- Password: 'VetPass#7'
('vet_6', '$2b$12$kKUnQT3F6EZ/pxnMTaW9ruVB.kUZjee7lbP5uY/NxLjf0nH/0eJk.', 'vet_6@example.com', true, 'vet'); -- Password: 'VetPass#8'


INSERT INTO vet_entity (id, name, cif, address, phone_number)
VALUES 
(11, 'Clinica Veterinaria Norte', 'C23456789', 'Calle del Norte 8, Bilbao, España', '944112233'),
(12, 'Hospital Veterinario Este', 'D34567890', 'Calle de la Salud 25, Valencia, España', '963112233'),
(13, 'Centro Veterinario Oeste', 'E45678901', 'Paseo de la Reforma 110, Madrid, España', '911123456'),
(14, 'Veterinaria del Centro', 'F56789012', 'Calle del Prado 18, Sevilla, España', '954112233'),
(15, 'Consultorio SurVet', 'G67890123', 'Avenida de la Libertad 75, Granada, España', '958112233');



INSERT INTO vet (id, national_id_document, name, registration_number, vet_entity_id)
VALUES 
(16, '23456789Y', 'Elena Martinez Lopez', 'REG789012', 11),
(17, '34567890Z', 'Javier Rodriguez Perez', 'REG890123', 12),
(18, '45678901X', 'Laura Fernandez Ruiz', 'REG901234', 11),
(19, '56789012Y', 'David Garcia Gonzalez', 'REG012345', 11),
(20, '67890123Z', 'Sara Gomez Diaz', 'REG123457', 11);


update vet set vet_entity_id = null where id = 18;

INSERT INTO client (id, national_id_document, name, birthdate, address, phone_number)
VALUES 
(6, '87654321Z', 'Lucia Martinez Garcia', '1987-01-25', 'Avenida de los Reyes 34, Madrid, España', '913456789'),
(7, '76543210X', 'Pablo Sanchez Martinez', '1990-11-05', 'Calle de las Flores 19, Sevilla, España', '954678912'),
(8, '65432109Y', 'Carmen Alvarez Jimenez', '1985-06-10', 'Paseo del Parque 45, Malaga, España', '952345678'),
(9, '54321098Z', 'Andres Ruiz Fernandez', '1979-03-22', 'Calle del Sol 123, Valencia, España', '963456789'),
(10, '43210987X', 'Elena Moreno Lopez', '1992-12-12', 'Calle Mayor 87, Zaragoza, España', '976123456');

INSERT INTO pet (chip_number, type, breed, name, birthdate, alive, castrated)
VALUES 
('CHIP006', 'dog', 'Golden Retriever', 'Buddy', '2016-09-14', true, true),
('CHIP007', 'dog', 'Beagle', 'Charlie', '2018-01-09', true, false),
('CHIP008', 'dog', 'Bulldog', 'Rocky', '2014-11-11', true, true),
('CHIP009', 'cat', 'Persian', 'Luna', '2019-04-24', true, false),
('CHIP010', 'cat', 'British Shorthair', 'Bella', '2020-07-13', true, true),
('CHIP011', 'ferret', 'Standard', 'Whiskers', '2018-05-02', true, false),
('CHIP012', 'horse', 'Friesian', 'Shadow', '2010-02-20', true, true),
('CHIP013', 'rabbit', 'Netherland Dwarf', 'Snowball', '2021-03-05', true, false),
('CHIP014', 'dog', 'Poodle', 'Coco', '2017-08-19', true, false),
('CHIP015', 'dog', 'Doberman', 'Duke', '2015-12-22', true, true),
('CHIP016', 'cat', 'Maine Coon', 'Leo', '2016-06-16', true, true),
('CHIP017', 'ferret', 'Albino', 'Ziggy', '2021-11-30', true, false),
('CHIP018', 'horse', 'Arabian', 'Storm', '2012-09-07', true, true),
('CHIP019', 'rabbit', 'Rex', 'Fluffy', '2019-02-18', true, false),
('CHIP020', 'dog', 'Chihuahua', 'Bella', '2019-10-10', true, true),
('CHIP021', 'cat', 'Ragdoll', 'Sassy', '2022-01-05', true, false),
('CHIP022', 'dog', 'Shih Tzu', 'Milo', '2020-05-15', true, true),
('CHIP023', 'cat', 'Abyssinian', 'Simba', '2021-11-21', true, false),
('CHIP024', 'dog', 'Boxer', 'Bruno', '2014-03-30', true, true),
('CHIP025', 'horse', 'Clydesdale', 'Thunder', '2008-08-08', true, true);

INSERT INTO client_pets (pet_id, client_id, show)
VALUES 
(6, 6, true),
(7, 6, true),
(8, 7, true),
(8, 6, true),
(9, 8, true),
(10, 8, true),
(11, 7, true),
(12, 8, true),
(13, 8, true),
(14, 8, true),
(15, 9, true),
(16, 9, true),
(17, 9, true),
(18, 6, true),
(19, 6, true),
(20, 7, true),
(21, 7, true),
(22, 8, true),
(23, 7, true),
(24, 8, true),
(25, 8, true);

INSERT INTO report (pet_id, vet_id, reason, diagnosis, treatment, report_date)
VALUES 
(6, 16, 'Dolor en las articulaciones', 'Artritis', 'Suplementos y analgésicos', '2023-01-12 09:45:00'),
(7, 18, 'Vómitos', 'Gastroenteritis', 'Dieta blanda y rehidratación', '2023-02-03 10:30:00'),
(8, 16, 'Picazón en la piel', 'Alergia', 'Antihistamínicos y dieta especial', '2023-03-15 11:15:00'),
(9, 16, 'Infección en los ojos', 'Conjuntivitis', 'Colirios antibióticos', '2023-04-20 12:00:00'),
(12, 19, 'Pérdida de peso', 'Infección intestinal', 'Antibióticos y dieta alta en proteínas', '2023-05-05 13:45:00'),
(12, 18, 'Fractura en la pata', 'Fractura ósea', 'Yeso y reposo', '2023-06-22 14:30:00'),
(12, 18, 'Problemas respiratorios', 'Asma', 'Broncodilatadores y control ambiental', '2023-07-10 15:15:00'),
(13, 18, 'Pérdida de apetito', 'Parásitos internos', 'Desparasitación y dieta alta en calorías', '2023-08-05 16:00:00'),
(14, 18, 'Cojea al caminar', 'Desgarro muscular', 'Reposo y fisioterapia', '2023-09-12 17:45:00'),
(15, 18, 'Problemas de piel', 'Dermatitis', 'Tratamiento tópico y dieta especial', '2023-10-01 09:30:00'),
(16, 17, 'Dolor abdominal', 'Gastritis', 'Dieta blanda y antiácidos', '2023-11-07 10:15:00'),
(17, 17, 'Fiebre', 'Infección viral', 'Antivirales y reposo', '2023-12-22 11:00:00'),
(18, 19, 'Infección de oídos', 'Otitis', 'Antibióticos y limpieza regular', '2023-09-14 14:45:00'),
(19, 16, 'Diarrea', 'Colitis', 'Dieta blanda y probióticos', '2023-10-25 15:30:00'),
(20, 16, 'Cojea de la pata trasera', 'Luxación de cadera', 'Cirugía y rehabilitación', '2023-11-11 13:15:00');

INSERT INTO appointment (pet_id, vet_id, client_id, appointment_date)
VALUES 
(6, 16, 6, '2025-09-15 10:00:00'),
(7, 17, 8, '2025-10-05 12:30:00'),
(8, 17, 9, '2025-09-20 15:00:00'),
(9, 18, 7, '2025-11-02 09:30:00'),
(10, 19, 6, '2025-12-12 11:00:00'),
(11, 19, 9, '2025-10-20 14:00:00'),
(12, 20, 9, '2025-11-15 09:00:00'),
(13, 19, 10, '2025-12-05 13:00:00'),
(14, 18, 6, '2025-11-10 16:00:00'),
(15, 17, 6, '2025-09-25 08:00:00'),
(16, 17, 8, '2025-11-07 10:00:00'),
(17, 17, 9, '2025-12-18 12:30:00'),
(18, 18, 7, '2025-09-30 15:00:00'),
(19, 19, 6, '2025-10-15 09:30:00'),
(20, 19, 6, '2025-11-27 11:00:00'),
(6, 20, 10, '2025-10-22 09:45:00'),
(7, 20, 10, '2025-11-03 10:30:00'),
(8, 20, 10, '2025-12-13 11:15:00'),
(9, 16, 9, '2025-09-18 12:00:00'),
(10, 16, 8, '2025-10-07 13:45:00');

select image from pet where id = 11;
