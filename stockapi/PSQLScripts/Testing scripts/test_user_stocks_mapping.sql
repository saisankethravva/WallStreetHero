-- test case
-- |Stock|User|
-- |v|v|
-- |v|n|
-- |n|v|
-- |n|n|
CALL sp_add_user_stock_mapping('rp', 'COIN');
CALL sp_add_user_stock_mapping('rp', 'COINs');
CALL sp_add_user_stock_mapping('rp1', 'COIN');
CALL sp_add_user_stock_mapping('rps', 'COINs')