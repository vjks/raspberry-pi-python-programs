from pyspark import SparkContext
from sys import stdin

if __name__ == "__main__":
    sc = SparkContext("local[*]", "wordcount")
    sc.setLogLevel("ERROR")  # INFO, ERROR, WARN
    input = sc.textFile("/Users/vj_ku/OneDrive/myCourses/BigData-TrendyTech/Week9/Sample.txt")
    words = input.flatMap(lambda x: x.split(" "))
    word_count = words.map(lambda x: (x, 1))
    final_count = word_count.reduceByKey(lambda x, y: x + y)
    result = final_count.collect()
    result.sort(key=lambda x: x[1], reverse=True)
    print("type is: ", type(result))
    for a in result:
        if a[1] > 1 and len(a[0]) > 3:
            print(a)

    # stdin.readline()
