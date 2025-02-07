############################################# PARA HISTÓRICOS ###################################################
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_excel('Data_empleados_historico .xlsx', sheet_name='Data_empleados_historico')

data = data.drop(columns=['horas_quincena', 'mayor_edad', 'Unnamed: 0', 'empleados', 'sexo'])

mask_other_career = data['carrera'] == 'Other'
data.loc[~mask_other_career & ((data['educacion'].isnull()) | (data['educacion'].isin(['Secundaria', 'Tecnica', 'Bachillerato']))), 'educacion'] = 'Universitaria'
data['salario_mes'] = data['salario_mes'].astype(float)

data['implicacion'].fillna('No aplica', inplace=True)
data['satisfaccion_trabajo'].fillna('No aplica', inplace=True)
data['abandono'] = data['abandono'].map({'Yes': 'voluntario', 'No': 'otro motivo'})


data_cleaned = data.drop(columns=['anos_en_puesto', 'conciliacion'])
data_cleaned['educacion'].fillna(data_cleaned['educacion'].mode()[0], inplace=True)


print("Datos faltantes después de la limpieza:")
print(data_cleaned.isnull().sum().sort_values(ascending=False))


plt.figure(figsize=(10, 6))
sns.boxplot(x=data_cleaned['edad'])
plt.title('Distribución de Edad')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x=data_cleaned['salario_mes'])
plt.title('Distribución de Salario Mensual')
plt.show()

data_cleaned.to_csv('Data_empleados_historico_limpio.csv', index=False)



############################################# PARA ACTUALES #####################################################
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_actuales = pd.read_excel('Data_empleados_actuales_.xlsx')

data_actuales = data_actuales.drop(columns=['horas_quincena', 'mayor_edad', 'Unnamed: 0', 'empleados', 'sexo'])

mask_other_career = data_actuales['carrera'] == 'Other'
data_actuales.loc[~mask_other_career & ((data_actuales['educacion'].isnull()) | (data_actuales['educacion'].isin(['Secundaria', 'Tecnica', 'Bachillerato']))), 'educacion'] = 'Universitaria'

data_actuales['salario_mes'] = data_actuales['salario_mes'].astype(float)

data_actuales_cleaned = data_actuales.drop(columns=['anos_en_puesto', 'conciliacion'])

data_actuales_cleaned['educacion'].fillna(data_actuales_cleaned['educacion'].mode()[0], inplace=True)
data_actuales_cleaned['implicacion'].fillna('No aplica', inplace=True)
data_actuales_cleaned['satisfaccion_trabajo'].fillna('No aplica', inplace=True)

print("Datos faltantes después de la limpieza:")
print(data_actuales_cleaned.isnull().sum().sort_values(ascending=False))

plt.figure(figsize=(10, 6))
sns.boxplot(x=data_actuales_cleaned['edad'])
plt.title('Distribución de Edad - Empleados Actuales')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x=data_actuales_cleaned['salario_mes'])
plt.title('Distribución de Salario Mensual - Empleados Actuales')
plt.show()

data_actuales_cleaned.to_csv('Data_empleados_actuales_limpio.csv', index=False)

