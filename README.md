# RPA-tunkki for adding Youtube-videos to SyncTube-service

## How to use
Build docker image and make sure it matches with the add_songs.sh shell script command. 

To run the RPA-tunkki

`./add_songs.sh <SyncTube Room id> <YouTube playlist url>`

The Docker container runs Python script which uses Selenium to add videos from the provided Youtube playlist to the SyncTube room.