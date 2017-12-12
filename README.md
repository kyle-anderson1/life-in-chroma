# AlbumMaker
By: Kyle Anderson

# Website link
https://life-in-chroma.appspot.com/

# Details on how to deploy application
1. Other access point for files is: Clone my github repository to get the files at:
  git@github.com:kyle-anderson1/life-in-chroma.git
2. Once files have been cloned or the zip file unzipped, go into the unzippped directory
3. There are some important dependencies to run the project locally: the Google SDK must be set up, python2.7 must be installed and the following additional requirements are needed for local deployment...
  a. Pillow version 1.1.7
  b. WebApp2 version 2.5.2
  c. Jinja2 version 2.6
  d. WebOb (latest version)
4. To run locally simply run "dev_appserver.py ." and go to "localhost:8080"
5. These are the instructions to deploy to google:
6. Run "gcloud config set project <project-id>" where <project-id> is the name of the project created on your google cloud account.
7. Run "gcloud app deploy app.yaml"
8. Make sure to select "US-central region" when prompted
9. Run "gcloud app browse" and voila
