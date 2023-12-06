from datetime import datetime, timedelta


datas = [datetime(2018, 5, 15), datetime(2019, 3, 22), datetime(2017, 11, 5)]


def ajustar_data(data):
    return datetime(data.year, data.month, 1)


datas_antigas = filter(lambda data: data.year < 2019, datas)


datas_ajustadas = map(ajustar_data, datas_antigas)


datas_ajustadas = list(datas_ajustadas)


for data_antiga, data_ajustada in zip(datas_antigas, datas_ajustadas):
    index = datas.index(data_antiga)
    datas[index] = data_ajustada


for data in datas:
    print(data.strftime("%Y-%m-%d"))
