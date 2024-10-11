def polar_datasets():
    import math
    datasety = float(input('enter y variable:'))
    datasetx = float(input('enter x variable:'))
    datasetd = float(input('enter distance:'))
    datasetdir = float(input('enter direction:'))
    y = datasety + datasetd * math.sin(datasetdir)
    x = datasetx + datasetd * math.cos(datasetdir)
    print(y)
    print(x)
polar_datasets()