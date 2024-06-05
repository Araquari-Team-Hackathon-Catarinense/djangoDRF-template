from simple_history.models import HistoricalRecords

class BaseModelWithHistory(HistoricalRecords):
    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True
        ordering: list[str] = ["-created_at"]
        get_latest_by: str = "created_at"