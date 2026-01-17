BEGIN TRANSACTION;
CREATE TABLE customers (
	id INTEGER NOT NULL, 
	full_name VARCHAR, 
	email VARCHAR, 
	shipping_address TEXT, 
	PRIMARY KEY (id)
);
INSERT INTO "customers" VALUES(1,'Christina Fowler','ivance@example.org','PSC 7204, Box 8517
APO AE 87523');
INSERT INTO "customers" VALUES(2,'Christopher Vasquez','roberta29@example.org','668 Sandra Brook Suite 107
Cherylberg, WV 13682');
INSERT INTO "customers" VALUES(3,'Rita Foster','andrewwebb@example.org','7174 Maria Expressway Apt. 184
Hodgesstad, KY 26679');
INSERT INTO "customers" VALUES(4,'Jason Santana','bkramer@example.org','6250 Rose Mall
Jenniferport, TN 36155');
INSERT INTO "customers" VALUES(5,'Joshua Smith','zdominguez@example.com','746 Tucker Neck
Katelynchester, MS 83183');
INSERT INTO "customers" VALUES(6,'Michael Thompson','ronald23@example.org','07841 Steven Skyway Apt. 150
West Shannonville, IA 69091');
INSERT INTO "customers" VALUES(7,'Susan Burke','jamesbeard@example.org','8578 Parks Union Apt. 040
Gloriaborough, AK 60725');
INSERT INTO "customers" VALUES(8,'William Ruiz','tracey33@example.net','30078 Tyler Mills Suite 800
New Keith, MO 36591');
INSERT INTO "customers" VALUES(9,'Kimberly Ingram','ronaldgates@example.org','966 Morgan Wall
Rodriguezview, VA 39939');
INSERT INTO "customers" VALUES(10,'Sarah Foster','herrerajonathan@example.net','35865 Friedman Club
Pollardberg, VA 06092');
CREATE TABLE order_items (
	id INTEGER NOT NULL, 
	order_id INTEGER, 
	product_id INTEGER, 
	quantity INTEGER, 
	unit_price FLOAT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(order_id) REFERENCES orders (id), 
	FOREIGN KEY(product_id) REFERENCES products (id)
);
INSERT INTO "order_items" VALUES(1,1,19,2,173.45);
INSERT INTO "order_items" VALUES(2,1,4,1,309.15);
INSERT INTO "order_items" VALUES(3,1,20,2,230.2);
INSERT INTO "order_items" VALUES(4,2,6,2,24.49);
INSERT INTO "order_items" VALUES(5,3,20,3,230.2);
INSERT INTO "order_items" VALUES(6,4,14,3,443.07);
INSERT INTO "order_items" VALUES(7,4,20,3,230.2);
INSERT INTO "order_items" VALUES(8,4,6,2,24.49);
INSERT INTO "order_items" VALUES(9,4,6,2,24.49);
INSERT INTO "order_items" VALUES(10,5,5,1,162.58);
INSERT INTO "order_items" VALUES(11,6,8,3,127.75);
INSERT INTO "order_items" VALUES(12,6,7,1,315.72);
INSERT INTO "order_items" VALUES(13,6,20,1,230.2);
INSERT INTO "order_items" VALUES(14,6,4,3,309.15);
INSERT INTO "order_items" VALUES(15,7,17,2,488.38);
INSERT INTO "order_items" VALUES(16,7,19,3,173.45);
INSERT INTO "order_items" VALUES(17,7,3,1,13.27);
INSERT INTO "order_items" VALUES(18,7,1,2,248.29);
INSERT INTO "order_items" VALUES(19,8,7,2,315.72);
INSERT INTO "order_items" VALUES(20,9,12,3,497.44);
INSERT INTO "order_items" VALUES(21,10,11,1,254.89);
INSERT INTO "order_items" VALUES(22,10,2,3,161.44);
INSERT INTO "order_items" VALUES(23,11,7,1,315.72);
INSERT INTO "order_items" VALUES(24,11,7,2,315.72);
INSERT INTO "order_items" VALUES(25,12,13,2,28.7);
INSERT INTO "order_items" VALUES(26,13,18,2,109.99);
INSERT INTO "order_items" VALUES(27,13,7,3,315.72);
INSERT INTO "order_items" VALUES(28,13,6,1,24.49);
INSERT INTO "order_items" VALUES(29,13,9,2,34.93);
INSERT INTO "order_items" VALUES(30,14,10,2,454.52);
INSERT INTO "order_items" VALUES(31,14,13,3,28.7);
INSERT INTO "order_items" VALUES(32,15,18,1,109.99);
INSERT INTO "order_items" VALUES(33,15,17,2,488.38);
INSERT INTO "order_items" VALUES(34,15,15,3,132.4);
INSERT INTO "order_items" VALUES(35,16,2,3,161.44);
INSERT INTO "order_items" VALUES(36,16,4,3,309.15);
INSERT INTO "order_items" VALUES(37,16,15,2,132.4);
INSERT INTO "order_items" VALUES(38,16,6,2,24.49);
INSERT INTO "order_items" VALUES(39,17,15,3,132.4);
INSERT INTO "order_items" VALUES(40,18,1,1,248.29);
INSERT INTO "order_items" VALUES(41,18,13,1,28.7);
INSERT INTO "order_items" VALUES(42,19,7,2,315.72);
INSERT INTO "order_items" VALUES(43,19,15,2,132.4);
INSERT INTO "order_items" VALUES(44,19,17,1,488.38);
INSERT INTO "order_items" VALUES(45,20,9,1,34.93);
INSERT INTO "order_items" VALUES(46,20,1,2,248.29);
INSERT INTO "order_items" VALUES(47,20,8,1,127.75);
INSERT INTO "order_items" VALUES(48,21,6,3,24.49);
INSERT INTO "order_items" VALUES(49,21,13,2,28.7);
CREATE TABLE orders (
	id INTEGER NOT NULL, 
	customer_id INTEGER, 
	status VARCHAR, 
	created_at DATETIME, 
	total_amount FLOAT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(customer_id) REFERENCES customers (id)
);
INSERT INTO "orders" VALUES(1,1,'shipped','2026-01-17 08:10:55.882892',1.116449999999999819e+03);
INSERT INTO "orders" VALUES(2,1,'delivered','2026-01-17 08:10:56.798320',48.98);
INSERT INTO "orders" VALUES(3,1,'delivered','2026-01-17 08:10:57.569659',6.90599999999999909e+02);
INSERT INTO "orders" VALUES(4,2,'pending','2026-01-17 08:10:58.777218',2117.77);
INSERT INTO "orders" VALUES(5,3,'delivered','2026-01-17 08:11:00.235074',162.58);
INSERT INTO "orders" VALUES(6,3,'shipped','2026-01-17 08:11:09.097900',1856.62);
INSERT INTO "orders" VALUES(7,4,'pending','2026-01-17 08:11:13.649041',2.006959999999999809e+03);
INSERT INTO "orders" VALUES(8,4,'cancelled','2026-01-17 08:11:15.546856',631.44);
INSERT INTO "orders" VALUES(9,4,'delivered','2026-01-17 08:11:17.327571',1492.32);
INSERT INTO "orders" VALUES(10,5,'cancelled','2026-01-17 08:11:21.656162',739.21);
INSERT INTO "orders" VALUES(11,5,'pending','2026-01-17 08:11:24.233784',9.47160000000000082e+02);
INSERT INTO "orders" VALUES(12,5,'cancelled','2026-01-17 08:11:26.136969',57.4);
INSERT INTO "orders" VALUES(13,6,'pending','2026-01-17 08:11:28.671921',1261.49);
INSERT INTO "orders" VALUES(14,7,'delivered','2026-01-17 08:11:31.447045',995.14);
INSERT INTO "orders" VALUES(15,8,'pending','2026-01-17 08:11:34.121532',1483.95);
INSERT INTO "orders" VALUES(16,8,'cancelled','2026-01-17 08:11:35.514125',1725.55);
INSERT INTO "orders" VALUES(17,8,'cancelled','2026-01-17 08:11:36.327988',3.972000000000000455e+02);
INSERT INTO "orders" VALUES(18,9,'delivered','2026-01-17 08:11:37.935801',276.99);
INSERT INTO "orders" VALUES(19,9,'pending','2026-01-17 08:11:40.521770',1384.62);
INSERT INTO "orders" VALUES(20,9,'shipped','2026-01-17 08:11:41.851249',659.26);
INSERT INTO "orders" VALUES(21,10,'cancelled','2026-01-17 08:11:43.409993',130.87);
CREATE TABLE products (
	id INTEGER NOT NULL, 
	name VARCHAR, 
	description TEXT, 
	price FLOAT, 
	stock_level INTEGER, 
	category VARCHAR, 
	PRIMARY KEY (id)
);
INSERT INTO "products" VALUES(1,'Police Yard','Structure source color seat bar trip success. Year so gas citizen. Add hotel end other camera.',248.29,16,'couple');
INSERT INTO "products" VALUES(2,'Piece Western','Tax yeah call great thing interesting. Attorney listen certain activity drop thing. Vote democratic man.',161.44,31,'yourself');
INSERT INTO "products" VALUES(3,'As Discussion','Single game significant personal almost. Up tax out yard debate town.',13.27,35,'matter');
INSERT INTO "products" VALUES(4,'Rise Suggest','Where group minute last card position certain. Reflect sound class six.',309.15,79,'senior');
INSERT INTO "products" VALUES(5,'Arm Arm','Woman rich seek pay even man. Rise interview bank fall bit. Interest first few scene provide music authority.',162.58,49,'not');
INSERT INTO "products" VALUES(6,'Take Whole','Heavy north wide. Seven finish sure. Probably indeed choice author similar task positive. Born scientist movie.',24.49,86,'security');
INSERT INTO "products" VALUES(7,'Day Social','Home camera sense factor strategy arm administration. Level stop choose.',315.72,51,'gun');
INSERT INTO "products" VALUES(8,'Nation Really','Area right power anyone force amount. Policy might car figure economy tree society.',127.75,44,'keep');
INSERT INTO "products" VALUES(9,'Ability List','Either necessary service risk forward weight serve. Late he level on. City stand care build.',34.93,75,'sister');
INSERT INTO "products" VALUES(10,'Information Across','Direction father peace final approach. Board thus hard away society adult writer. Owner activity during painting person southern value.',454.52,76,'type');
INSERT INTO "products" VALUES(11,'Movement Garden','Tend guy skin movement degree throughout. Sign may significant politics option meet myself. Poor maybe natural beyond cultural maybe.',254.89,4,'style');
INSERT INTO "products" VALUES(12,'In Third','Bring world hard near course represent. Personal bad bit personal.',497.44,19,'arm');
INSERT INTO "products" VALUES(13,'Land Any','Rich question million art develop. Ago share bar plan attorney their describe religious. Simple move responsibility economic. Deep kid option whatever community pick realize ground.',28.7,36,'hair');
INSERT INTO "products" VALUES(14,'Nature Great','Hard down help southern guess specific. Offer government she quality protect.',443.07,25,'conference');
INSERT INTO "products" VALUES(15,'Media Choice','Figure well century then fire issue. Central machine give issue.',132.4,6,'indeed');
INSERT INTO "products" VALUES(16,'Do Cell','These despite small product despite west particular. Moment American decade marriage. Hope floor film choice will.',373.61,13,'majority');
INSERT INTO "products" VALUES(17,'Reach Ten','Oil meet herself against who doctor off year. Score just prevent fund you. Fear rest official provide weight friend during.',488.38,87,'movie');
INSERT INTO "products" VALUES(18,'System During','Town sometimes medical involve ago ten protect. Charge office when score product level. Service down magazine film simple performance least sometimes.',109.99,96,'collection');
INSERT INTO "products" VALUES(19,'Live Knowledge','Represent I skill discussion audience no dream source. Away stop own easy do history fact. Production her mouth fast.',173.45,2,'people');
INSERT INTO "products" VALUES(20,'Significant Want','Between minute while. Particular visit save growth hold poor bank.',230.2,9,'some');
CREATE INDEX ix_products_id ON products (id);
CREATE INDEX ix_products_name ON products (name);
CREATE INDEX ix_customers_id ON customers (id);
CREATE UNIQUE INDEX ix_customers_email ON customers (email);
CREATE INDEX ix_orders_id ON orders (id);
CREATE INDEX ix_order_items_id ON order_items (id);
COMMIT;
