# Cloudlab Simple profile template

[Cloudlab](https://www.cloudlab.us) profile script to run a couple of standalone machines prepared to run docker on top.
This serves more like a quick profile initializer than an ultimate script for a specific use case.


The profile descriptor takes care of installing all necessary packages to the system, including docker.
Once your machines are up, the install script does the thing. 

Wait until the install is done:
```
Installation finished
$PATH=/usr/local/etc/emulab:/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:/usr/site/bin:/usr/site/sbin!
```

If you see this with red background:
```
Installing is still in progess...!
tail -f /tmp/install.log
```
you still have to wait, but you can keep track of the status using the command shown.




