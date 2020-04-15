# Academic Staff Assessment
Feedback web application for Innopolis University 

## What you should do to run the application locally
1. You need to install [Docker](https://www.docker.com/)
2. Clone this project on your computer
3. With terminal go to directory web_app_swp
4. In terminal run
```bash
docker-compose up --build
```
This command create image for this project and starts the application on [http://localhost/](http://localhost/)

### Usefull commands
P.s. If you want to rerun a container in the background, just run
```bash
docker-compose up -d <container-name>
```
P.s.2. If you want to rebuild and rerun the container
```bash
docker-compose up -d --build <container-name>
```

Possible options for `<container-name>` are:
  - backend
  - frontend
  - nginx

## Support
Write to @ma_evgor via Telegram if you have any problems with installation
