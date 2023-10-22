"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep= ";")

    df.sexo = df.sexo.str.lower()

    df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.str.lower()
    
    df.idea_negocio = df.idea_negocio.str.lower()
    df.idea_negocio = df.idea_negocio.str.replace(' ', '_', regex=False)
    df.idea_negocio = df.idea_negocio.str.replace('-', '_', regex=False)

    df.barrio = df.barrio.str.rstrip()
    df.barrio = df.barrio.str.lower()
    df.barrio = df.barrio.str.replace('-', ' ', regex=False)
    df.barrio = df.barrio.str.replace('_', ' ', regex=False)
    df.barrio = df.barrio.str.rstrip()
    df.barrio = df.barrio.str.replace("no. ", "no.", regex=False)
    df.barrio = df.barrio.str.replace(' ', '_', regex=False)
    df.barrio = df.barrio.str.replace('-', '_', regex=False)
    df.barrio = df.barrio.str.replace('bel¿n', 'belen', regex=False)
    df.barrio = df.barrio.str.replace('boyac¿', 'boyaca', regex=False)
    df.barrio = df.barrio.str.replace('andaluc¿a', 'andalucia', regex=False)
    df.barrio = df.barrio.str.replace('antonio_nari¿o', 'antonio_narino', regex=False)
    df.barrio = df.barrio.str.replace('barrio_caycedo', 'barrio_caicedo', regex=False)
    df.barrio = df.barrio.str.replace('antonio_nariño', 'antonio_narino', regex=False)
    df.barrio = df.barrio.str.replace('campo_vald¿s_no.1', 'campo_valdes_no.1', regex=False)
    df.barrio = df.barrio.str.replace('veinte_de_julio', '20_de_julio', regex=False)

    df.estrato = df.estrato.astype('int')

    df.comuna_ciudadano = df.comuna_ciudadano.round()
    df.comuna_ciudadano = df.comuna_ciudadano.astype(pd.Int64Dtype())

    fecha_split = df.fecha_de_beneficio.str.split("/")
    dia, mes, ano = [], [], []
    for fecha in fecha_split:
        dia.append(fecha[0])
        mes.append(fecha[1])
        ano.append(fecha[2])

    dia_ok, ano_ok = [], []
    for date in range(len(dia)):
        if int(dia[date]) > 31:
            dia_ok.append(ano[date])
            ano_ok.append(dia[date])
        else:
            dia_ok.append(dia[date])
            ano_ok.append(ano[date])
        

    fecha_ok = []
    for day, month, year in zip(dia_ok, mes, ano_ok):
        fecha_ok.append(f"{day}/{month}/{year}")

    fechas_df = pd.DataFrame(fecha_ok)

    df.fecha_de_beneficio = fechas_df
    df.fecha_de_beneficio.value_counts()

    df.monto_del_credito = df.monto_del_credito.str.strip("$")
    df.monto_del_credito = df.monto_del_credito.str.strip(" ")
    df.monto_del_credito = df.monto_del_credito.replace(",", "", regex=True)
    df.monto_del_credito = df.monto_del_credito.astype('float')

    df.línea_credito = df.línea_credito.str.lower()
    df.línea_credito = df.línea_credito.str.rstrip()
    df.línea_credito = df.línea_credito.str.replace('-', ' ', regex=False)
    df.línea_credito = df.línea_credito.str.replace('_', ' ', regex=False)
    df.línea_credito = df.línea_credito.str.rstrip()
    
    return df