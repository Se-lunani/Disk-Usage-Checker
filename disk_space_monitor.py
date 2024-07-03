import psutil # type: ignore

def check_disk_usage(path):
    """check the disk usage of the given path."""
    usage = psutil.disk_usage(path)
    total_space = usage.total
    free_space = usage.free
    used_space = usage.used

    return total_space, used_space, free_space

def main ():
    path = "/"
    total, used, free = check_disk_usage(path)
    print(f"Disk Usage for {path}:")
    print(f"Total Space: {total / (1024 ** 3):.2f} GB")
    print(f"Used Space: {used / (1024 ** 3):.2f} GB")
    print(f"Free Space: {free / (1024 ** 3):.2f} GB")

if __name__ == "__main__":
    main()
