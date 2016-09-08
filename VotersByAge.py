from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("Voters by Age")
sc = SparkContext(conf = conf)

# Take in a raw line, and return parsed info (only the stuff we care about)
# For initial parsing + organization
def parseLines(line):
    fields = line.split(',')
    age = fields[1]
    voted = fields[2]
    return (age, voted)

# Take in (Age, Voted), return (Age, 1)
# For Aggregation by key
def justAge(line):
    age = line[0]
    return (age, 1)

lines = sc.textFile("file:///SparkCourse/voters.csv")
raw1 = lines.collect() 

print("\n\nWe have a set of data that is\
      \nName  ,  Age  ,  Voted(bool)\
      \nand we and to see # of voters for each age")

print("\nHere's our raw data...\n")
for item in raw1:
    print(item)
    
print("\nLet's get rid of the names...\
       \nAnd put them as tuples\n")
noName = lines.map(parseLines)
raw2 = noName.collect()

for item in raw2:
    cleanAge = item[0].encode('ascii', 'ignore')
    cleanVote = item[1].encode('ascii', 'ignore')
    
    if (cleanAge and cleanVote):
        print(cleanAge, cleanVote)

print("\nNow lets just get rid of the 'no' columns and map as (age, 1)")
print("This way, we can just add up each row by Key\n")

noNo = noName.filter(lambda x: "yes" in x[1])
justAge = noNo.map(justAge)
raw3 = justAge.collect()

for item in raw3:
    print (item[0].encode('ascii','ignore'), item[1])
    
print("\nNow lets see how much each age group has voted...\n")
final = justAge.reduceByKey(lambda x,y: x + y).map(lambda (x,y): (y,x)).sortByKey()
raw4 = final.collect()

for item in raw4:
    print (item[1].encode('ascii','ignore'), item[0])
    
print("\nNow with this data we can see...\n")
print("1. That 34 people didn't vote!")
print("2. Amongst the people that DID vote, 26yr olds seem to be the most active\n")
print("Very informative!\n  ")
