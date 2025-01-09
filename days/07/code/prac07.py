# a = "exusiaa-india"

# count = 0
# for i in a:
#     if count < a.count(i):
#         count = a.count(i)

# print(count)

# l1 = [i for i in set(a) if a.count(i) == count]
# print(*sorted(l1), sep=", ")

import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

def refresh_mv(view_name):
    print(datetime.datetime.now())
    print(view_name)
    sql_st = f"REFRESH MATERIALIZED VIEW schema.{view_name}"
    return sql_st

mv = "mv1,mv2,m3"

mv = mv.split(',')
print(mv)

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(refresh_mv, view) for view in mv]
    statements = []

    for future in as_completed(futures):
        statement = future.result()
        statements.append(statement)

print(statements)