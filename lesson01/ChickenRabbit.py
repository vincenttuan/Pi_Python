def calc(sum, foots):
    checken = rabbit = 0
    rabbit = (foots - sum * 2) / 2;
    checken = sum - rabbit
    return int(checken), int(rabbit)

checken, rabbit = calc(83, 240)
print(checken, rabbit)
