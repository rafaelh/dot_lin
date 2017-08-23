#!/usr/bin/env python3






echo ">>> Backing up Photos"
rsync -avz --delete -e 'ssh -p 9012' root@192.168.0.15:/raid/Photos /mnt/g/

echo ">>> Backing up Documents"
rsync -avz --delete -e 'ssh -p 9012' root@192.168.0.15:/raid/Documents /mnt/e/

echo ">>> Backing up Movies"
rsync -avz --delete -e 'ssh -p 9012' root@192.168.0.15:/raid/Movies /mnt/f/