-- SQLite
SELECT id, username, email, name, password
FROM user;

delete from user
where 1=1;
VACUUM;

INSERT INTO user (username, email, name, password)
VALUES ("jeremy12", "correo@jeremy.com", "Jeremy", "xd123");