#!/usr/bin/env python3
import os

# Set environment variables
homedir = os.getenv("HOME") + '/'
repodir = os.getenv("HOME") + '/dot_lin/'
links = os.listdir(repodir)
ignore = ['.git', 'README.md', 'setup.py', 'setup']
windowsdirs = ['']

# Remove standard config files
if os.path.exists('/etc/skel'):
    basicdotfiles = os.listdir('/etc/skel')
    for basicdotfile in basicdotfiles:
        cmdstring = "rm -rf %s%s" % (homedir, basicdotfile)
        os.system(cmdstring)


# Create Directories
if not os.path.exists(homedir + 'gitrepos'):
    cmdstring = "mkdir %s/gitrepos" % homedir
    os.system(cmdstring)
    cmdstring = "ln -s %s %s" % (repodir, homedir + 'gitrepos/dot_lin')
    os.system(cmdstring)

def linkfolder(windowspath, linkname):
    linkpath = homedir + linkname
    if not os.path.exists(linkpath):
        cmdstring = "ln -s %s %s" % ('/cygdrive/c/Users/' + os.getenv("USER")
                + windowspath, linkpath)
        os.system(cmdstring)

if os.path.exists('/cygdrive'):
    linkfolder('/Dropbox', 'dropbox')
    linkfolder('/OneDrive', 'onedrive')
    linkfolder('/Downloads', 'downloads')
    linkfolder('/Dropbox/Computers/Projects', 'projects')


# Simlink dotfiles
for link in links:
    if link not in ignore and not os.path.exists(homedir + '.' + link):
        print("\033[1;32;40m>>> \033[1;37;40mLinking: %s\033[0;37;40m" % link)
        cmdstring = "ln -s %s%s %s.%s" % (repodir, link, homedir, link)
        os.system(cmdstring)


# Download git plugins
def gitsync(gitrepo, gitname):
    if not os.listdir(repodir + 'vim/bundle/' + gitname):
        print("Syncing %s" % gitname)
        cmdstring = "git -C %svim/bundle/ clone %s" % (repodir, gitrepo)
        os.system(cmdstring)
    return;

gitsync('https://github.com/jiangmiao/auto-pairs', 'auto-pairs')
gitsync('https://github.com/ajh17/VimCompletesMe', 'VimCompletesMe')
gitsync('https://github.com/PProvost/vim-ps1', 'vim-ps1')
gitsync('https://github.com/scrooloose/nerdtree', 'nerdtree')
gitsync('https://github.com/Xuyuanp/nerdtree-git-plugin', 'nerdtree-git-plugin')