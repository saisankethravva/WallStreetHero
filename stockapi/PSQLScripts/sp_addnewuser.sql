DROP PROCEDURE IF EXISTS sp_add_new_user(
	
	password VARCHAR ( 50 ) ,
	fname VARCHAR ( 255 ),
	lname VARCHAR ( 255 ),
	phone_no VARCHAR ( 255 ) ,
	emailid VARCHAR ( 255 ));
	
create or replace procedure sp_add_new_user(
	
	password VARCHAR ( 50 ) ,
	fname VARCHAR ( 255 ),
	lname VARCHAR ( 255 ),
	phone_no VARCHAR ( 255 ) ,
	emailid VARCHAR ( 255 ))

language plpgsql	
as $$
DECLARE 
		userid INT;
		roleid INT;
BEGIN
	
	insert into users(email, fn, ln, phone_no, created_on, password )
	values(emailid, fname, lname, phone_no,CURRENT_TIMESTAMP, password );
	
	select user_id into userid from users u where u.email = emailid ;
	select role_id into roleid from roles where role_name = 'user' ;
	insert into users_roles (user_id, role_id) values (userid, roleid);
END;
$$;