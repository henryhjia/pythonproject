# pythonproject
Python project
1. In GitHub create a fine-grained personal access token
   setting->developer setting->...
2. In GitHub, create a repository, e.g. pythonproject
3. In Ubuntu top directory e.g. ~/Projects/ clone the Git Repository:

Cloning into 'pythonproject'...
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (4/4), done.

4. Copy all files from another directory:
e.g.
cp -r ../pythonreview/* .

5. git add .
6. git commit -m 'initial commit'

7. git push origin main

Enumerating objects: 79, done.
Counting objects: 100% (79/79), done.
Delta compression using up to 4 threads
Compressing objects: 100% (73/73), done.
Writing objects: 100% (78/78), 78.16 KiB | 5.58 MiB/s, done.
Total 78 (delta 4), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (4/4), done.
To https://github.com/henryhjia/pythonproject.git
   43c07ca..c19e973  main -> main



