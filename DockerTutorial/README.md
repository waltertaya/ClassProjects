# GETTING STARTED WITH DO

- `docker pull image_name` command fetches the image from the Docker registry and save it to the our system.
- `docker images` command to see a list of Docker images on our system.
- **Running a container** using `docker run container_name` command
- `docker ps` command to show all containers that are currently running
- `docker ps -a` command
- `docker run -it container_name sh` command. Running the `run` command with the `-it` flags attaches us to an interactive tty in the container. Now we can run as many commands in the container as we want. Take some time to run your favorite commands.

    `Danger Zone: If you're feeling particularly adventurous you can try rm -rf bin in the container. Make sure you run this command in the container and not in your laptop/desktop. Doing this will make any other commands like ls, uptime not work. Once everything stops working, you can exit the container (type exit and press Enter) and then start it up again with the docker run -it busybox sh command. Since Docker creates a new container every time, everything should start working again.`

- To find out more about run, use docker `run --help` to see a list of all flags it supports.
- We saw above that we can still see remnants of the container even after we've exited by running `docker ps -a`.
- Running `docker run` command multiple times will result in leaving stray containers will eat up disk space. Hence, as a rule of thumb, I clean up containers once I'm done with them. To do that, you can run the `docker rm` command. Just copy the container IDs from above and paste them alongside the command.
- On deletion, you should see the IDs echoed back to you. If you have a bunch of containers to delete in one go, copy-pasting IDs can be tedious. In that case, you can simply run -

```Bash
docker rm $(docker ps -a -q -f status=exited)
```

- This command deletes all containers that have a status of exited. In case you're wondering, the `-q` flag, only returns the numeric IDs and `-f` filters output based on conditions provided. One last thing that'll be useful is the `--rm` flag that can be passed to docker run which automatically deletes the container once it's exited from. For one off docker runs, `--rm` flag is very useful.

- In later versions of Docker, the docker container prune command can be used to achieve the same effect.

```Bash
$ docker container prune
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
4a7f7eebae0f63178aff7eb0aa39f0627a203ab2df258c1a00b456cf20063
f98f9c2aa1eaf727e4ec9c0283bcaa4762fbdba7f26191f26c97f64090360

Total reclaimed space: 212 B
```

- Lastly, you can also delete images that you no longer need by running docker rmi.

## Terminologies

1. Images - The blueprints of our application which form the basis of containers. In the demo above, we used the docker pull command to download the busybox image.
2. Containers - Created from Docker images and run the actual application. We create a container using docker run which we did using the busybox image that we downloaded. A list of running containers can be seen using the docker ps command.
3. Docker Daemon - The background service running on the host that manages building, running and distributing Docker containers. The daemon is the process that runs in the operating system which clients talk to.
4. Docker Client - The command line tool that allows the user to interact with the daemon. More generally, there can be other forms of clients too - such as Kitematic which provide a GUI to the users.
5. Docker Hub - A registry of Docker images. You can think of the registry as a directory of all available Docker images. If required, one can host their own Docker registries and can use them for pulling images.
