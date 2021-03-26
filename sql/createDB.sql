-- Generiert von Oracle SQL Developer Data Modeler 18.2.0.179.0806
--   am/um:        2021-01-12 11:27:38 MEZ
--   Site:      Oracle Database 11g
--   Typ:      Oracle Database 11g



CREATE TABLE besitzer (
    id            NUMBER(4) NOT NULL,
    password      VARCHAR2(32),
    picturepath   VARCHAR2(64),
    phonenumber   NUMBER(15) NOT NULL,
    person_id     NUMBER(8) NOT NULL
);

CREATE UNIQUE INDEX besitzer__idx ON
    besitzer (
        person_id
    ASC );

ALTER TABLE besitzer ADD CONSTRAINT besitzer_pk PRIMARY KEY ( id );

CREATE TABLE betreter (
    id            NUMBER(4) NOT NULL,
    besitzer_id   NUMBER(4),
    person_id     NUMBER(8) NOT NULL,
    nachname      VARCHAR2(32)
);

CREATE UNIQUE INDEX betreter__idx ON
    betreter (
        person_id
    ASC );

ALTER TABLE betreter ADD CONSTRAINT betreter_pk PRIMARY KEY ( id );

CREATE TABLE entrancehistory (
    id          NUMBER(4) NOT NULL,
    "date"      DATE,
    person_id   NUMBER(8) NOT NULL
);

ALTER TABLE entrancehistory ADD CONSTRAINT entrancehistory_pk PRIMARY KEY ( id );

CREATE TABLE face (
    id          NUMBER(4) NOT NULL,
    path        VARCHAR2(64),
    person_id   NUMBER(8) NOT NULL
);

CREATE UNIQUE INDEX face__idx ON
    face (
        person_id
    ASC );

ALTER TABLE face ADD CONSTRAINT face_pk PRIMARY KEY ( id );

CREATE TABLE fingerprint (
    id          NUMBER(5) NOT NULL,
    path        VARCHAR2(64),
    person_id   NUMBER(8) NOT NULL
);

ALTER TABLE fingerprint ADD CONSTRAINT fingerprint_pk PRIMARY KEY ( id );

CREATE TABLE person (
    id            NUMBER(8) NOT NULL,
    vorname       VARCHAR2(32),
    email         VARCHAR2(64),
    besitzer_id   NUMBER(4) NOT NULL,
    betreter_id   NUMBER(4) NOT NULL,
    face_id       NUMBER(4) NOT NULL
);

CREATE UNIQUE INDEX person__idx ON
    person (
        besitzer_id
    ASC );

CREATE UNIQUE INDEX person__idxv1 ON
    person (
        betreter_id
    ASC );

CREATE UNIQUE INDEX person__idxv2 ON
    person (
        face_id
    ASC );

ALTER TABLE person ADD CONSTRAINT person_pk PRIMARY KEY ( id );

ALTER TABLE besitzer
    ADD CONSTRAINT besitzer_person_fk FOREIGN KEY ( person_id )
        REFERENCES person ( id );

ALTER TABLE betreter
    ADD CONSTRAINT betreter_besitzer_fk FOREIGN KEY ( besitzer_id )
        REFERENCES besitzer ( id );

ALTER TABLE betreter
    ADD CONSTRAINT betreter_person_fk FOREIGN KEY ( person_id )
        REFERENCES person ( id );

ALTER TABLE entrancehistory
    ADD CONSTRAINT entrancehistory_person_fk FOREIGN KEY ( person_id )
        REFERENCES person ( id );

ALTER TABLE face
    ADD CONSTRAINT face_person_fk FOREIGN KEY ( person_id )
        REFERENCES person ( id );

ALTER TABLE fingerprint
    ADD CONSTRAINT fingerprint_person_fk FOREIGN KEY ( person_id )
        REFERENCES person ( id );

ALTER TABLE person
    ADD CONSTRAINT person_besitzer_fk FOREIGN KEY ( besitzer_id )
        REFERENCES besitzer ( id );

ALTER TABLE person
    ADD CONSTRAINT person_betreter_fk FOREIGN KEY ( betreter_id )
        REFERENCES betreter ( id );

ALTER TABLE person
    ADD CONSTRAINT person_face_fk FOREIGN KEY ( face_id )
        REFERENCES face ( id );



-- Zusammenfassungsbericht für Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                             6
-- CREATE INDEX                             6
-- ALTER TABLE                             15
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
