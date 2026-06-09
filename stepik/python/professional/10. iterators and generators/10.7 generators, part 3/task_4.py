import csv


def get_round_sum(filename, rnd):
    with open(filename, encoding='u8') as i_file:
        rnd_gen = (row for row in csv.DictReader(i_file) if row['round'].lower() == rnd)
        amount_gen = (int(row['raisedAmt']) for row in rnd_gen)
        return sum(amount_gen)


filename = 'data.csv'
rnd = 'a'
print(get_round_sum(filename, rnd))

# alt
with open('data.csv', encoding='utf-8') as file:
    data_rows = (line.strip().split(',') for line in file)
    total_a_round = sum(int(amt) for _, amt, rnd in data_rows if rnd == 'a')
    print(total_a_round)
