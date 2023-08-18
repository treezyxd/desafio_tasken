SELECT NOME, TELEFONE FROM tbl_Clientes 
INNER JOIN tbl_Telefones
ON tbl_Clientes.CPF = tbl_Telefones.CPF_CLIENTE