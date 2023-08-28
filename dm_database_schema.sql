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

-- 日常監控數據
create table self_health_data(
self_health_id	int auto_increment		comment	"監控數據編號",
patient_id		int     				comment	"病人代碼",
recorder_id		int 					comment	"紀錄者代碼",
record_type		int     				comment	"紀錄類型",
record_time		datetime				comment	"紀錄時間",
record			double					comment	"紀錄數值",
create_time		datetime				comment	"建立時間",
update_time		datetime				comment	"修改時間",
delete_time		datetime				comment	"刪除時間",
primary key (self_health_id)
);

-- 回診/就診紀錄 medical_records
create table medical_records(
medical_record_id	int auto_increment  comment "回診記錄編號",
record_date			date				comment	"回診/就診日期",
patient_id			int     			comment	"病人代碼",
institution_id		int 				comment	"醫療機構編號",
doctor_id			int 				comment	"看診醫師編號",
dietitian_id		int 				comment	"營養師編號",
educator_id			int 				comment	"衛教師編號",
phase_type			int					comment	"追蹤階段編號",
prescription_id		int					comment "處方簽編號",		
memo				text				comment "備忘紀錄",
follow_up_date		date				comment "下次回診日期",
create_time			datetime			comment	"建立時間",
update_time			datetime			comment	"修改時間",
delete_time			datetime			comment	"刪除時間",
primary key (medical_record_id)
-- foreign key (patient_id) 	references user(user_id),
-- foreign key (institution_id) references medical_institution(institution_id),
-- foreign key (doctor_id) 		references medical_staff(staff_id),
-- foreign key (dietitian_id) 	references medical_staff(staff_id),
-- foreign key (educator_id) 	references medical_staff(staff_id),
-- foreign key (phase_type) 	references phase_type(phase_id),
-- foreign key (prescription_id) references prescription(prescription_id)
);

-- 檢驗數據
create table medical_records_data(
medical_record_data_id	int auto_increment  comment "檢驗數據編號",
medical_record_id		int 				comment "回診記錄編號",
record_type				int 				comment	"紀錄類別編號",
record					double				comment	"檢驗數據",
test_date				date				comment "檢驗時間",
create_time				datetime			comment	"建立時間",
update_time				datetime			comment	"修改時間",
delete_time				datetime			comment	"刪除時間",
primary key (medical_record_data_id)
-- foreign key (record_type) 	references record_type(type_id)
);

-- 醫療機構
create table medical_institution(
institution_id		int auto_increment		comment	"醫療機構編號",
institution_name	varchar(32)				comment "醫療機構名稱",
institution_type	int						comment "醫療機構類型[醫學中心, 區域醫院, 地區醫院, 診所, 衛生局]",
telephone			varchar(16)				comment	"連絡電話",
address				varchar(64)				comment	"住址",
contact_person		varchar(16)	not null 	comment "聯絡人名稱",
create_time			datetime				comment	"建立時間",
update_time			datetime				comment	"修改時間",
delete_time			datetime				comment	"刪除時間",
primary key (institution_id)
);

-- 醫事人員
create table  medical_staff(
staff_id			int auto_increment		comment	"醫事人員代號",
staff_name			varchar(16)	not null 	comment "醫事人員名稱",
staff_account		varchar(64) not null 	comment "醫事人員帳號",
staff_password		varchar(256) not null 	comment "醫事人員密碼(hash)",
staff_position_code	int						comment "職位類別[1:醫師, 2:護理師, 3:營養師, 4:中心營養師, 5:中心個案管理師, 6:中心衛教師]",
staff_position		varchar(16)				comment "職稱",
create_time			datetime				comment	"建立時間",
update_time			datetime				comment	"修改時間",
delete_time			datetime				comment	"刪除時間",
primary key (staff_id)
);

-- 醫療機構與人員關聯表
create table institution_staff_relate(
relate_id			int auto_increment	comment	"關聯編號",
institution_id		int 				comment	"醫療機構代號",
staff_id			int 				comment	"醫事人員代號",
create_time			datetime			comment	"建立時間",
update_time			datetime			comment	"修改時間",
delete_time			datetime			comment	"刪除時間",
primary key (relate_id)
-- foreign key (institution_id) references medical_institution(institution_id),
-- foreign key (staff_id) references medical_staff(staff_id)
);

-- 處方籤紀錄
create table prescription_relate(
relate_id			int auto_increment	comment	"關聯代碼",
prescription_id		int 				comment	"處方籤編號",
medicine_id			int					comment	"藥品代碼",
create_time			datetime			comment	"建立時間",
update_time			datetime			comment	"修改時間",
delete_time			datetime			comment	"刪除時間",
primary key (relate_id)
-- foreign key (medicine_id) references medicine(medicine_id)
-- foreign key (prescription_id) references medical_records(prescription_id)
);

-- 藥品與使用指示資料
create table medicine(
medicine_id			int auto_increment	comment	"藥品代碼",
medicine_name		varchar(64)			comment "藥品名稱",
medicine_dosage		varchar(64)			comment "藥品劑量服用方式",
create_time			datetime			comment	"建立時間",
update_time			datetime			comment	"修改時間",
delete_time			datetime			comment	"刪除時間",
primary key (medicine_id)
);

-- 紀錄類型參數
create table record_type(	
type_id			int auto_increment		comment	"紀錄類別編號",
record_name		varchar(16)	not null	comment	"記錄類型名稱",
record_name_cn	varchar(16)	not null	comment	"記錄類型中文名稱",
record_unit		varchar(16)	not null	comment	"紀錄單位",
record_group	int						comment "紀錄類型(1:檢驗數據,, 2:自主監測數據)",
create_time		datetime				comment	"建立時間",
update_time		datetime				comment	"修改時間",
delete_time		datetime				comment	"刪除時間",
primary key (type_id)
);

-- 階段參數
create table phase_type(
phase_id		int auto_increment		comment	"階段參數編號",
diseases_name	varchar(16)	not null	comment	"適應症(計畫)",
phase_code		varchar(16)				comment "追蹤階段代碼",
phase_name		varchar(16)	not null	comment	"追蹤階段",
create_time		datetime				comment	"建立時間",
update_time		datetime				comment	"修改時間",
delete_time		datetime				comment	"刪除時間",
primary key (phase_id)
);




-- 選取 Table name
SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME="self_health_data";