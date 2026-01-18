import math

def schedule_videos(videos, time_available):
    days = []  # List of lists: each day is [(video_num, minutes, is_whole)]
    current_day = -1  # No day yet
    
    for video_num, video_length in enumerate(videos, start=1):
        if video_length <= time_available:
            # Small video: try to add whole
            if current_day < 0 or get_remaining(days[current_day], time_available) < video_length:
                days.append([])
                current_day += 1
            # Add whole
            days[current_day].append((video_num, video_length, True))
        else:
            # Large video: split into equal-ish parts
            num_parts = math.ceil(video_length / time_available)
            base = video_length // num_parts
            extra = video_length % num_parts
            parts = [base + 1 if i < extra else base for i in range(num_parts)]
            
            for part_size in parts:
                if current_day < 0 or get_remaining(days[current_day], time_available) < part_size:
                    days.append([])
                    current_day += 1
                # Add part
                days[current_day].append((video_num, part_size, False))  # False means partial
    
    # Now output
    print("Here is the time schedule!")
    for day_num, day in enumerate(days, start=1):
        print(f"day {day_num}:", end=" ")
        items = []
        for video_num, minutes, is_whole in day:
            if is_whole:
                items.append(f"watch video {video_num} ({minutes} minutes)")
            else:
                items.append(f"watch video {video_num} ({minutes} minutes, out of {video_length} minutes)")
        print(" and ".join(items[:-1]) + (" and " if len(items) > 1 else "") + items[-1] if len(items) > 1 else items[0])

def get_remaining(day, time_available):
    return time_available - sum(minutes for _, minutes, _ in day)

# Example usage
videos = [50, 204, 30, 720]
time_available = 60
schedule_videos(videos, time_available)