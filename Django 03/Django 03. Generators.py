# generators
import datetime


# numbers = [i for i in range(10)]
# numbers1 = (i for i in range(10))
#
# print(numbers)
# print(next(numbers1))
# print(next(numbers1))
# print(next(numbers1))
# print(next(numbers1))
# print(next(numbers1))
# print(next(numbers1))
# print(next(numbers1))
# print(next(numbers1))
# print(next(numbers1))
# print(next(numbers1))


def infinite_days(start=None):
    if start is None:
        start = datetime.date.today()
    while True:
        yield start
        start+= datetime.timedelta(days=1)

# days = infinite_days()
#
# print(next(days))
# print(next(days))
# print(next(days))

def read_file_lines(path:str):
    with open(path) as f:
        for line in f:
            yield line.strip()

# for line in read_file_lines("students.txt"):
#     input()
#     print(line)


def generate_events():
    events = [
        {"level": "INFO", "event":"user_login", "user_id":1},
        {"level": "ERROR", "event":"db_unavailable", "retry_in":5},
        {"level": "INFO", "event":"user_logout", "user_id":1},
        {"level": "WARNING", "event":"slow_request", "duration_ms":1200},
    ]
    for event in events:
        yield event


def filter_errors(events, level:str):
    for event in events:
        if event["level"] == level:
            yield event


def enrich_events(events, source):
    for event in events:
        enriched = dict(event)
        enriched["source"] = source
        yield enriched


def demo_pipline(level, target_source):
    print("Generators Pipline")
    source = generate_events()
    errors_only = filter_errors(source, level)
    enriched = enrich_events(errors_only, target_source)
    for event in enriched:
        print(f"event -> {event}")

demo_pipline("ERROR", "app_server_1")


"""
Generatorların əsas konsepsiyası:
    1. Lazy
    2. Yaddaşa qənaət
    3. Generator state
    4. Birdəfəlik
    

"""