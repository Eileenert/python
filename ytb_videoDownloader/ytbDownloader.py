import os
from pytube import YouTube
os.chdir(f"{os.path.dirname(__file__)}/ytb_download")


# informations about the video
def info_video():

    link = input("Enter the link: ")
    yt = YouTube(link)
    subtitle = yt.captions.all()

    # Title of the video
    print(f"Title: {yt.title}")

    # number of views of the video
    print(f"Number of views: {yt.views}")

    # length of the video
    print(f"Length of the video: {yt.length} seconds")

    # Description of video
    print(f"Description: {yt.description}")

    # rating
    print(f"Ratings: {yt.rating}")

    # Subtitle
    print(f"Subtitle available: \n {subtitle}")

    return subtitle, yt


# Download the video
def download_video(yt):
    # get the best resolutiom
    ys = yt.streams.get_highest_resolution()

    # Starting download
    print("Downloading...")
    try:
        ys.download()
    except:
        print("We can't downlad this video")
    else:
        print("Download completed!")


# download the subtitles
def download_subtitles(subtitle):
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
                            print(f"Press {i} for this subtitle: {sub}")
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
                        subtitle_text = subtitle[language].generate_srt_captions(
                        )
                        with open(f"subtitle{language}.srt", "wt") as file:
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
    download_subtitles(sub_yt[0])
    restart()


main()
