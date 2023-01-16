# Create app celery to start satellite_downloader
from celery import Celery
from celery.signals import worker_ready
from celeryapp import delay_controller as delay

app = Celery('beat_downloader')

app.config_from_object('satellite.celeryapp.downloader.config')





# -----------------
# Celery Beat

app.conf.beat_schedule = {
    'download-brasil-copernicus-netcdf': {
        'task': 'extract_br_netcdf_monthly',
        'schedule': delay.get_task_delay('extract_br_netcdf_monthly'),
    }
}


# Send signal to run at worker startup
@worker_ready.connect
def at_start(sender, **kwargs):
    """Run tasks at startup"""
    with sender.app.connection() as conn:
        sender.app.send_task('initialize_satellite_download_db', connection=conn)