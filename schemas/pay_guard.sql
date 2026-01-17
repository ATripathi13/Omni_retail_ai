BEGIN TRANSACTION;
CREATE TABLE transactions (
	id INTEGER NOT NULL, 
	wallet_id INTEGER, 
	order_id INTEGER, 
	amount FLOAT, 
	type VARCHAR, 
	status VARCHAR, 
	created_at DATETIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(wallet_id) REFERENCES wallets (id)
);
INSERT INTO "transactions" VALUES(1,1,1,1.116449999999999819e+03,'debit','completed','2026-01-17 08:10:55.882892');
INSERT INTO "transactions" VALUES(2,1,2,48.98,'debit','completed','2026-01-17 08:10:56.798320');
INSERT INTO "transactions" VALUES(3,1,3,6.90599999999999909e+02,'debit','completed','2026-01-17 08:10:57.569659');
INSERT INTO "transactions" VALUES(4,2,4,2117.77,'debit','completed','2026-01-17 08:10:58.777218');
INSERT INTO "transactions" VALUES(5,3,5,162.58,'debit','completed','2026-01-17 08:11:00.235074');
INSERT INTO "transactions" VALUES(6,3,6,1856.62,'debit','completed','2026-01-17 08:11:09.097900');
INSERT INTO "transactions" VALUES(7,4,7,2.006959999999999809e+03,'debit','completed','2026-01-17 08:11:13.649041');
INSERT INTO "transactions" VALUES(8,4,8,631.44,'debit','completed','2026-01-17 08:11:15.546856');
INSERT INTO "transactions" VALUES(9,4,9,1492.32,'debit','completed','2026-01-17 08:11:17.327571');
INSERT INTO "transactions" VALUES(10,5,10,739.21,'debit','completed','2026-01-17 08:11:21.656162');
INSERT INTO "transactions" VALUES(11,5,11,9.47160000000000082e+02,'debit','completed','2026-01-17 08:11:24.233784');
INSERT INTO "transactions" VALUES(12,5,12,57.4,'debit','completed','2026-01-17 08:11:26.136969');
INSERT INTO "transactions" VALUES(13,6,13,1261.49,'debit','completed','2026-01-17 08:11:28.671921');
INSERT INTO "transactions" VALUES(14,7,14,995.14,'debit','completed','2026-01-17 08:11:31.447045');
INSERT INTO "transactions" VALUES(15,8,15,1483.95,'debit','completed','2026-01-17 08:11:34.121532');
INSERT INTO "transactions" VALUES(16,8,16,1725.55,'debit','completed','2026-01-17 08:11:35.514125');
INSERT INTO "transactions" VALUES(17,8,17,3.972000000000000455e+02,'debit','completed','2026-01-17 08:11:36.327988');
INSERT INTO "transactions" VALUES(18,9,18,276.99,'debit','completed','2026-01-17 08:11:37.935801');
INSERT INTO "transactions" VALUES(19,9,19,1384.62,'debit','completed','2026-01-17 08:11:40.521770');
INSERT INTO "transactions" VALUES(20,9,20,659.26,'debit','completed','2026-01-17 08:11:41.851249');
INSERT INTO "transactions" VALUES(21,10,21,130.87,'debit','completed','2026-01-17 08:11:43.409993');
CREATE TABLE wallets (
	id INTEGER NOT NULL, 
	customer_id INTEGER, 
	balance FLOAT, 
	currency VARCHAR, 
	PRIMARY KEY (id)
);
INSERT INTO "wallets" VALUES(1,1,2585.24,'USD');
INSERT INTO "wallets" VALUES(2,2,4680.24,'USD');
INSERT INTO "wallets" VALUES(3,3,4450.76,'USD');
INSERT INTO "wallets" VALUES(4,4,4332.0,'USD');
INSERT INTO "wallets" VALUES(5,5,4977.13,'USD');
INSERT INTO "wallets" VALUES(6,6,1591.49,'USD');
INSERT INTO "wallets" VALUES(7,7,1358.16,'USD');
INSERT INTO "wallets" VALUES(8,8,4358.9,'USD');
INSERT INTO "wallets" VALUES(9,9,681.63,'USD');
INSERT INTO "wallets" VALUES(10,10,2736.9,'USD');
CREATE UNIQUE INDEX ix_wallets_customer_id ON wallets (customer_id);
CREATE INDEX ix_wallets_id ON wallets (id);
CREATE INDEX ix_transactions_id ON transactions (id);
CREATE INDEX ix_transactions_order_id ON transactions (order_id);
COMMIT;
