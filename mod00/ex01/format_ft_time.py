from datetime import datetime

def format_ft_time(ft_time):
    seconds_pass = (ft_time - datetime(1970, 1, 1)).total_seconds()
    scientific_notation = f"{seconds_pass:.2e}"
    result_str = f"Seconds since January 1, 1970: {seconds_pass} or {scientific_notation} in scientific notation"

    print(result_str)
    print(ft_time.strftime("%b %d %Y"))

    return



ft_time = datetime.now()
format_ft_time(ft_time)
print()
ft_time = datetime(2022,10, 21)
format_ft_time(ft_time)


