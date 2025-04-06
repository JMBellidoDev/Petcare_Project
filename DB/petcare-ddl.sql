

/* Seguridad de la aplicación */
create table app_user (
	id BIGSERIAL primary key,
	username varchar(20) unique,
	hashed_password varchar(60),
	email varchar(80),
	enabled boolean,
	role varchar(10) check(role in ('client', 'vet', 'vet_entity'))
);


/* Entidades hijas de seguridad (foreign keys) */
create table vet_entity (
	id bigint primary key,
	name varchar(100),
	cif varchar(9) unique,
	address varchar(255),
	phone_number varchar(9),
	constraint fk_vet_entity_app_user foreign key (id) references app_user(id)
);


create table vet (
	id bigint primary key,
	national_id_document varchar(9) unique,
	name varchar(100),
	registration_number varchar(20) unique,
	vet_entity_id bigint,
	constraint fk_vet_entity foreign key (vet_entity_id) references vet_entity (id),
	constraint fk_vet_app_user foreign key (id) references app_user(id)
);


create table client (
	id bigint primary key,
	national_id_document varchar(9) unique,
	name varchar(100),
	birthdate date,
	address varchar(255),
	phone_number varchar(9),
	constraint fk_pet_app_user foreign key (id) references app_user(id)
);


/** Entidades mascota y su relación con clientes y veterinarios */
create table pet (
	id BIGSERIAL primary key,
	chip_number varchar(15),
	type varchar(20) check (type in ('dog', 'cat', 'horse', 'ferret', 'bird', 'rabbit')),
	breed varchar(50),
	name varchar(30),
	birthdate date,
	alive boolean default true,
	castrated boolean,
    image bytea
);


create table client_pets (
	id BIGSERIAL primary key,
	pet_id bigint,
	client_id bigint,
	show boolean default true,
	unique (pet_id, client_id),
	constraint client_pets_pet_id foreign key (pet_id) references pet(id),
	constraint client_pets_client_id foreign key (client_id) references client(id)
);

create table report (
	id BIGSERIAL primary key,
	pet_id bigint,
	vet_id bigint,
	reason text,
	diagnosis text,
	treatment text,
	report_date timestamp,
	constraint fk_report_pet_id foreign key (pet_id) references pet(id),
	constraint fk_report_vet_id foreign key (vet_id) references vet(id)
);


create table appointment ( 
	id BIGSERIAL primary key,
	pet_id bigint, 
	vet_id bigint,
	client_id bigint,
	appointment_date timestamp,
	constraint fk_appointment_pet_id foreign key (pet_id) references pet(id),
	constraint fk_appointment_vet_id foreign key (vet_id) references vet(id),
	constraint fk_appointment_client_id foreign key (client_id) references client(id)
);
