# RPA-tunkki for adding YouTube-videos to SyncTube-service

## How to use
Build docker image and make sure it matches with the add_songs.sh shell script command. 

`docker build -t <image name:tag> .`

1. Prepare for the long awaited SyncTube session by adding the most diamond like YouTube videos to a public or unlisted playlist. Write on paper the playlist url.
2. Create or join a room on SyncTube (https://sync-tube.de/) with your friends. Write on paper the SyncTube room id.
3. Run the RPA-tunkki with the following command.

`./add_songs.sh <SyncTube room id> <YouTube playlist url>`

That shell script spins up a Docker container which executes a Python script which uses Selenium to add videos from the provided Youtube playlist to the SyncTube room for the joy of your friends.

4. Enjoy the lovely dark side of YouTube with your friends.

#roboticprocessautomation