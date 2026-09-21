apple = ("macbook pro", "macbook air", "mac mini", "imac", "mac studio")

windows = ("hp spectre", "dell xps", "lenovo thinkpad", "asus zenbook", "microsoft surface")

all_pc = apple + windows

if "dell xps" in windows and "dell xps" in all_pc:
    print("Dell XPS is available in both windows and all_pc tuples")
else:
    print("Not available")
