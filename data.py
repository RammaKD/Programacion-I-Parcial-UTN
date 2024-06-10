from funciones_archivos import *

lista_pacientes = []
lista_grupos_sanguineos = ["A+","B+","AB+","O+","A-","B-","AB-","O-"]
lista_diccionarios_compatibilidad = [{"grupo sanguineo" : [("A+"), ("A+", "AB+"), ("O+", "O-", "A+", "A-")]},
                                     {"grupo sanguineo" : [("A-"), ("A+", "A-", "AB+", "AB-"), ("O-", "A-")]},
                                     {"grupo sanguineo" : [("B+"), ("B+", "AB+"), ("O+", "O-", "B+", "B-")]},
                                     {"grupo sanguineo" : [("B-"), ("B+", "B-", "AB+", "AB-"), ("O-", "B-")]},
                                     {"grupo sanguineo" : [("AB+"), ("AB+"), ("A+","B+","AB+","O+","A-","B-","AB-","O-")]},
                                     {"grupo sanguineo" : [("AB-"), ("AB+", "AB-"), ("AB-", "O-", "A-", "B-")]},
                                     {"grupo sanguineo" : [("O+"), ("A+", "B+", "AB+", "O+"), ("O+", "O-")]},
                                     {"grupo sanguineo" : [("O-"), ("A+","B+","AB+","O+","A-","B-","AB-","O-"), ("O-")]},]
path_csv = "Pacientes.csv"
path_json = "Bajas.json"
path_json_ultimo_id = "ultimo_id.json"
