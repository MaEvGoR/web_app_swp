# web_app_swp
Feedback web application for Innopolis University


## What you should do to run the code
### First 
You need to install [Docker](https://www.docker.com/)

### Second
Clone this project on your computer

### Third 
With terminal go to directory web_app_swp

### Fourth
In terminal run
```bash
docker-compose up --build
```
This command create image for this project and starts the site on [http://localhost/](http://localhost/)

If you want to rerun a container in the background, just run
```bash
docker-compose up -d <container-name>
```

If you want to rebuild and rerun the container
```bash
docker-compose up -d --build <container-name>
```

Possible options for `<container-name>` are:
  - backend
  - frontend
  - nginx

## Support
Write to @ma_evgor if you have any problems with installation
