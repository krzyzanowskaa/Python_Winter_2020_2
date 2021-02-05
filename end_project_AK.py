# Top and worst hours for asking on Hacker News

def top_and_worst_hours_for_posting(file):
    file_name = file + '.csv'
    from csv import reader
    with open(file_name, encoding='utf8') as read_obj:
        csv_reader = reader(read_obj)
        hn = list(csv_reader)

    headers = []
    headers = hn[0]

    hn = hn[1:]

    ask_posts = []
    show_posts = []
    other_posts = []

    for row in hn:
        title = row[1]
        if title.lower().startswith('ask hn'):
            ask_posts.append(row)
        elif title.lower().startswith('show hn'):
            show_posts.append(row)
        else:
            other_posts.append(row)

    all_ask_posts = len(ask_posts)
    all_show_posts = len(show_posts)
    all_other_posts = len(other_posts)

    total_ask_comments = 0
    for row in ask_posts:
        num = int(row[4])
        total_ask_comments = total_ask_comments + num

    avg_ask_comments = total_ask_comments / all_ask_posts

    total_show_comments = 0
    for row in show_posts:
        num = int(row[4])
        total_show_comments = total_show_comments + num

    avg_show_comments = total_show_comments / all_show_posts

    import datetime as dt

    result_list = []

    for row in ask_posts:
        cr_time = row[6]
        comment = int(row[4])
        second_list = [cr_time, comment]
        result_list.append(second_list)

    counts_by_hour = {}
    comments_by_hour = {}

    for row in result_list:
        date_and_time = row[0]
        comment = row[1]
        str_format = "%m/%d/%Y %H:%M"
        dt_object = dt.datetime.strptime(date_and_time, str_format)
        hour = dt_object.strftime("%H")

        if hour not in counts_by_hour:
            counts_by_hour[hour] = 1
            comments_by_hour[hour] = comment
        else:
            counts_by_hour[hour] += 1
            comments_by_hour[hour] += comment

    avg_by_hour = []

    for hr in comments_by_hour:
        avg_by_hour.append([hr, comments_by_hour[hr] / counts_by_hour[hr]])
    avg_by_hour

    swap_avg_by_hour = []

    for row in avg_by_hour:
        swap_avg_by_hour.append([row[1], row[0]])

    sorted_swap = sorted(swap_avg_by_hour, reverse=True)
    sorted_swap1 = sorted(swap_avg_by_hour, reverse=False)

    print("Top 5 Hours for 'Ask HN' Comments")
    for avg, hour in sorted_swap[:5]:
        print(
            "{}: {:.2f} average comments per post".format(dt.datetime.strptime(hour, "%H").strftime("%H:%M"), avg))

    print("")

    print("Worst 5 Hours for 'Ask HN' Comments")
    for avg, hour in sorted_swap1[:5]:
        print("{}: {:.2f} average comments per post".format(dt.datetime.strptime(hour, "%H").strftime("%H:%M"), avg))

    return

top_and_worst_hours_for_posting('HackerNews')