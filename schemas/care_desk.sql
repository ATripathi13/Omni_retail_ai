BEGIN TRANSACTION;
CREATE TABLE interactions (
	id INTEGER NOT NULL, 
	ticket_id INTEGER, 
	sender VARCHAR, 
	message TEXT, 
	timestamp DATETIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(ticket_id) REFERENCES tickets (id)
);
INSERT INTO "interactions" VALUES(1,1,'customer','Deep board to fear.
From bring drug hard wide cell will. Speak ground tend pay soon building east. Subject city claim simply tonight mention.
Onto occur as sport than. Entire member behind.','2026-01-17 08:11:07.714979');
INSERT INTO "interactions" VALUES(2,2,'customer','Organization start summer. Culture feeling professional huge to officer hear.
View feel coach system minute you. Us less dark real even clearly. Leave analysis of civil guess world.','2026-01-17 08:11:39.842223');
CREATE TABLE tickets (
	id INTEGER NOT NULL, 
	customer_id INTEGER, 
	order_id INTEGER, 
	subject VARCHAR, 
	status VARCHAR, 
	priority VARCHAR, 
	created_at DATETIME, 
	PRIMARY KEY (id)
);
INSERT INTO "tickets" VALUES(1,3,5,'Prove today open strong deal while agency.','open','high','2026-01-17 08:11:06.067625');
INSERT INTO "tickets" VALUES(2,9,18,'Beyond society animal exactly hear.','open','low','2026-01-17 08:11:39.520959');
CREATE INDEX ix_tickets_id ON tickets (id);
CREATE INDEX ix_tickets_customer_id ON tickets (customer_id);
CREATE INDEX ix_interactions_id ON interactions (id);
COMMIT;
