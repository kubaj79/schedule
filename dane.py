import pandas
import datetime
df=pandas.read_excel("sp_1.xlsx",sheet_name='Apteka')
df_a=pandas.read_excel("sp_1.xlsx",sheet_name='Apteka')
df_k=pandas.read_excel("sp_1.xlsx",sheet_name='Komputerowa')
df_2=pandas.read_excel("sp_1.xlsx",sheet_name='Aula_2')
df_3=pandas.read_excel("sp_1.xlsx",sheet_name='Aula_3')
df_4a=pandas.read_excel("sp_1.xlsx",sheet_name='4_A')
df_4b=pandas.read_excel("sp_1.xlsx",sheet_name='4_B')
df_45=pandas.read_excel("sp_1.xlsx",sheet_name='45')
df_46=pandas.read_excel("sp_1.xlsx",sheet_name='46')
df_213=pandas.read_excel("sp_1.xlsx",sheet_name='213')
df_214=pandas.read_excel("sp_1.xlsx",sheet_name='214')
df_leg=pandas.read_excel("sp_1.xlsx",sheet_name='leg')

def dane(df):
    l=[]
    aula=[]
    for i in range(len(df)):
        aula=(df.iloc[i,0:len(df.columns)].tolist())
        for n,j in enumerate(aula):
            if type(j) is datetime.time:
                aula[n]=aula[n].strftime("%H,%M,%S")
        l.append(aula)
    return l

def apteka():
    return dane(df_a)

def komputerowa():
    return dane(df_k)

def aula2():
    return dane(df_2)

def aula3():
    return dane(df_3)

def aula4a():
    return dane(df_4a)

def aula4b():
    return dane(df_4b)

def sala45():
    return dane(df_45)

def sala46():
    return dane(df_46)

def sala213():
    return dane(df_213)

def sala214():
    return dane(df_214)

def legeda():
    return dane(df_leg)
