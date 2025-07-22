from django.http import JsonResponse
from clickhouse_driver import Client
from django.shortcuts import render
client = Client(host='127.0.0.1')


def show_date_table(request):
    query = "SELECT * FROM date LIMIT 100"
    result = client.execute(query)

    # ตั้งชื่อ column ตาม schema ใน ClickHouse
    columns = [
        "D_DATEKEY", "D_DATE", "D_YEAR", "D_DAYOFWEEK", "D_MONTH",
        "D_YEAR2", "D_YEARMONTHNUM", "D_YEARMONTH", "D_DAYNUMINWEEK",
        "D_DAYNUMINMONTH", "D_DAYNUMINYEAR", "D_MONTHNUMINYEAR",
        "D_WEEKNUMINYEAR", "D_SEASON", "D_HOLIDAY", "D_WEEKDAY",
        "D_WORKDAY", "D_SCHOOLDAY"
    ]

    rows = result

    return render(request, 'show_date.html', {'rows': rows, 'columns': columns})