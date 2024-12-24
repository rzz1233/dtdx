from django.apps import AppConfig
from meeting.settings import ENABLE_SCHEDULED_TASKS
class MeetConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "meet"

    def ready(self):
        # 导入并启动定时任务
        from meet.scheduler import start
        if ENABLE_SCHEDULED_TASKS:
            start()

    # def stop_scheduler(sender, **kwargs):
    #     from meet.scheduler import stop_scheduler
    #     stop_scheduler()
    #
    # connection_created.connect(stop_scheduler)
