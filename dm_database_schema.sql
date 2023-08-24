create database dmplat;

use dmplat;

-- APP 使用者資料
create table user(
user_id			int auto_increment  	comment "使用者編號",
user_name		varchar(16)	not null 	comment "使用者名稱",
user_account	varchar(64) not null 	comment "使用者帳號(電子信箱)",
user_password	varchar(256) not null 	comment "使用者密碼(hash)",
born_date		date					comment	"出生年月日",
telephone		varchar(16)				comment	"連絡電話",
address			varchar(64)				comment	"住址",
user_type		int						comment "使用者類型(1:病人, 2:照護者)",
institution_id	int						comment	"收案醫院代號",
create_time		datetime				comment	"建立時間",
update_time		datetime				comment	"修改時間",
delete_time		datetime				comment	"刪除時間",
primary key (user_id)
);

-- 紀錄類型參數
create table record_type(	
type_id			int auto_increment		comment	"紀錄類別編號",
record_name		varchar(16)	not null	comment	"記錄類型名稱",
record_unit		varchar(16)	not null	comment	"紀錄單位",
record_group	int						comment "紀錄類型(1:檢驗數據,, 2:自主監測數據)",
create_time		datetime				comment	"建立時間",
update_time		datetime				comment	"修改時間",
delete_time		datetime				comment	"刪除時間",
primary key (type_id)
);

-- 日常監控數據
create table self_health_data(
self_health_id	int auto_increment		comment	"監控數據編號",
patient_id		int     				comment	"病人代碼",
recorder_id		int 					comment	"紀錄者代碼",
record_type		int     				comment	"紀錄類型",
record_date		date					comment	"紀錄日期",
record			double					comment	"紀錄數值",
create_time		datetime				comment	"建立時間",
update_time		datetime				comment	"修改時間",
delete_time		datetime				comment	"刪除時間",
primary key (self_health_id)
);



-- 選取 Table name
SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME="self_health_data";