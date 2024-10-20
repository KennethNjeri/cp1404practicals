
FILENAME = "wimbledon.csv"

def main():
    records = get_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)

def get_records(filename):
    records= []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
        return records


def process_records(records):
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[0])
        if record[1]  in champion_to_count:
            champion_to_count[record[1]] += 1
        else:
            champion_to_count[record[1]] = 1
    return champion_to_count, countries

def display_results(champion_to_count, countries):
    print("wimbledon Champions: ")
    for name, count in champion_to_count.items():
        print(f"{name}: {count}")
    print(f"\nThese  {len(countries)} countries have won the wimbledon: ")
    print(", ".join(country for country in sorted(countries)))
