import os
import time

# BOILER PLATE sort of kickstart later for a function.
songs_folder_path = r"D:\mukul\Vision\Lyrics_Fav_Songs_Code\Fav_Songs"
print("\nScanning for Songs")
print("-" * 20)

# Data Structure < list > to hold the songs
available_songs = []
lyrics_timeline = []

# To list the songs from the folder
for song_files in os.listdir(songs_folder_path):
    if song_files.endswith(".mp3"):
        available_songs.append(song_files)
        ## We do even want to list the songs with their serial numbers.
        print(f"\n{len(available_songs)} => {song_files}\n")
        print("-" * 20)
        print("\n")


# Variables to hold the path values.\
## LYRICS PATH
lrc_file = "tere liye.lrc"
full_lrc_path = os.path.join(songs_folder_path, lrc_file)

## SONG PATH
song_name = available_songs[0]
full_song_path = os.path.join(songs_folder_path, song_name)

# MAIN FRAME LOGIC
with open(full_lrc_path, "r", encoding="utf-8") as song_lrc_file:
    lines = song_lrc_file.readlines()

print("...........SONG DETAILS...........")
for line in lines:
    if line.startswith("[00:") or line.startswith("[01:") or line.startswith("[02:"):

        # Good practice to strip() the lines endings.
        clean_line = line.strip()
        # Split the line into chunks of time block [0] and actual words [1].
        line_chunks = clean_line.split("]")

        ## Working onto the time_chunk to remove these brackets [ ].
        ## Here, ending ] has been removed by split function already.
        ##       starting [ will be replaced now by nothing.
        time_chunk = line_chunks[0].replace("[", "")
        lyrics_chunk = line_chunks[1]

        # print(f"TIME: {time_chunk}\tLYRICS: {lyrics_chunk}")

        # Convert the Minutes of time chunks into seconds of float data type.
        # 00:00:00 == Minutes : Seconds : MileSeconds
        # MAKE SURE TO CONVERT IT TO FLOAT or else YOU WILL BE BEWILDERED 😂
        time_chunk_parts = time_chunk.split(":")
        minutes = float(time_chunk_parts[0])
        seconds = float(time_chunk_parts[1])
        total_seconds = (minutes * 60) + seconds

        # Store into lyrics_timeline as a tuple DS these total_seconds separated chunks.
        lyrics_timeline.append((total_seconds, lyrics_chunk))

# To launch the Audio on terminal screen
os.system("cls") ## Will clear the terminal screen before we start.
print(f"PLAYING : {available_songs[0]}")
os.startfile(full_song_path)

# Variable to help in syncing the timestamp correctly
# delayed_offset = 2.5

# Starting the stopwatch
dis_start_time = time.time()

# SYNCHRONISED DISPLAY || SYNCHRONISATION
for target_timeStamp, target_lyrics in lyrics_timeline:

    ## Starting the stopwatch then matching it to target time from where it should start displaying the lyrics.

    elapsed_time = (time.time() - dis_start_time)

    ## now actually SYNCING them.
    while elapsed_time < target_timeStamp:

        ### As long as elapsed_time is less than 1st timestamp, the script just waits and checks the clock again.
        ### And once the time_stamp is hit, it starts doing the same for the next time_stamp
        time.sleep(3) # sleeps for 3 seconds
        elapsed_time = (time.time() - dis_start_time)  # check again.

    ## Once the target_timeStamp is hit, we release our lyrics on display.
    os.system("cls")
    print(f"\n{target_lyrics}\n")
