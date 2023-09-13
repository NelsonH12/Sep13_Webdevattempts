from website import create_app #the website folder has to be a .py file or else this doesn't work

app = create_app()

if __name__ == '__main__':  #only if you run THIS file, will the server be initiated
  app.run(debug=True) #this allows the site to update as changes are made.