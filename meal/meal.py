def main():
    # get time from user
    answer = input("What time is it? ").strip()
    time = convert(answer)

    # check meal times
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    # split hours and minutes and convert to float
    hours, minutes = time.split(":")
    new_minute = float(minutes) / 60
    return float(hours) + new_minute


if __name__ == "__main__":
    main()