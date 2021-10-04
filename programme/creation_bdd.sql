
use open_food_facts;

create database if not exists open_food_facts;



create table if not exists category(ID smallint unsigned not null auto_increment primary key, name varchar(150) not null ) engine = innodb;
create table if not exists food_items(ID smallint unsigned not null auto_increment , name varchar(150) , category_ID smallint unsigned , description varchar(255),nutriscore varchar(1), shop varchar(255), brand varchar(255), url varchar(500) , primary key (ID  )) engine = innodb;
create table if not exists registred_food(ID smallint unsigned not null auto_increment , product varchar(150), substtituant varchar(150), primary key (ID)) engine = innodb