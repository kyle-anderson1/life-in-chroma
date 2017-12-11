# AlbumMaker
By: Kyle Anderson

# Details on how to deploy application
1. Clone my github repository to get the files at:
  git@github.com:kyle-anderson1/life-in-chroma.git
  ^This is a secondary source of all my files
2. Google App Engine has all the necessary requirements when it is deployed by: gcloud app deploy
3. To deploy it locally there are some necessary requirements:
pillow version 1.1.7, webapp2 version 2.5.2, jinja2 version 2.6, and webob (latest version).
4. For local deployment: make sure the Google Cloud SDK is setup (this should be setup for any user that has set up an app engine project before) and then run dev_appserver.py app.yaml in the directory. This will open up a local deployment in localhost:8080.
