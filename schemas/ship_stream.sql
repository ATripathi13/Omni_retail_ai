BEGIN TRANSACTION;
CREATE TABLE shipments (
	id INTEGER NOT NULL, 
	order_id INTEGER, 
	carrier VARCHAR, 
	tracking_number VARCHAR, 
	status VARCHAR, 
	estimated_delivery DATETIME, 
	PRIMARY KEY (id), 
	UNIQUE (tracking_number)
);
INSERT INTO "shipments" VALUES(1,1,'USPS','9731ef8d-b541-43a8-b1ab-ba8825cb9d43','in_transit','2026-01-21 08:10:56.224782');
INSERT INTO "shipments" VALUES(2,2,'UPS','d46b3c60-7394-4ab5-a1b6-f8b2e86771b2','delivered','2026-01-21 08:10:57.132852');
INSERT INTO "shipments" VALUES(3,3,'FedEx','569815a0-5227-4161-892a-6128f91d3e3b','delivered','2026-01-22 08:10:57.873426');
INSERT INTO "shipments" VALUES(4,5,'UPS','42c2f95d-7db3-45fd-a01e-369cfc660ae1','delivered','2026-01-22 08:11:00.738142');
INSERT INTO "shipments" VALUES(5,6,'USPS','e80dda57-cb7a-4b81-b264-1e75a767942a','in_transit','2026-01-18 08:11:10.490674');
INSERT INTO "shipments" VALUES(6,9,'FedEx','0081a360-d1d6-47b0-ba87-582d463f1bc8','delivered','2026-01-21 08:11:18.779685');
INSERT INTO "shipments" VALUES(7,14,'USPS','c92c5604-5e52-4bd8-ad23-e9b164c5ae2c','delivered','2026-01-21 08:11:32.482496');
INSERT INTO "shipments" VALUES(8,18,'USPS','f9586489-4717-490c-8256-09bdc6cf84a4','delivered','2026-01-20 08:11:38.558145');
INSERT INTO "shipments" VALUES(9,20,'USPS','dbe62845-8016-4cb7-8d9c-9023f58d21ca','in_transit','2026-01-22 08:11:42.300643');
CREATE TABLE tracking_updates (
	id INTEGER NOT NULL, 
	shipment_id INTEGER, 
	location VARCHAR, 
	status VARCHAR, 
	timestamp DATETIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(shipment_id) REFERENCES shipments (id)
);
INSERT INTO "tracking_updates" VALUES(1,1,'Mariafurt','In transit','2026-01-17 08:10:56.335577');
INSERT INTO "tracking_updates" VALUES(2,1,'Donaldmouth','Arrived at facility','2026-01-17 04:10:56.336576');
INSERT INTO "tracking_updates" VALUES(3,1,'Josephtown','Arrived at facility','2026-01-17 00:10:56.336576');
INSERT INTO "tracking_updates" VALUES(4,2,'East Abigailmouth','Arrived at facility','2026-01-17 08:10:57.266784');
INSERT INTO "tracking_updates" VALUES(5,3,'Baileyview','Arrived at facility','2026-01-17 08:10:58.077269');
INSERT INTO "tracking_updates" VALUES(6,4,'Morganmouth','Arrived at facility','2026-01-17 08:11:02.393187');
INSERT INTO "tracking_updates" VALUES(7,5,'East Sean','Arrived at facility','2026-01-17 08:11:11.175391');
INSERT INTO "tracking_updates" VALUES(8,5,'North Marvin','In transit','2026-01-17 04:11:11.176390');
INSERT INTO "tracking_updates" VALUES(9,6,'North Cherylfurt','Arrived at facility','2026-01-17 08:11:19.378720');
INSERT INTO "tracking_updates" VALUES(10,6,'Lake Elijahberg','Picked up','2026-01-17 04:11:19.379734');
INSERT INTO "tracking_updates" VALUES(11,6,'Willisburgh','In transit','2026-01-17 00:11:19.379734');
INSERT INTO "tracking_updates" VALUES(12,7,'South Reneefurt','Picked up','2026-01-17 08:11:32.891893');
INSERT INTO "tracking_updates" VALUES(13,7,'West Phillip','Arrived at facility','2026-01-17 04:11:32.892889');
INSERT INTO "tracking_updates" VALUES(14,8,'North Brandon','Picked up','2026-01-17 08:11:38.792275');
INSERT INTO "tracking_updates" VALUES(15,8,'Susanmouth','Picked up','2026-01-17 04:11:38.795265');
INSERT INTO "tracking_updates" VALUES(16,8,'Zavalabury','Picked up','2026-01-17 00:11:38.797262');
INSERT INTO "tracking_updates" VALUES(17,9,'North Graceland','Arrived at facility','2026-01-17 08:11:42.510221');
INSERT INTO "tracking_updates" VALUES(18,9,'South Samuel','In transit','2026-01-17 04:11:42.510733');
CREATE INDEX ix_shipments_id ON shipments (id);
CREATE UNIQUE INDEX ix_shipments_order_id ON shipments (order_id);
CREATE INDEX ix_tracking_updates_id ON tracking_updates (id);
COMMIT;
