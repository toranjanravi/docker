Overview: I have containerised a simple flask application to greet. Its my first one and will now start making bigger ones :)

Instructions: 

Download image using : docker pull docker push toranjanravi/docker:howareyou
Check downloaded using : docker images
Run the image using : docker run -d -p 5000:5000 -t <image ID>

It can be browsed on http://hostip:5000/<yourname>

List running containers: docker ps

To stop it run docker stop <container id>

Docker hub link: https://cloud.docker.com/repository/docker/toranjanravi/docker
Github link with dockerfile: https://github.com/toranjanravi/docker/tree/master/flaskapp
