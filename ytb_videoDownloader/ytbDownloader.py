import os
from pytube import YouTube
os.chdir(f"{os.path.dirname(__file__)}/ytb_download")


# information about the video
def info_video():

    link = input("Enter the link: ")
    yt = YouTube(link)
    subtitle = yt.captions.all()

    # Title of the video
    print(f"\nTitle: {yt.title}", flush=True)

    # number of views of the video
    print(f"\nNumber of views: {yt.views}", flush=True)

    # length of the video
    print(f"\nLength of the video: {yt.length} seconds", flush=True)

    # Description of video
    print(f"\nDescription: \n{yt.description}", flush=True)

    # rating
    print(f"\nRatings: {yt.rating}", flush=True)

    # Subtitle
    print(f"\nSubtitle available:\n{subtitle}", flush=True)

    return subtitle, yt


# Download the video
def download_video(yt):
    # get the best resolution
    ys = yt.streams.get_highest_resolution()

    # Starting download
    print("Downloading...")
    try:
        ys.download()
    except:
        print("\nWe can't downlad this video")
    else:
        print(f"\n{yt.title} Download completed!")


# download the subtitles
def download_subtitles(subtitle,yt):
    if subtitle != []:
        while True:
            # ask to download or not the subtitles
            subtitle_dwl = input(
                "Do you want to download the subtitles? y/n: ")

            # we do not download the subtitles
            if subtitle_dwl.lower() == "n":

                # Be sure before qui
                sure = input("Are you sure? y/n: ")
                if sure.lower() == "n":
                    pass

                # quit
                else:
                    print("\nBye")
                    break

            # we download the subtitles
            elif subtitle_dwl.lower() == "y":
                while True:
                    while True:
                        i = 0
                        # list of subtitles with a number for each one
                        for sub in subtitle:
                            print(f"\nPress {i} for this subtitle: {sub}")
                            i += 1

                        # choose the subtitles
                        language = input("Press the number: ")
                        try:  # verify that it's a correct number
                            language = int(language)

                            if language > len(subtitle):
                                print("please enter a correct number")

                            else:
                                break
                        except:
                            print("Please enter a number")

                    try:
                        # generate subtitle's text
                        subtitle_text = subtitle[language].generate_srt_captions()
                        with open(f"{yt.title}subtitle{language}.srt", "wt") as file:
                            # write subtitle's text
                            file.write(f"{subtitle_text}")

                        print("Download completed!")
                        # quit
                        break

                    except:
                        print("Impossible to download this subtitle")
                        os.remove(f"subtitle{language}.srt")

                        retry = input("try other subtitles? y/n: ")

                        if retry.lower() == "y":
                            pass

                        elif retry.lower() == "n":
                            break

                        else:
                            break

                break

            else:
                print("Please enter 'y' or 'n'")


# Ask if we want to download another video or not
def restart():
    again = input("Do you want to download another video? y/n: ")

    if again.lower() == "n":
        print("bye")
    elif again.lower() == "y":
        main()
    else:
        print("bye")


def main():
    sub_yt = info_video()
    download_video(sub_yt[1])
    download_subtitles(sub_yt[0],sub_yt[1])
    restart()

if __name__ == '__main__':
    main()
