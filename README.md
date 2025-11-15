## SigPy
### Site Generator Python


### One time setup
```
1. Go to this
    https://github.com/tactlabs/sigpy

2. Use this template and create a new repository

3. run this
    pip install -r requirements.txt

4. Start adding new notebooks under `notebooks` folder
```

### Change Settings
```
go to pelicanconf.py

change the necessary changes to update:
    AUTHOR
    SITENAME
    GITHUB_USERNAME
    LINKS
    SOCIAL
```

### Verify Local
```
python make.py

PELICAN_ENV=local pelican content

pelican --listen
    this will run the local server
    http://127.0.0.1:8000
```

### Publish (first time)
```
python make.py

pelican content

git add .

git commit -m "<change details>"

git push

go to GitHub Repository (pynotes) settings -> Pages -> Source

select "Deploy from  branch"

Go to branch on the same page

select "main" branch and "docs" folder
```

### Publish (second time onwards)
```
python make.py

pelican content

git add .

git commit -m "<change details>"

git push
```

![1731731240445](image/README/1731731240445.png)

### Screenshots
![1731731318195](image/README/1731731318195.png)


![1731731351975](image/README/1731731351975.png)


![1731731363325](image/README/1731731363325.png)