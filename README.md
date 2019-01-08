# Clean cloud service for motioneye

To delete old media files on Google Drive that were uploaded by [`motioneye`](https://github.com/ccrisan/motioneye), download `cleancloud` folder and copy it to your pi somewhere, for example to `/home/pi`. Then add a cron job as follows:

```
sudo crontab -e

0 0 * * * python /home/pi/cleancloud/cleancloud.py
```
Some assumptions are:

* upload service is working ok
* file persistence is working ok
* camera id is `1`
* service name is `gdrive`

Following functions are added in `uploadservices.py`
* clean_cloud()
* exist_in_local()
* get_local_folders()
* GoogleDrive.clean_cloud()
* GoogleDrive._get_children()
* GoogleDrive._delete_child()
* GoogleDrive._get_file_metadata()
* GoogleDrive._get_file_title()

Also `_request()` function was modified to accept a new optional parameter `method` to override the default GET.

Periodically codes here will compare media folders in local and cloud and will delete a cloud folder that does not exist in local as it must be an old folder that was deleted by `motioneye` as configured by users' file persistence setting.