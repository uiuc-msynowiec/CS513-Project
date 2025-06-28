# CS513-Project


## Enabling lfs

From the commandline:

git lfs install


## Adding files with lfs support
The following have already been performed for this repo.

Once lfs is enabled, track the filetypes that will be large:

git lfs track "*.db"
git lfs track "*.csv"

Add .gitattributes to the repo:
git add .gitattributes

Then commit and push the changes.