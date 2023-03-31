PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "sellers" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "seller_name" varchar(255) NULL);
INSERT INTO sellers VALUES(1,'Company A');
INSERT INTO sellers VALUES(2,'Company B');
COMMIT;
