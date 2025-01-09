from concurrent.futures import ThreadPoolExecutor, as_completed


def refresh_mv(view):
    sql_st = f"REFRESH MATERIALISED VIEW schema.{view}"
    #execute query and return the statement id
    return sql_st

mv = "mv1,mv2,mv3"
mv = mv.split(",")

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(refresh_mv, i) for i in mv]
    result = []
    for future in as_completed(futures):
        res = future.result()
        result.append(res)

print(result)
