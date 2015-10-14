#!flask/bin/python
from flask import Flask, jsonify, abort, request

app = Flask(__name__)

users = [
    {
        'user_id': 1,
        'user_fullname': 'Gary Figuerola Mora',
        'user_nickname': 'garyfimo',
        'user_password': '123'
    },
    {
        'user_id': 2,
        'user_fullname': 'Percy Quevedo',
        'user_nickname': 'pquevedo',
        'user_password': '987'
    }
]

detailPDV = {
    "listColaborador": [
        {
            "asistenciaColaborador": "Tarde",
            "horaAperturaColaborador": "10:00:00",
            "horaLlegadaColaborador": "10:01",
            "nombreColaborador": "ELTHON JOHN NANO QUINONEZ"
        },
        {
            "asistenciaColaborador": "Puntual",
            "horaAperturaColaborador": "10:00:00",
            "horaLlegadaColaborador": "09:59",
            "nombreColaborador": "MARIA LUZ TACUCHE CHUQUIYAURI"
        }
    ]
}

listPDV = {
    "listPDV": [
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "08:00",
            "idPDV": 24,
            "nombrePDV": "MINKA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "08:00",
            "idPDV": 123,
            "nombrePDV": "MATARANI"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "08:00",
            "idPDV": 126,
            "nombrePDV": "EJERCITO CAYMA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "08:00",
            "idPDV": 223,
            "nombrePDV": "HUANUCO"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "08:00",
            "idPDV": 230,
            "nombrePDV": "OFICINAS PUCALLPA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "08:00",
            "idPDV": 231,
            "nombrePDV": "OFICINAS IQUITOS"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "08:00",
            "idPDV": 232,
            "nombrePDV": "OFICINAS HUANUCO"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "08:00",
            "idPDV": 233,
            "nombrePDV": "OFICINAS TACNA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "08:00",
            "idPDV": 234,
            "nombrePDV": "OFICINAS AREQUIPA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "08:30",
            "idPDV": 170,
            "nombrePDV": "IQUITOS II"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "08:30",
            "idPDV": 67,
            "nombrePDV": "VENTANILLA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "08:30",
            "idPDV": 68,
            "nombrePDV": "VENTANILLA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "08:30",
            "idPDV": 73,
            "nombrePDV": "SAN JUAN DE MIRAFLORES"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:00",
            "idPDV": 74,
            "nombrePDV": "VILLA EL SALVADOR"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:00",
            "idPDV": 75,
            "nombrePDV": "SAN JUAN DE MIRAFLORES"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:00",
            "idPDV": 78,
            "nombrePDV": "LURIN"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:00",
            "idPDV": 64,
            "nombrePDV": "SAN MARTIN DE PORRES"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:00",
            "idPDV": 65,
            "nombrePDV": "SAN MARTIN DE PORRES"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:00",
            "idPDV": 66,
            "nombrePDV": "SAN MARTIN DE PORRES"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:00",
            "idPDV": 71,
            "nombrePDV": "BRENA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:00",
            "idPDV": 80,
            "nombrePDV": "VILLA EL SALVADOR"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:00",
            "idPDV": 90,
            "nombrePDV": "MERCADERES"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:00",
            "idPDV": 92,
            "nombrePDV": "ISLAY"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:00",
            "idPDV": 93,
            "nombrePDV": "MOLLENDO"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:00",
            "idPDV": 95,
            "nombrePDV": "CREDISHOP PEDREGAL"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:00",
            "idPDV": 98,
            "nombrePDV": "PEDREGAL"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:00",
            "idPDV": 101,
            "nombrePDV": "ELECTRO"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:00",
            "idPDV": 105,
            "nombrePDV": "MOLLENDO 2"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:00",
            "idPDV": 108,
            "nombrePDV": "AREQUIPA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:00",
            "idPDV": 20,
            "nombrePDV": "MINKA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:00",
            "idPDV": 33,
            "nombrePDV": "PUENTE PIEDRA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:00",
            "idPDV": 1,
            "nombrePDV": "INDEPENDENCIA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:00",
            "idPDV": 4,
            "nombrePDV": "INDEPENDENCIA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:00",
            "idPDV": 35,
            "nombrePDV": "COMAS"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:00",
            "idPDV": 36,
            "nombrePDV": "COMAS"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:00",
            "idPDV": 44,
            "nombrePDV": "SAN MIGUEL"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:00",
            "idPDV": 55,
            "nombrePDV": "LOS OLIVOS"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:00",
            "idPDV": 61,
            "nombrePDV": "RIMAC"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:00",
            "idPDV": 171,
            "nombrePDV": "PUCALLPA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:00",
            "idPDV": 161,
            "nombrePDV": "HUANUCO"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:00",
            "idPDV": 163,
            "nombrePDV": "IQUITOS"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:00",
            "idPDV": 180,
            "nombrePDV": "ILO"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:00",
            "idPDV": 183,
            "nombrePDV": "TACNA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:00",
            "idPDV": 120,
            "nombrePDV": "MOLLENDO"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:00",
            "idPDV": 151,
            "nombrePDV": "HUANUCO"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:00",
            "idPDV": 153,
            "nombrePDV": "TINGO MARIA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:00",
            "idPDV": 154,
            "nombrePDV": "CERRO DE PASCO"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:00",
            "idPDV": 155,
            "nombrePDV": "HUANUCO 1"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:00",
            "idPDV": 211,
            "nombrePDV": "VENTANILLA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:00",
            "idPDV": 212,
            "nombrePDV": "PUCALLPA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:00",
            "idPDV": 213,
            "nombrePDV": "HIPERBODEGA PRECIO UNO"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:00",
            "idPDV": 217,
            "nombrePDV": "CUSCO"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:30",
            "idPDV": 121,
            "nombrePDV": "AREQUIPA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:30",
            "idPDV": 107,
            "nombrePDV": "CAYMA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:30",
            "idPDV": 124,
            "nombrePDV": "PARRA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:30",
            "idPDV": 58,
            "nombrePDV": "LOS OLIVOS DOS"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:30",
            "idPDV": 53,
            "nombrePDV": "ANGELICA GAMARRA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:30",
            "idPDV": 16,
            "nombrePDV": "CANTA CALLAO"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:30",
            "idPDV": 18,
            "nombrePDV": "COLONIAL"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:30",
            "idPDV": 19,
            "nombrePDV": "COLONIAL"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:30",
            "idPDV": 25,
            "nombrePDV": "CALLAO"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:30",
            "idPDV": 26,
            "nombrePDV": "BELAUNDE"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:30",
            "idPDV": 28,
            "nombrePDV": "COMAS"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:30",
            "idPDV": 82,
            "nombrePDV": "PACHACUTEC"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "09:30",
            "idPDV": 88,
            "nombrePDV": "BRASIL2"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 85,
            "nombrePDV": "LURIN"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 87,
            "nombrePDV": "PEDRO MIOTA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 72,
            "nombrePDV": "NACIONES UNIDAS"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 70,
            "nombrePDV": "VENTANILLA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 109,
            "nombrePDV": "AREQUIPA 2"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 113,
            "nombrePDV": "AREQUIPA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 114,
            "nombrePDV": "AREQUIPA A CACERES"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 116,
            "nombrePDV": "CAYMA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 117,
            "nombrePDV": "PAUCARPATA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 102,
            "nombrePDV": "AVELINO"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 100,
            "nombrePDV": "MERCADERES"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 63,
            "nombrePDV": "ACHO"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 97,
            "nombrePDV": "CAMANA 2"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 30,
            "nombrePDV": "PUENTE PIEDRA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 21,
            "nombrePDV": "BELLAVISTA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 23,
            "nombrePDV": "QUILCA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 17,
            "nombrePDV": "CALLAO"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 13,
            "nombrePDV": "SAN JUAN DE LURIGANCHO"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 56,
            "nombrePDV": "TOMAS VALLE"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 60,
            "nombrePDV": "CANTA CENTRAL"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 45,
            "nombrePDV": "SAN MIGUEL"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 47,
            "nombrePDV": "LA MARINA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 50,
            "nombrePDV": "RISSO"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 38,
            "nombrePDV": "COMAS"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 39,
            "nombrePDV": "BRASIL"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 40,
            "nombrePDV": "PUEBLO LIBRE"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 42,
            "nombrePDV": "SAN MIGUEL"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 119,
            "nombrePDV": "RIVERO"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 157,
            "nombrePDV": "TINGO MARIA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 158,
            "nombrePDV": "HUANUCO"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 159,
            "nombrePDV": "PASCO"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 160,
            "nombrePDV": "TINGO MARIA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 129,
            "nombrePDV": "CUSCO"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 132,
            "nombrePDV": "CUSCO"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 188,
            "nombrePDV": "JUANJUI"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 189,
            "nombrePDV": "MOYOBAMBA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 192,
            "nombrePDV": "YURIMAGUAS"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 193,
            "nombrePDV": "MOYOBAMBA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 196,
            "nombrePDV": "YURIMAGUAS"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 197,
            "nombrePDV": "TARAPOTO"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 198,
            "nombrePDV": "YURIMAGUAS"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 199,
            "nombrePDV": "MOYOBAMBA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 202,
            "nombrePDV": "JUANJUI"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 165,
            "nombrePDV": "IQUITOS"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 173,
            "nombrePDV": "PUCALLPA II"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 175,
            "nombrePDV": "PUCALLPA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 177,
            "nombrePDV": "JULIACA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 168,
            "nombrePDV": "IQUITOS"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 169,
            "nombrePDV": "IQUITOS"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 208,
            "nombrePDV": "PUCALLPA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:00",
            "idPDV": 209,
            "nombrePDV": "IQUITOS"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:30",
            "idPDV": 32,
            "nombrePDV": "PUENTE PIEDRA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "10:30",
            "idPDV": 96,
            "nombrePDV": "AREQUIPA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "11:00",
            "idPDV": 106,
            "nombrePDV": "PEDREGAL"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "11:00",
            "idPDV": 118,
            "nombrePDV": "LAMBRAMANI"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "11:00",
            "idPDV": 79,
            "nombrePDV": "VILLA MARIA DEL TRIUNFO"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "11:00",
            "idPDV": 81,
            "nombrePDV": "VILLA MARIA DEL TRIUNFO"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "11:00",
            "idPDV": 89,
            "nombrePDV": "GARCIA CARBAJAL"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "11:00",
            "idPDV": 34,
            "nombrePDV": "COMAS"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "11:00",
            "idPDV": 2,
            "nombrePDV": "LOS OLIVOS"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "11:00",
            "idPDV": 3,
            "nombrePDV": "INDEPENDENCIA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "11:00",
            "idPDV": 62,
            "nombrePDV": "RIMAC"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "11:00",
            "idPDV": 54,
            "nombrePDV": "MEGA PLAZA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "11:00",
            "idPDV": 218,
            "nombrePDV": "PORONGOCHE"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "11:00",
            "idPDV": 178,
            "nombrePDV": "PUNO"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "11:00",
            "idPDV": 166,
            "nombrePDV": "IQUITOS"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "11:00",
            "idPDV": 164,
            "nombrePDV": "IQUITOS II"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "11:00",
            "idPDV": 204,
            "nombrePDV": "SALAVERRY"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "11:00",
            "idPDV": 133,
            "nombrePDV": "CUSCO"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "11:00",
            "idPDV": 152,
            "nombrePDV": "CERRO DE PASCO"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "11:00",
            "idPDV": 122,
            "nombrePDV": "AREQUIPA"
        },
        {
            "coberturaCompletaPDV": 2,
            "coberturadoPDV": "SI",
            "horaAperturaPDV": "11:00",
            "idPDV": 127,
            "nombrePDV": "CUSCO TIENDA AYACUCHO"
        }
    ]
}


@app.route('/')
def home():
    return "SERVICIO CORRIENDO"

@app.route('/login', methods=['POST'])
def get_user():
    if not request.json or not 'username' or not 'user_password' in request.json:
        abort(400)
    user_response = {
        'user_id' : -1,
            'user_fullname': '',
            'user_nickname': '',
            'user_password': ''
    }
    for u in users:
        if request.json['username'] == u['user_nickname'] and request.json['user_password'] == u['user_password']:
            user_response = u
    return jsonify(user_response)

@app.route('/listPDV', methods=['GET'])
def get_store():
    return jsonify(listPDV)

@app.route('/detailPDV', methods=['GET'])
def get_stores():
    return jsonify(detailPDV)


if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
