PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "omron_transactions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "handling_date" datetime NULL, "credit_company_code" varchar(255) NULL, "credit_company_name" varchar(255) NULL, "payment_category" varchar(255) NULL, "payment_name" varchar(255) NULL, "installment_count_gift_value" integer NULL, "gift_ticket_quantity" integer NULL, "slip_number" varchar(255) NULL, "sales_amount" decimal NULL, "scheduled_payment_date1" datetime NULL, "scheduled_payment_date2" datetime NULL);
INSERT INTO omron_transactions VALUES(1,'2022-07-01 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'427',20000,'2022-09-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(2,'2022-07-01 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'427',-6000,'2022-09-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(3,'2022-07-02 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'401',5000,'2022-09-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(4,'2022-07-02 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'403',10000,'2022-09-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(5,'2022-07-02 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'401',-850,'2022-09-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(6,'2022-07-02 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'403',-3000,'2022-09-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(7,'2022-07-05 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'194',10000,'2022-09-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(8,'2022-07-05 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'194',-3000,'2022-09-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(9,'2022-07-09 15:00:00','f890d752d330caf426a52643f6510d6efd597f3e','ﾎﾟｲﾝﾄ利用','10','一括',1,0,'760',5316,'2022-09-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(10,'2022-07-11 15:00:00','f890d752d330caf426a52643f6510d6efd597f3e','ﾎﾟｲﾝﾄ利用','10','一括',1,0,'472',3000,'2022-09-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(11,'2022-07-17 15:00:00','9d00089c4194a6c21c2d95f432a2777dac29d24e','特定会員ｸｰﾎﾟﾝ','10','一括',1,0,'347',5000,'2022-09-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(12,'2022-07-18 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'211',30000,'2022-09-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(13,'2022-07-18 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'211',-9000,'2022-09-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(14,'2022-07-19 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'243',20000,'2022-09-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(15,'2022-07-19 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'243',-6000,'2022-09-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(16,'2022-07-22 15:00:00','f890d752d330caf426a52643f6510d6efd597f3e','ﾎﾟｲﾝﾄ利用','10','一括',1,0,'623',2000,'2022-09-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(17,'2022-07-23 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'379',10000,'2022-09-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(18,'2022-07-23 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'381',10000,'2022-09-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(19,'2022-07-23 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'379',-3000,'2022-09-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(20,'2022-07-23 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'381',-3000,'2022-09-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(21,'2022-07-25 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'180',20000,'2022-09-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(22,'2022-07-25 15:00:00','f890d752d330caf426a52643f6510d6efd597f3e','ﾎﾟｲﾝﾄ利用','10','一括',1,0,'502',1821,'2022-09-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(23,'2022-07-25 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'180',-6000,'2022-09-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(24,'2022-07-26 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'208',10000,'2022-09-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(25,'2022-07-26 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'208',-3000,'2022-09-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(26,'2022-08-03 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'183',10000,'2022-10-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(27,'2022-08-03 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'184',20000,'2022-10-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(28,'2022-08-03 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'183',-3000,'2022-10-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(29,'2022-08-03 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'184',-6000,'2022-10-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(30,'2022-08-04 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'257',10000,'2022-10-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(31,'2022-08-04 15:00:00','f890d752d330caf426a52643f6510d6efd597f3e','ﾎﾟｲﾝﾄ利用','10','一括',1,0,'459',1160,'2022-10-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(32,'2022-08-04 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'257',-3000,'2022-10-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(33,'2022-08-07 15:00:00','f890d752d330caf426a52643f6510d6efd597f3e','ﾎﾟｲﾝﾄ利用','10','一括',1,0,'256',2030,'2022-10-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(34,'2022-08-10 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'335',5000,'2022-10-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(35,'2022-08-10 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'335',-850,'2022-10-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(36,'2022-08-17 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'221',10000,'2022-10-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(37,'2022-08-17 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'222',10000,'2022-10-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(38,'2022-08-17 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'221',-3000,'2022-10-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(39,'2022-08-17 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'222',-3000,'2022-10-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(40,'2022-08-19 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'358',10000,'2022-10-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(41,'2022-08-19 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'359',10000,'2022-10-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(42,'2022-08-19 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'361',10000,'2022-10-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(43,'2022-08-19 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'363',10000,'2022-10-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(44,'2022-08-19 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'358',-3000,'2022-10-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(45,'2022-08-19 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'359',-3000,'2022-10-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(46,'2022-08-19 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'361',-3000,'2022-10-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(47,'2022-08-19 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'363',-3000,'2022-10-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(48,'2022-08-21 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'79',10000,'2022-10-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(49,'2022-08-21 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'79',-3000,'2022-10-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(50,'2022-08-26 15:00:00','549843ddfef8fcf36afa56c6286f2689537c8b2c','入会特典ｸｰﾎﾟﾝ','10','一括',1,0,'1',500,'2022-10-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(51,'2022-08-30 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'214',10000,'2022-10-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(52,'2022-08-30 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'214',-3000,'2022-10-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(53,'2022-09-06 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'45',10000,'2022-11-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(54,'2022-09-06 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'46',10000,'2022-11-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(55,'2022-09-06 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'45',-3000,'2022-11-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(56,'2022-09-06 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'46',-3000,'2022-11-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(57,'2022-09-07 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'45',10000,'2022-11-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(58,'2022-09-07 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'45',-3000,'2022-11-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(59,'2022-09-09 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'43',10000,'2022-11-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(60,'2022-09-09 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'43',-3000,'2022-11-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(61,'2022-09-10 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'33',10000,'2022-11-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(62,'2022-09-10 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'33',-3000,'2022-11-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(63,'2022-09-22 15:00:00','f47aea8bdcbd1179a1f3d91e6afeeb259488f2d1','お買物券','B0','ｷﾞﾌﾄ券',1000,19,'0',19000,'2022-11-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(64,'2022-09-24 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'38',5000,'2022-11-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(65,'2022-09-24 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'38',-850,'2022-11-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(66,'2022-09-26 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'36',10000,'2022-11-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(67,'2022-09-26 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'36',-3000,'2022-11-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(68,'2022-09-27 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'31',20000,'2022-11-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(69,'2022-09-27 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'31',-6000,'2022-11-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(70,'2022-09-30 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'47',20000,'2022-12-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(71,'2022-09-30 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'51',10000,'2022-12-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(72,'2022-09-30 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'47',-6000,'2022-12-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(73,'2022-09-30 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'51',-3000,'2022-12-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(74,'2022-10-05 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'34',10000,'2022-12-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(75,'2022-10-05 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'35',10000,'2022-12-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(76,'2022-10-05 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'34',-3000,'2022-12-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(77,'2022-10-05 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'35',-3000,'2022-12-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(78,'2022-10-07 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'90',20000,'2022-12-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(79,'2022-10-07 15:00:00','f890d752d330caf426a52643f6510d6efd597f3e','ﾎﾟｲﾝﾄ利用','10','一括',1,0,'323',688,'2022-12-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(80,'2022-10-07 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'90',-6000,'2022-12-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(81,'2022-10-12 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'20',10000,'2022-12-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(82,'2022-10-12 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'21',10000,'2022-12-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(83,'2022-10-12 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'20',-1700,'2022-12-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(84,'2022-10-12 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'21',-3000,'2022-12-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(85,'2022-10-13 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'32',10000,'2022-12-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(86,'2022-10-13 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'32',-1700,'2022-12-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(87,'2022-10-15 15:00:00','9d00089c4194a6c21c2d95f432a2777dac29d24e','特定会員ｸｰﾎﾟﾝ','10','一括',1,0,'17',2000,'2022-12-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(88,'2022-10-15 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'30',10000,'2022-12-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(89,'2022-10-15 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'32',10000,'2022-12-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(90,'2022-10-15 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'30',-3000,'2022-12-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(91,'2022-10-15 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'32',-3000,'2022-12-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(92,'2022-10-20 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'28',10000,'2022-12-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(93,'2022-10-20 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'28',-3000,'2022-12-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(94,'2022-10-24 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'26',20000,'2022-12-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(95,'2022-10-24 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'26',-6000,'2022-12-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(96,'2022-10-25 15:00:00','f890d752d330caf426a52643f6510d6efd597f3e','ﾎﾟｲﾝﾄ利用','10','一括',1,0,'56',9350,'2022-12-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(97,'2022-10-26 15:00:00','f47aea8bdcbd1179a1f3d91e6afeeb259488f2d1','お買物券','B0','ｷﾞﾌﾄ券',1000,8,'0',8000,'2022-12-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(98,'2022-10-27 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'13',10000,'2022-12-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(99,'2022-10-27 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'13',-3000,'2022-12-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(100,'2022-10-29 15:00:00','9d00089c4194a6c21c2d95f432a2777dac29d24e','特定会員ｸｰﾎﾟﾝ','10','一括',1,0,'17',2000,'2022-12-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(101,'2022-11-06 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'22',30000,'2023-01-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(102,'2022-11-06 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'22',-9000,'2023-01-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(103,'2022-11-09 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'14',10000,'2023-01-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(104,'2022-11-09 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'14',-3000,'2023-01-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(105,'2022-11-11 15:00:00','9d00089c4194a6c21c2d95f432a2777dac29d24e','特定会員ｸｰﾎﾟﾝ','10','一括',1,0,'13',2000,'2023-01-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(106,'2022-11-11 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'22',20000,'2023-01-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(107,'2022-11-11 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'22',-6000,'2023-01-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(108,'2022-11-12 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'26',10000,'2023-01-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(109,'2022-11-12 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'30',10000,'2023-01-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(110,'2022-11-12 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'33',10000,'2023-01-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(111,'2022-11-12 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'26',-3000,'2023-01-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(112,'2022-11-12 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'30',-3000,'2023-01-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(113,'2022-11-12 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'33',-3000,'2023-01-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(114,'2022-11-15 15:00:00','f890d752d330caf426a52643f6510d6efd597f3e','ﾎﾟｲﾝﾄ利用','10','一括',1,0,'249',1524,'2023-01-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(115,'2022-11-16 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'19',10000,'2023-01-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(116,'2022-11-16 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'20',10000,'2023-01-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(117,'2022-11-16 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'21',20000,'2023-01-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(118,'2022-11-16 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'19',-3000,'2023-01-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(119,'2022-11-16 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'20',-3000,'2023-01-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(120,'2022-11-16 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'21',-6000,'2023-01-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(121,'2022-11-18 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'24',10000,'2023-01-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(122,'2022-11-18 15:00:00','f890d752d330caf426a52643f6510d6efd597f3e','ﾎﾟｲﾝﾄ利用','10','一括',1,0,'302',792,'2023-01-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(123,'2022-11-18 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'24',-3000,'2023-01-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(124,'2022-11-21 15:00:00','f890d752d330caf426a52643f6510d6efd597f3e','ﾎﾟｲﾝﾄ利用','10','一括',1,0,'347',1296,'2023-01-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(125,'2022-11-25 15:00:00','f890d752d330caf426a52643f6510d6efd597f3e','ﾎﾟｲﾝﾄ利用','10','一括',1,0,'250',4480,'2023-01-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(126,'2022-11-26 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'25',5000,'2023-01-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(127,'2022-11-26 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'38',10000,'2023-01-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(128,'2022-11-26 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'25',-850,'2023-01-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(129,'2022-11-26 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'38',-3000,'2023-01-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(130,'2022-11-28 15:00:00','f890d752d330caf426a52643f6510d6efd597f3e','ﾎﾟｲﾝﾄ利用','10','一括',1,0,'366',810,'2023-01-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(131,'2022-11-29 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'24',10000,'2023-01-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(132,'2022-11-29 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'24',-3000,'2023-01-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(133,'2022-11-30 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'18',10000,'2023-02-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(134,'2022-11-30 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'19',10000,'2023-02-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(135,'2022-11-30 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'20',10000,'2023-02-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(136,'2022-11-30 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'18',-3000,'2023-02-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(137,'2022-11-30 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'19',-3000,'2023-02-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(138,'2022-11-30 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'20',-3000,'2023-02-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(139,'2022-12-01 15:00:00','f47aea8bdcbd1179a1f3d91e6afeeb259488f2d1','お買物券','B0','ｷﾞﾌﾄ券',1000,1,'0',1000,'2023-02-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(140,'2022-12-02 15:00:00','f47aea8bdcbd1179a1f3d91e6afeeb259488f2d1','お買物券','B0','ｷﾞﾌﾄ券',1000,20,'0',20000,'2023-02-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(141,'2022-12-02 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'30',10000,'2023-02-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(142,'2022-12-02 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'30',-3000,'2023-02-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(143,'2022-12-03 15:00:00','f890d752d330caf426a52643f6510d6efd597f3e','ﾎﾟｲﾝﾄ利用','10','一括',1,0,'291',3400,'2023-02-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(144,'2022-12-06 15:00:00','9d00089c4194a6c21c2d95f432a2777dac29d24e','特定会員ｸｰﾎﾟﾝ','10','一括',1,0,'31',2000,'2023-02-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(145,'2022-12-06 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'55',10000,'2023-02-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(146,'2022-12-06 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'55',-3000,'2023-02-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(147,'2022-12-08 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'218',10000,'2023-02-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(148,'2022-12-08 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'218',-3000,'2023-02-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(149,'2022-12-09 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'329',10000,'2023-02-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(150,'2022-12-09 15:00:00','f890d752d330caf426a52643f6510d6efd597f3e','ﾎﾟｲﾝﾄ利用','10','一括',1,0,'491',6600,'2023-02-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(151,'2022-12-09 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'329',-1700,'2023-02-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(152,'2022-12-11 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'43',10000,'2023-02-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(153,'2022-12-11 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'44',10000,'2023-02-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(154,'2022-12-11 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'43',-3000,'2023-02-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(155,'2022-12-11 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'44',-3000,'2023-02-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(156,'2022-12-16 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'68',20000,'2023-02-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(157,'2022-12-16 15:00:00','f890d752d330caf426a52643f6510d6efd597f3e','ﾎﾟｲﾝﾄ利用','10','一括',1,0,'219',300,'2023-02-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(158,'2022-12-16 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'68',-6000,'2023-02-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(159,'2022-12-23 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'65',10000,'2023-02-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(160,'2022-12-23 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'65',-3000,'2023-02-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(161,'2022-12-24 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'49',10000,'2023-02-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(162,'2022-12-24 15:00:00','f890d752d330caf426a52643f6510d6efd597f3e','ﾎﾟｲﾝﾄ利用','10','一括',1,0,'251',5400,'2023-02-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(163,'2022-12-24 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'49',-3000,'2023-02-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(164,'2022-12-27 15:00:00','f47aea8bdcbd1179a1f3d91e6afeeb259488f2d1','お買物券','B0','ｷﾞﾌﾄ券',1000,9,'0',9000,'2023-02-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(165,'2022-12-27 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'25',20000,'2023-02-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(166,'2022-12-27 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'25',-6000,'2023-02-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(167,'2022-12-28 15:00:00','9d00089c4194a6c21c2d95f432a2777dac29d24e','特定会員ｸｰﾎﾟﾝ','10','一括',1,0,'16',2000,'2023-02-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(168,'2022-12-28 15:00:00','f890d752d330caf426a52643f6510d6efd597f3e','ﾎﾟｲﾝﾄ利用','10','一括',1,0,'185',2400,'2023-02-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(169,'2022-12-29 15:00:00','f890d752d330caf426a52643f6510d6efd597f3e','ﾎﾟｲﾝﾄ利用','10','一括',1,0,'100',1766,'2023-02-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(170,'2022-12-30 15:00:00','43a784ccb1556e9769a993465bbe5bfe24b397d4','ﾎﾟｲﾝﾄｸｰﾎﾟﾝ','10','一括',1,0,'25',10000,'2023-02-19 15:00:00',NULL);
INSERT INTO omron_transactions VALUES(171,'2022-12-30 15:00:00','264bb3273d03cef72b6fbd7618bce7349989fa94','店舗負担額','10','一括',1,0,'25',-3000,'2023-02-19 15:00:00',NULL);
COMMIT;
