DROP TABLE IF EXISTS app_user;

CREATE TABLE app_user (
    id int,
    name text
);

INSERT INTO app_user (id, name)
    VALUES (1, 'David'), (2, 'Rose');
