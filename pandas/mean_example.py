import pandas

visitors = [2343, 2323, 4442, 34343, 23232]
errors = [23, 23,43,41, 64]
df = pandas.DataFrame({"visitors": visitors, "errors": errors}, index=["Mon", "Tues", "Wed", "Thu", "Fri"])
print(df)
print(df["errors"].mean())
