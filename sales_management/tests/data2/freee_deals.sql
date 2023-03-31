PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "freee_deals" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "type" varchar(255) NULL, "number" bigint NULL, "title" varchar(255) NULL, "date" datetime NULL, "slip_number" integer NULL, "debit_account" varchar(255) NULL, "debit_sub_account" varchar(255) NULL, "debit_partner" varchar(255) NULL, "debit_department" varchar(255) NULL, "debit_item" varchar(255) NULL, "debit_memo_tag" varchar(255) NULL, "debit_tax_category" varchar(255) NULL, "debit_amount" decimal NULL, "debit_tax_amount" decimal NULL, "credit_account" varchar(255) NULL, "credit_sub_account" varchar(255) NULL, "credit_partner" varchar(255) NULL, "credit_department" varchar(255) NULL, "credit_item" varchar(255) NULL, "credit_memo_tag" varchar(255) NULL, "credit_tax_category" varchar(255) NULL, "credit_amount" decimal NULL, "credit_tax_amount" decimal NULL, "summary" varchar(255) NULL);
INSERT INTO freee_deals VALUES(11,'会計',43891,'[明細行]','2022-07-06 15:00:00',2,'e5087fe727d1f929d570c911bcc6e581e2170919','','da39a3ee5e6b4b0d3255bfef95601890afd80709','','','','対象外',270307,0,'売掛金','','82810cb97184cf542141f811b63d90bc5de31d1b','','','','対象外',279589,0,'39fae878f3e4bfec74a147a960714494e6340aa8');
INSERT INTO freee_deals VALUES(12,'会計',43892,'[明細行]','2022-07-06 15:00:00',2,'f6222363ffa69bd042c846504f07507a4f0f8fb4','','82810cb97184cf542141f811b63d90bc5de31d1b','','','','課税売返10%',9282,844,'支払手数料','','82810cb97184cf542141f811b63d90bc5de31d1b','','','','課税売返10%',3730,339,'da39a3ee5e6b4b0d3255bfef95601890afd80709');
INSERT INTO freee_deals VALUES(13,'会計',43893,'[明細行]','2022-07-06 15:00:00',2,'da568edb40d1dc5c0f3790cfbef2a161268e34a8','','21bd4f75f7f72babd6d220f4ffec12f90f7303bc','','支払手数料(Square)','','対象外',3730,0,'','','da39a3ee5e6b4b0d3255bfef95601890afd80709','','','','',0,0,'da39a3ee5e6b4b0d3255bfef95601890afd80709');
INSERT INTO freee_deals VALUES(14,'会計',43894,'[明細行]','2022-07-06 15:00:00',3,'e5087fe727d1f929d570c911bcc6e581e2170919','','da39a3ee5e6b4b0d3255bfef95601890afd80709','','','','対象外',125802,0,'売掛金','','82810cb97184cf542141f811b63d90bc5de31d1b','','','','対象外',130073,0,'64074768fb89121ea3ac395a135f11549123e497');
INSERT INTO freee_deals VALUES(15,'会計',43895,'[明細行]','2022-07-06 15:00:00',3,'f6222363ffa69bd042c846504f07507a4f0f8fb4','','82810cb97184cf542141f811b63d90bc5de31d1b','','','','課税売返10%',4271,388,'支払手数料','','82810cb97184cf542141f811b63d90bc5de31d1b','','','','課税売返10%',1010,92,'da39a3ee5e6b4b0d3255bfef95601890afd80709');
INSERT INTO freee_deals VALUES(16,'会計',43896,'[明細行]','2022-07-06 15:00:00',3,'da568edb40d1dc5c0f3790cfbef2a161268e34a8','','21bd4f75f7f72babd6d220f4ffec12f90f7303bc','','支払手数料(Square)','','対象外',1010,0,'','','da39a3ee5e6b4b0d3255bfef95601890afd80709','','','','',0,0,'da39a3ee5e6b4b0d3255bfef95601890afd80709');
INSERT INTO freee_deals VALUES(17,'会計',43897,'[明細行]','2022-07-06 15:00:00',4,'e5087fe727d1f929d570c911bcc6e581e2170919','','da39a3ee5e6b4b0d3255bfef95601890afd80709','','','','対象外',102244,0,'売掛金','','82810cb97184cf542141f811b63d90bc5de31d1b','','','','対象外',105679,0,'8ff2af29074ae860060fa0512f054d47b2218e16');
INSERT INTO freee_deals VALUES(18,'会計',43898,'[明細行]','2022-07-06 15:00:00',4,'f6222363ffa69bd042c846504f07507a4f0f8fb4','','82810cb97184cf542141f811b63d90bc5de31d1b','','','','課税売返10%',3435,312,'支払手数料','','82810cb97184cf542141f811b63d90bc5de31d1b','','','','課税売返10%',300,27,'da39a3ee5e6b4b0d3255bfef95601890afd80709');
INSERT INTO freee_deals VALUES(19,'会計',43899,'[明細行]','2022-07-06 15:00:00',4,'da568edb40d1dc5c0f3790cfbef2a161268e34a8','','21bd4f75f7f72babd6d220f4ffec12f90f7303bc','','支払手数料(Square)','','対象外',300,0,'','','da39a3ee5e6b4b0d3255bfef95601890afd80709','','','','',0,0,'da39a3ee5e6b4b0d3255bfef95601890afd80709');
INSERT INTO freee_deals VALUES(20,'会計',43900,'[明細行]','2022-07-06 15:00:00',5,'e5087fe727d1f929d570c911bcc6e581e2170919','','da39a3ee5e6b4b0d3255bfef95601890afd80709','','','','対象外',182527,0,'売掛金','','82810cb97184cf542141f811b63d90bc5de31d1b','','','','対象外',189059,0,'362a4e03c87bf81b0b124dd3a5aa772b0878afde');
INSERT INTO freee_deals VALUES(21,'会計',43901,'[明細行]','2022-07-06 15:00:00',5,'f6222363ffa69bd042c846504f07507a4f0f8fb4','','82810cb97184cf542141f811b63d90bc5de31d1b','','','','課税売返10%',6532,594,'支払手数料','','82810cb97184cf542141f811b63d90bc5de31d1b','','','','課税売返10%',1992,181,'da39a3ee5e6b4b0d3255bfef95601890afd80709');
INSERT INTO freee_deals VALUES(22,'会計',43902,'[明細行]','2022-07-06 15:00:00',5,'da568edb40d1dc5c0f3790cfbef2a161268e34a8','','21bd4f75f7f72babd6d220f4ffec12f90f7303bc','','支払手数料(Square)','','対象外',1992,0,'','','da39a3ee5e6b4b0d3255bfef95601890afd80709','','','','',0,0,'da39a3ee5e6b4b0d3255bfef95601890afd80709');
INSERT INTO freee_deals VALUES(23,'会計',43903,'[明細行]','2022-07-06 15:00:00',6,'e5087fe727d1f929d570c911bcc6e581e2170919','','da39a3ee5e6b4b0d3255bfef95601890afd80709','','','','対象外',109074,0,'売掛金','','82810cb97184cf542141f811b63d90bc5de31d1b','','','','対象外',112739,0,'277bb3aa3d9e40047d33985b2cd884de2acd9e9c');
INSERT INTO freee_deals VALUES(24,'会計',43904,'[明細行]','2022-07-06 15:00:00',6,'f6222363ffa69bd042c846504f07507a4f0f8fb4','','82810cb97184cf542141f811b63d90bc5de31d1b','','','','課税売返10%',3665,333,'支払手数料','','82810cb97184cf542141f811b63d90bc5de31d1b','','','','課税売返10%',449,41,'da39a3ee5e6b4b0d3255bfef95601890afd80709');
INSERT INTO freee_deals VALUES(25,'会計',43905,'[明細行]','2022-07-06 15:00:00',6,'da568edb40d1dc5c0f3790cfbef2a161268e34a8','','21bd4f75f7f72babd6d220f4ffec12f90f7303bc','','支払手数料(Square)','','対象外',449,0,'','','da39a3ee5e6b4b0d3255bfef95601890afd80709','','','','',0,0,'da39a3ee5e6b4b0d3255bfef95601890afd80709');
COMMIT;
